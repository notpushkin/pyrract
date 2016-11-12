from ..tree import Node


def render_tree(node):
    if not isinstance(node, Node):
        yield node
    elif node._is_final:
        new_node = node.copy()
        new_node.children = [render_tree(child) for child in node.children]
        yield new_node
    else:
        rendered = Node.normalize(node.render())
        for rnode in rendered:
            yield from render_tree(rnode)
