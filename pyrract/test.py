import toga
from .tree import render, Component
from .toga import TogaBox, TogaButton


class Root(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"count": 0}

    def do_count(self, widget):
        self.set_state(lambda s: {"count": s["count"] + 1})

    def render(self):
        return TogaBox() [
            TogaButton(label="Needs some pudding, huh"),
            TogaButton(label="Clicked %d times" % self.state["count"],
                       on_press=self.do_count),
        ]


app = toga.App(
    name="TEM COUNTER!!!", app_id="rocks.ale.TemCounter",
    startup=lambda app: render(Root()).base)

if __name__ == '__main__':
    app.main_loop()
