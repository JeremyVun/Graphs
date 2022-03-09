from node import Node

class Player:
  def __init__(self, pos, graph):
    self.pos = pos
    self.graph = graph

    self.graph.set(self.pos, "O")

  # Everythign below here is what we have done
  def move_up(self):
    self.move(0, -1)

  def move_right(self):
    self.move(1, 0)

  def move_down(self):
    self.move(0, 1)

  def move_left(self):
    self.move(-1, 0)

  def move(self, dx, dy):
    adjacents = self.graph.get_adjacents(self.pos)
    next_pos = Node(self.pos.x + dx, self.pos.y + dy)

    if next_pos in adjacents:
      self.graph.set(self.pos, "_")
      self.pos = next_pos
      self.graph.set(self.pos, "O")
