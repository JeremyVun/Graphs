from node import Node

class Graph:
  def __init__(self, graph):
    self.graph = graph
    self.height = len(graph)
    self.width = len(graph[0])

  def render(self):
    for row in self.graph:
      print(row)

  # set(Node(4, 4), "X")
  def set(self, node, value):
    self.graph[node.y][node.x] = value

  # Return valid moves around the node
  def get_adjacents(self, node):
    adjacents = []

    # Get the node to the right of us
    if node.x < self.width - 1:
      adjacents.append(Node(node.x+1, node.y))

    # Get the node to the left of us
    if node.x > 0:
      adjacents.append(Node(node.x-1, node.y))

    # Get the node below us
    if node.y < self.height - 1:
      adjacents.append(Node(node.x, node.y+1))

    # Get the node above us
    if node.y > 0:
      adjacents.append(Node(node.x, node.y-1))

    return adjacents
    


# Factory pattern
# Graph factory -> creates graph objects
def build_graph(width, height, goal):
  rows = []
  for i in range(height):
    row = ["_" for x in range(width)]
    rows.append(row)

  graph = Graph(rows)
  graph.set(goal, "X")
  return graph
