# Phuong Nguyen
# CS380 - HW3
# Program: Game.py
# 11/16/2018

import random
from Player import Player
from RandomPlayer import RandomPlayer
from MinimaxPlayer import MinimaxPlayer

class Game:
    def __init__(self, board):
        self.board = board
    
    # 2 random players play against each other
    def playRandom(self):
        p1 = RandomPlayer("X")
        p2 = RandomPlayer("0")

        currentPlayer = p1
        currentBoard = p1.randomMove(self.board) # p1 makes a random move and updates current board

        solution = []
        random.seed()

        while True:
            solution.append(currentBoard)

            if currentBoard.winner(): # stop when there's a winner
                if currentBoard.winner() == "TIE":
                    print(currentBoard.winner())
                else:
                    print(currentBoard.winner(), "wins")
                break
            else:
                if currentPlayer.equals(p1): # change turn
                    currentPlayer = p2
                else: # change turn
                    currentPlayer = p1
                currentBoard = currentPlayer.randomMove(currentBoard)
        return solution

    # A random player plays against a minimax player
    def playMinimax(self):
        p1 = RandomPlayer("X")
        p2 = MinimaxPlayer("O")
        
        random.seed()

        currentPlayer = p1
        currentBoard = p1.randomMove(self.board) # p1 makes a random move and updates current board

        solution = []

        while True:
            solution.append(currentBoard)

            if currentBoard.winner(): # stop when there's a winner
                if currentBoard.winner() == "TIE":
                    print(currentBoard.winner())
                else:
                    print(currentBoard.winner(), "wins")
                break
            else:
                if currentPlayer.equals(p1): # change turn
                    currentPlayer = p2
                    currentBoard = currentPlayer.minimaxMove(currentBoard) # p2 makes a minimax move and updates current board
                else: # change turn
                    currentPlayer = p1
                    currentBoard = currentPlayer.randomMove(currentBoard)
        return solution