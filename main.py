from graph import build_graph
from player import Player
from node import Node
from util import clear


def main():
  goal = Node(4, 4)
  graph = build_graph(5, 5, goal)

  player_pos = Node(0, 0)
  player = Player(player_pos, graph)
  moves = {
    "w": player.move_up,
    "a": player.move_left,
    "s": player.move_down,
    "d": player.move_right
  }
  
  graph.render()

  # Event loop
  while not player.pos == goal:
    move_dir = input("Move [w][a][s][d]")
    if move_dir in moves:
      moves[move_dir]()

    clear()
    graph.render()

  print("Game over!")

main()