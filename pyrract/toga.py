import toga
from .tree import Node


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
