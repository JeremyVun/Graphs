class Player:
  def __init__(self, pos, graph):
    self.pos = pos
    self.graph = graph

    self.graph.set(self.pos, "O")
  
  def move_up(self):
    self.move(0, -1)

  def move_down(self):
    self.move(0, 1)

  def move_left(self):
    self.move(-1, 0)

  def move_right(self):
    self.move(1, 0)

  # Do the moving
  def move(self, xDir, yDir):
    next_pos = self.pos.move(xDir, yDir)
    
    # Adj Validations
    adjacents = self.graph.get_adjacents(self.pos)
    if next_pos in adjacents:
      
      # Basic moving
      self.graph.set(self.pos, "_")
      self.pos = next_pos
      self.graph.set(self.pos, "O")
    