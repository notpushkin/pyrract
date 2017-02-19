# Pyrract

Pyrract is a React-esque library for Python. It allows you to build component
trees with a simple DSL:

```py
class Header(Component):
    def render(self):
        return dom.header(class_=["foo", "bar"]) [
            dom.h1() ["Hello, world!"]
        ]

class Footer(Component):
    def render(self):
        return dom.footer() [
            dom.p(class_="copy") ["Copyright 2016"],
            dom.p(class_="social") ["Like us on Facebook!"],
        ]

class App(Component):
    def render(self):
        return dom.div() [
            Header(),
            dom.p() ["Y'all"],
            Footer(),
        ]
```

Our primary target is currently [Toga][], an emerging widget
toolkit for desktop (Windows, Linux and macOS) and mobile (Android and iOS).
(It is still in development, but already usable — see the
[platform support][TogaPlatforms] page).

Let's run a quick demo:

```py
>>> from pyrract import render_tree
>>> from pyrract.test import App
>>> next(render_tree(App()))
TogaApp(name='First App', app_id='rocks.ale.TemVillage') [
    TogaBox() [
        TogaButton(label='temmie', on_press=<function ...>) [],
        TogaButton(label='temmie', on_press=<function ...>) [],
        TogaButton(label='temmie', on_press=<function ...>) [],
        TogaButton(label='temmie', on_press=<function ...>) [],
    ],
]
>>> _.build()
<toga_gtk.app.App ...>

>>> _.main_loop()
```

After that, a window with two buttons should appear, each displaying a simple
message (as a dialog on Linux or to stdout on other platforms).

![Screenshot](https://cloud.githubusercontent.com/assets/1298948/23102000/434f0984-f6ba-11e6-8862-d8c0e29bf3d4.png)

For now, nothing really works except from that, so it isn't really useful
right now. Current roadmap is:

- [ ] Component state
- [ ] Diffing component trees and updating

## Prior art

Pyrract is heavily inspired, loosely based on [Preact][], a fast, lightweight
React-compatible JavaScript library. It is totally awesome.


## License

MIT


## Final thoughts

![Fish can't understand what the actual fuck am I doing](https://cloud.githubusercontent.com/assets/1298948/20235885/a5c6a760-a8b9-11e6-926f-ea5f03ee82af.png)


[Toga]: http://pybee.org/project/projects/libraries/toga/
[TogaPlatforms]: https://toga.readthedocs.io/en/latest/reference/index.html#supported-platforms
[Brython]: http://brython.info/
[Preact]: https://preactjs.com/
