#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: Vanessa Fountain vsf2106 
"""

import random
import sys
import time
import numpy as np

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move



        
def compute_utility(board, color):
    #Write the function compute_utility(board, color) that computes the utility of a final game board state (in the format described above). The utility is the number of disks of player color minus the number of disks of the opponent. Hint: The function get_score(board) returns a tuple (number of dark disks, number of light disks)
    
    score = get_score(board)[0] - get_score(board)[1] 
    return score


############ MINIMAX ###############################

def minimax_min_node(board, color):
    #function MIN-VALUE(state) returns a utility value
#if TERMINAL-TEST(state) then return UTILITY(state) v←∞
#for each a in ACTIONS(state) do 
#v ← MIN(v, MAX-VALUE(RESULT(s, a))) return v
    moves = get_possible_moves(board, color) 
    move = min(moves)
    #(col,row) tuples representing legal moves for player color
    results = play_move(board, color, move) 
    #computes successor board state that results from player color playing move (a(col,row)tuple)
    if color.status == "FINAL":
        return color.compute_utility(board, color)
    v = inf
    for (a, s) in color.results(board):
        v = min(v, minimax_max_node(board, color))
    return v

def minimax_max_node(board, color):
    #function MAX-VALUE(state) returns a utility value
#if TERMINAL-TEST(state) then return UTILITY(state) v ← −∞
#for each a in ACTIONS(state) do
#v ← MAX(v, MIN-VALUE(RESULT(s, a))) return v
    moves = get_possible_moves(board, color)
    move = max(moves)
    results = play_move(board, color, move)
    if color.status == "FINAL":
        return color.compute_utility(state, player)
    v = -infinity
    for (a, s) in color.results(board):
        v = max(v, minimax_min_node(board, color))
    return v            
    
def select_move_minimax(board, color):
    #implement the method select_move_minimax(board, color) that selects the action that leads to the state with the highest minimax value. The parameters of the function are the current board (in the format described above) and the color for the AI player, integer 1 for dark and 2 for light. The return value should be a (column, row) tuple, representing the move.
    
    #function MINIMAX-DECISION(state) returns an action
#return arg maxa ∈ ACTIONS(s) MIN-VALUE(RESULT(state, a))


    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    
    i,j = np.argmax(get_possible_moves(board, color),
                           lambda i, j: minimax_min_node(color))
    return i,j
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta):
    return None


def select_move_alphabeta(board, color): 
    return 0,0 


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
