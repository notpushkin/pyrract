"""
>>> from pyrract.tree import *
>>> x = X()
>>> t1 = next(render_tree(x, build=True))
Built B at A !
Built B at A !
Built A at <root> !
>>> t1
A() [
    B(foo='bar') [],
    B(foo='baz') [],
]
>>> x.set_state(type=C)
>>> t2 = next(render_tree(x))  # no build happens here
>>> update_tree(t1, t2)
Built C at A !
Built C at A !
>>> t1
A() [                 # A() doesn't get rebuilt
    C(foo='bar') [],  # but C's do
    C(foo='baz') [],
]
"""

from .tree import Element, Component


class TestElement(Element):
    def build(self, parent=None):
        print("Built", self.name, "at", getattr(parent, "name", "<root>"), "!")


class A(TestElement): pass  # noqa
class B(TestElement): pass  # noqa
class C(TestElement): pass  # noqa


class X(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "type": B
        }

    def render(self):
        return A() [
            self.state["type"](foo="bar"),
            self.state["type"](foo="baz"),
        ]
