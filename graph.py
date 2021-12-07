class Graph:
  def __init__(self, graph):
    self.width = len(graph[0])
    self.height = len(graph)
    self.graph = graph
    
  def render(self):
    for row in self.graph:
      print(row)

  def set(self, node, value):
    self.graph[node.y][node.x] = value


  ####
  # STUDENTS TO IMPLEMENT THIS FUNCTION
  ####
  def get_adjacents(self, node):
    adjacents = []

    # Get node to the right
    if node.x < self.width - 1:
      adjacents.append(node.move(1, 0))

    # Get node to the left
    if node.x > 0:
      adjacents.append(node.move(-1, 0))

    # Get node above us
    if node.y < self.height - 1:
      adjacents.append(node.move(0, 1))

    # Get node below us
    if node.y > 0:
      adjacents.append(node.move(0, -1))
    
    return adjacents


def build_graph(width, height, goal):
  rows = []
  for y in range(height):
    row = ["_" for x in range(width)]
    rows.append(row)

  graph = Graph(rows)
  graph.set(goal, "X")

  return graph