import networkx as nx
import matplotlib.pyplot as plt
import uuid

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [tree.nodes[node]['color'] for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
    plt.show()

def generate_color_shade(start_color, end_color, n):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))

    gradient = [('#%02x%02x%02x' % (
        int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / n),
        int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / n),
        int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / n)
    )) for i in range(n)]
    return gradient

def depth_first_traversal(node, colors, visited):
    if node is not None and node not in visited:
        visited.add(node)
        node.color = colors.pop(0)
        depth_first_traversal(node.left, colors, visited)
        depth_first_traversal(node.right, colors, visited)

def breadth_first_traversal(root, start_color, end_color):
    visited = set()
    queue = [(root, start_color)]
    level_colors = {}
    while queue:
        node, color = queue.pop(0)
        if node is not None and node not in visited:
            visited.add(node)
            node.color = color
            level_colors.setdefault(node, color)
            if node.left:
                queue.append((node.left, color))
            if node.right:
                queue.append((node.right, color))
    
    for i, node in enumerate(level_colors):
        gradient = generate_color_shade(start_color, end_color, len(level_colors))
        node.color = gradient[i]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

blue_shade = generate_color_shade("#0000FF", "#ADD8E6", 7)

depth_first_traversal(root, blue_shade.copy(), set())
draw_tree(root)

for node in nx.DiGraph().nodes(data=True):
    node[1]['color'] = "#FFFFFF"

red_shade = generate_color_shade("#800000", "#FF5733", 7)

breadth_first_traversal(root, red_shade[0], red_shade[-1])
draw_tree(root)
