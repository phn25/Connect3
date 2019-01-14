# Phuong Nguyen
# CS380 - HW3
# Program: MinimaxPlayer.py
# 11/16/2018

import math
import random
from Player import Player

class MinimaxPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    # represents the minimax tree root
    def minimaxMove(self, board):
        allPossibleNextMoves = board.next('O') # the roots level accounts for "O"
        bestMove = None
        bestScore = -math.inf # keep track of max score

        depth = 0 
        
        # find max of all min scores
        for move in allPossibleNextMoves:
            score = self.minValue(move, depth)
            if bestScore < score: # update move and score if there's a new max
                bestMove = move 
                bestScore = score
        return bestMove

    # this function represents how "X" moves
    def minValue(self, board, depth):
        depth += 1

        if self.isTerminalState(board): 
            return self.evaluateMove(board, depth)
        allPossibleNextMoves = board.next('X') 
        bestScore = math.inf

        # find min of all max scores
        for move in allPossibleNextMoves:
            score = self.maxValue(move, depth)
            if score < bestScore:
                bestScore = score
        return bestScore
    

    # this function represents how "O" moves
    def maxValue(self, board, depth):
        depth += 1 

        if self.isTerminalState(board):
            return self.evaluateMove(board, depth)
        allPossibleNextMoves = board.next('O')
        bestScore = -math.inf

        # find max of min scores
        for move in allPossibleNextMoves:
            score = self.minValue(move, depth)
            if score > bestScore:
                bestScore = score
        return bestScore

    def isTerminalState(self, board):
        # board.winner() != None meaning board.winner() can be either 'X', 'O' or 'TIE'
        return board.winner() != None 

    def evaluateMove(self, board, depth): # helps choose the best move at a state
        if board.winner() == 'X': # opponent(X) wins
            return -depth # if O loses, reduce the score so that it won't pick this branch
        elif board.winner() == 'O': # player wins
            return depth 
        else:
            return 0