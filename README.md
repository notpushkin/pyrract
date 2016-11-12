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

and render them:

```py
>>> from pyrract import render_tree
>>> from pyrract.test import App
>>> list(render_tree(App()))
[div() [
    header(class_=['foo', 'bar']) [
        h1() [
            'Hello, world!'
        ],
    ],
    p() [
        "Y'all"
    ],
    footer() [
        p(class_='copy') [
            'Copyright 2016'
        ],
        p(class_='social') [
            'Like us on Facebook!'
        ],
    ],
]]
```

For now, nothing really works except from that, so it isn't really useful
right now. Current roadmap is:

- [ ] Component state
- [ ] Diffing component trees and updating
- [ ] Finally, make something useful, like:
  - [ ] Desktop GUI interfaces (Qt / Gtk?)
  - [ ] Mobile apps (like React Native, but in Python)
  - [ ] Interacting with real DOM (using [Brython][] probably)


## Prior art

Pyrract is heavily inspired, loosely based on [Preact][], a fast, lightweight
React-compatible library. It is totally awesome.


## License

MIT


## Final thoughts

![Fish can't understand what the actual fuck am I doing](https://cloud.githubusercontent.com/assets/1298948/20235885/a5c6a760-a8b9-11e6-926f-ea5f03ee82af.png)


[Brython]: http://brython.info/
[Preact]: https://preactjs.com/
