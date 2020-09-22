from nim_env import NimGameEnv
from nim_player import RandomPlayer

# Follow these steps to run a game of Nim:
# 1. Instantiate two Player objects.
# 2. Instantiate the game by passing the Players to the Nim constructor. (The
#    initial heap sizes and win condition can also be given. The default
#    arguments are (3, 4, 5) and misere.)
# 3. Call play() on the Nim object.
player_1 = RandomPlayer()
player_2 = RandomPlayer()
game = Nim(player_1, player_2)
game.play()

# The history field keeps track of the state of the game and contains the
# following information:
# 1. The player types and win condition.
# 2. The sequence of moves. Each move is a list of the form
#      [player number,
#       (heap sizes before move),
#       (heap index, number of objects to remove)]
# 3. The winner and loser.
print(*game.history, sep='\n')