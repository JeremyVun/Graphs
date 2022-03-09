from util import clear
from graph import build_graph
from node import Node
from player import Player


def main():
  goal = Node(4, 4)
  graph = build_graph(5, 5, goal)

  player_start = Node(0, 0)
  player = Player(player_start, graph)

  moves = {
    "w": player.move_up,
    "a": player.move_left,
    "s": player.move_down,
    "d": player.move_right
  }

  graph.render()

  # Event loop
  while True:
    move_dir = input("Move [w][a][s][d]")
    if move_dir in moves:
      moves[move_dir]()

    clear()
    graph.render()

  print("Game over!")

main()