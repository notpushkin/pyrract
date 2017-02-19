# flake8: noqa

import toga

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


class NodeFactory:
    """
    Generates nodes with a given name by using attribute syntax sugar.
    """

    def __init__(self, node_class=Node):
        self.node_class = node_class

    def __getattribute__(self, the_name):
        class _generated(self.node_class):
            name = the_name
        return _generated


dom = NodeFactory()


class TogaNode(Node):
    toga_component = None

    def build(self):
        self.base = self.toga_component(**self.props)

        for child in self.children:
            self.base.add(child.build())

        return self.base


class TogaApp(TogaNode):
    toga_component = toga.App

    def build(self):
        if len(self.children) != 1:
            raise ValueError("TogaApp should have exactly 1 child")

        self.base = self.toga_component(
            startup=lambda app: self.children[0].build(),
            **self.props)

        return self.base


class TogaBox(TogaNode):
    toga_component = toga.Box


class TogaButton(TogaNode):
    toga_component = toga.Button
