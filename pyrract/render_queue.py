class RenderQueue:
    def __init__(self, render_component):
        self.items = []
        self.render_component = render_component

    def enqueue_render(self, component):
        if not component._dirty:
            component._dirty = True
            self.items.append(component)
            if len(self.items) == 1:
                self.rerender()  # todo: debounce?

    def rerender(self):
        items = self.items
        self.items = []

        for p in items:
            if p._dirty:
                self.render_component(p)
