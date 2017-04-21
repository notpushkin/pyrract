from collections import namedtuple
from itertools import zip_longest

from .util import flatten


class Node:
    def __init__(self, children=None, **props):
        self.props = props
        self._children = []
        if children is not None:
            self.children = children

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = list(self.normalize(children))

    @staticmethod
    def normalize(node_or_nodes):
        return flatten([node_or_nodes])

    def copy(self):
        return self.__class__(**self.props.copy())

    def __getitem__(self, children):
        """
        DSL for adding children. Duh.
        """
        self.children = children
        return self

    def __repr__(self):
        def _repr(node):
            if isinstance(node, Node):
                name = getattr(node, "name", node.__class__.__name__)
                props = ", ".join(("%s=%r" % (k, v)
                                   for k, v in node.props.items()
                                   if k != "children"))
                if len(node.children) == 0:
                    yield "%s(%s)," % (name, props)
                else:
                    yield "%s(%s) [" % (name, props)
                    for child in node.children:
                        for line in _repr(child):
                            yield "    " + line
                    yield "],"
            else:
                yield repr(node)

        return "\n".join(_repr(self))[:-1]


class Element(Node):
    _is_final = True

    def set_props(self, props):
        self.props.update(props)

    def destroy(self):
        pass

    def build(self, parent=None):
        pass


class Component(Node):
    _is_final = False

    def __init__(self, **props):
        super().__init__(**props)

        self._dirty = False

        self.state = {}
        self._pending_state = None
        self._rendered_component = None
        self._current_element = None

    def set_state(self, f=None, **partial_state):
        """
        Either
            set_state(x=0)
        or
            set_state(lambda state: {"x": state["x"] + 1})
        """
        if callable(f):
            partial_state = f(self.state)
        self._pending_state = {}
        self._pending_state.update(self.state)
        self._pending_state.update(partial_state)
        self._dirty = True

        update_if_needed(self)

    def render(self):
        raise NotImplementedError()


def render_tree(node, build=False):
    """
    Renders an Element tree from a Component tree.

    Args:
        build: if True, builds all the elements. If a node is given,
               it is considered a parent (little dirty private API).
    """

    parent = build if isinstance(build, Node) else None

    if not isinstance(node, Node):
        raise TypeError("%r is not a Node" % node)
    elif node._is_final:  # Element
        new_node = node.copy()
        new_node.children = [render_tree(child, build=new_node)
                             for child in node.children]
        if build:
            new_node.build(parent=parent)
        yield new_node
    else:  # Component
        if node._dirty:
            node._dirty = False
            node.state = node._pending_state
        rendered = Node.normalize(node.render())
        for rnode in rendered:
            yield from render_tree(rnode, build=parent or True)


def update_tree(prev_root, next_root, parent=None):
    """
    Updates an Element tree, rebuilding if necessary.
    """

    if prev_root is None:
        next_root.build(parent=parent)
        return next_root
    if prev_root.name != next_root.name:
        prev_root.destroy()
        next_root.build(parent=parent)
        return next_root
    else:
        prev_root.set_props(next_root.props)
        children = []
        for prev_child, next_child in zip_longest(prev_root.children,
                                                  next_root.children):
            if prev_child is None:
                children.append(next_child.build(parent=prev_root))
            elif next_child is None:
                prev_child.destroy()
            else:
                children.append(update_tree(prev_child, next_child,
                                            parent=prev_root))

        prev_root.children = children

        return prev_root


root_component = None
root_element = None


def render(node):
    """
    Render and build tree at `node` and remember it so it can be updated.
    """

    global root_component
    global root_element
    root_component = node
    root_element = next(render_tree(node, build=True))
    return root_element


def update_if_needed(component):
    update_tree(root_element, next(render_tree(root_component)))
