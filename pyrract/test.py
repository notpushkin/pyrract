from .toga import Component, TogaApp, TogaBox, TogaButton

try:
    from gi.repository import Gtk

    def info_dialog(title, message):
        """
        Copied from https://github.com/pybee/toga/blob/master/src/gtk/toga_gtk/dialogs.py,
        so obviously if would only work on Linux.

        TODO: replace with toga.dialog.info import when it becomes available.
        """

        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK, title)
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()

except ImportError:
    print("Dialogs won't work on your platform (yet!), look in stdout instead.")

    def info_dialog(title, message):
        print("[%s] %s" % (title, message))


class App(Component):
    def dialog(self, text):
        info_dialog("TEM MESSAGE!!!", text)

    def temmie_1(self, widget):
        self.dialog("hOI!!")
        self.dialog("im temmie!!!")
        self.dialog("and dis is my friend...")
        self.dialog("temmie!!!")

    temmie_2 = temmie_1

    def temmie_3(self, widget):
        self.dialog("hOI!!")
        self.dialog("im temmie!!!")
        self.dialog("don forget my friend!")

    def temmie_4(self, widget):
        self.dialog("Hi.")
        self.dialog("I'm Bob.")

    def render(self):
        return TogaApp(name="TEM VILLAGE!!!", app_id="rocks.ale.TemVillage") [
            TogaBox() [
                TogaButton(label="temmie", on_press=self.temmie_1),
                TogaButton(label="temmie", on_press=self.temmie_2),
                TogaButton(label="temmie", on_press=self.temmie_3),
                TogaButton(label="temmie", on_press=self.temmie_4),
            ]
        ]
