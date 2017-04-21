import toga
from .tree import Element


class TogaElement(Element):
    toga_component = None

    def destroy(self):
        print("Not available :V")

    def set_props(self, next_props):
        for name, value in next_props.items():
            setattr(self.base, name, value)

    def build(self, parent=None):
        self.base = self.toga_component(**self.props)

        for child in self.children:
            self.base.add(child.build())

        return self.base


class TogaBox(TogaElement):
    toga_component = toga.Box


class TogaButton(TogaElement):
    toga_component = toga.Button
