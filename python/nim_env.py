import abc
from typing import Tuple
import random

class Player(abc.ABC):
    """Abstract base class inherited by all player classes"""
    @abc.abstractmethod
    def move(self, heaps: Tuple[int, ...], misere: bool) -> Tuple[int, int]:
        """Return the next move given the current heaps and win condition. The
        move should be a tuple of the form (heap_index, num_remove).
        """
        pass

    def won(self):
        """This method is called at the end of a game if the player wins.
        Learning agents can override it to trigger a positive reward.
        """
        return None

    def lost(self):
        """This method is called at the end of a game if the player loses.
        Learning agents can override it to trigger a negative reward.
        """
        return None

    @staticmethod
    def heap_choices(heaps):
        """Return the indices of the heaps that still have objects. This is a
        helper method intended to reduce duplicate code in derived classes.
        """
        return [index for index, size in enumerate(heaps) if size > 0]


class Nim(object):
    """Simulate a game of Nim between two players."""
    def __init__(self, player_1, player_2, heaps=(3, 4, 5), misere=True):
        self.current_player = player_1
        self.other_player = player_2
        self.player_numbers = {player_1: 1, player_2: 2}
        self.heaps = list(heaps)
        self.misere = misere
        self.winner = None
        self.loser = None
        self.history = [[(1, player_1.__class__.__name__),
                         (2, player_2.__class__.__name__),
                         ('misere', self.misere)]]

    def play(self):
        """Start the game."""
        # Get moves from each player until the heaps are empty. Note: Players
        # are given a copy of self.heaps so they can't change it directly.
        while self.winner is None:
            move = self.current_player.move(tuple(self.heaps), self.misere)
            self.update_history(move)
            self.update_heaps(move)
            self.check_winner()
            self.current_player, self.other_player = ( # Swap players
                    self.other_player, self.current_player)

        # Append the outcome to history and notify the players.
        outcome = sorted([(self.player_numbers[self.winner], 'won'),
                          (self.player_numbers[self.loser], 'lost')])
        self.history.append(outcome)
        self.winner.won()
        self.loser.lost()

    def update_history(self, move):
        """Add the game state and move to the history."""
        player_number = self.player_numbers[self.current_player]
        heaps = tuple(self.heaps)
        self.history.append([player_number, heaps, move])

    def update_heaps(self, move):
        """Check a move for errors and then apply it to the heaps."""
        heap_index, num_remove = move
        if heap_index not in range(len(self.heaps)):
            raise IndexError("invalid move: " + self.history[-1])
        if num_remove not in range(1, self.heaps[heap_index] + 1):
            raise ValueError("invalid move: " + self.history[-1])
        self.heaps[heap_index] -= num_remove

    def check_winner(self):
        """Check if the game is over. If so, determine the winner."""
        if all(heap == 0 for heap in self.heaps):
            if self.misere:
                self.winner = self.other_player
                self.loser = self.current_player
            else:
                self.winner = self.current_player
                self.loser = self.other_player