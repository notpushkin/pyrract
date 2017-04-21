# Pyrract

Pyrract is a React-esque library for Python. It allows you to build component
trees with a simple DSL.

Our primary target is currently [Toga][], an emerging widget
toolkit for desktop (Windows, Linux and macOS) and mobile (Android and iOS).
(It is still in development, but already usable — see the
[platform support][TogaPlatforms] page).

[Toga]: http://pybee.org/project/projects/libraries/toga/
[TogaPlatforms]: https://toga.readthedocs.io/en/latest/reference/index.html#supported-platforms

Let's run a quick demo.

```py
class Root(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {"count": 0}

    def do_count(self, widget):
        self.set_state(lambda s: {"count": s["count"] + 1})

    def render(self):
        return TogaBox() [
            TogaButton(label="Needs some pudding, huh"),
            # [TN: pudding means padding, see https://github.com/pybee/toga/issues/139]
            TogaButton(label="Clicked %d times" % self.state["count"],
                       on_press=self.do_count),
        ]


app = toga.App(name="TEM COUNTER!!!", app_id="rocks.ale.TemCounter",
               startup=lambda app: render(Root()).base)
```

If you've seen React, you'll instantly recognize what's going on here.

To try out this code, run:

```
pip install toga
git clone https://github.com/iamale/pyrract && cd pyrract
python -m pyrract.demo
```

Now click that button. C'mon. That's all I've got.

![TEM COUNTER!](https://cloud.githubusercontent.com/assets/1298948/25261125/5f1939ea-2659-11e7-93c4-359bbd4808dc.png)


## Caveats

- You can't remove elements apparently (see [pybee/toga#30][]).
  - Either wait when it's fixed...
  - ...try fix it ourselves...
  - ...or move on to something a bit more stable, like Qt / PySide?

- Needs performance testing. I'm using suboptimal tree comparison

[pybee/toga#30]: https://github.com/pybee/toga/issues/30

## Prior art

Pyrract is heavily inspired, loosely based on [Preact][], a fast, lightweight
React-compatible JavaScript library. It is totally awesome.

[Preact]: https://preactjs.com/


## License

MIT


## Final thoughts

![Fish can't understand what the actual fuck am I doing](https://cloud.githubusercontent.com/assets/1298948/20235885/a5c6a760-a8b9-11e6-926f-ea5f03ee82af.png)
