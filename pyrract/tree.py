from .util import flatten


class Node:
    _is_final = True  # or False?

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
                    yield "%s(%s) []," % (name, props)
                else:
                    yield "%s(%s) [" % (name, props)
                    for child in node.children:
                        for line in _repr(child):
                            yield "    " + line
                    yield "],"
            else:
                yield repr(node)

        return "\n".join(_repr(self))[:-1]


class Component(Node):
    _is_final = False

    def render(self):
        pass



def render_tree(node):
    if not isinstance(node, Node):
        yield node
    elif node._is_final:
        new_node = node.copy()
        new_node.children = [render_tree(child) for child in node.children]
        yield new_node
    else:
        rendered = Node.normalize(node.render())
        for rnode in rendered:
            yield from render_tree(rnode)
