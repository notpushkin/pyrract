from .tree import dom, Component


class Header(Component):
    def render(self):
        return dom.header(class_name=["foo", "bar"]) [
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
