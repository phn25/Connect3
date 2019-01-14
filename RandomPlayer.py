# Phuong Nguyen
# CS380 - HW3
# Program: RandomPlayer.py
# 11/16/2018

import random
from Player import Player

class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def randomMove(self, board):
        allPossibleNextBoards = board.next(super().getName())
        # randomly pick a move in a list of all possible next moves
        rand = random.randint(0, len(allPossibleNextBoards) - 1)
        return allPossibleNextBoards[rand] 