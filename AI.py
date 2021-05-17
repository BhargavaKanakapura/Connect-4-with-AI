import constants
import numpy
import math
import random

class Computer:
    
    def __init__(self):
        
        self.ai_piece = 2
        self.player_piece = 1
        self.red = constants.RED
        self.yellow = constants.YELLOW

        self.HelperMethods = self.HelperMethods()
        
    def score_window(self, window, two_score=2, three_score=5, four_score=100):
        
        def _contains(piece, number, score):
            return (window.count(piece) == number and window.count(0) == (4 - number)) * score
            
        return (_contains(self.ai_piece, 2, two_score) + 
                _contains(self.ai_piece, 3, three_score) + 
                _contains(self.ai_piece, 4, four_score) -
                _contains(self.player_piece, 3, four_score))

    def score_board(self, board):

        score = 0

        center_array = [int(i) for i in list(board[:, constants.COLS//2])]
        center_count = center_array.count(self.ai_piece)
        score += center_count * 3

        for r in range(constants.ROWS):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(constants.COLS-3):
                window = row_array[c:c+4]
                score += self.score_window(window)

        for c in range(constants.COLS):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(constants.ROWS-3):
                window = col_array[r:r+4]
                score += self.score_window(window)

        for r in range(constants.ROWS-3):
            for c in range(constants.COLS-3):
                window = [board[r+i][c+i] for i in range(4)]
                score += self.score_window(window)

        for r in range(constants.ROWS-3):
            for c in range(constants.COLS-3):
                window = [board[r+3-i][c+i] for i in range(4)]
                score += self.score_window(window)

        return score

    class HelperMethods:

        def __init__(self):
            self.player_piece = 1
            self.ai_piece = 2
            self.red = constants.RED
            self.yellow = constants.YELLOW

        def flip_board(self, board):
            return numpy.flip(board, 0)

        def drop_piece(self, board, col, piece):
            row = self.getNextRow(col, board)
            board[row][col] = piece

        def getNextRow(self, col, board):
            for row in range(constants.COLS):
                if board[row][col] == 0:
                    return row

        def winning_move(self, board, piece):
                    
        	for c in range(constants.COLS-3):
        		for r in range(constants.ROWS):
        			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        				return True
        
        	for c in range(constants.COLS):
        		for r in range(constants.ROWS-3):
        			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        				return True
    
        	for c in range(constants.COLS-3):
        		for r in range(constants.ROWS-3):
        			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        				return True
        
        	for c in range(constants.COLS-3):
        		for r in range(3, constants.ROWS):
        			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
        				return True

        def is_terminal(self, board):
            return (self.winning_move(board, self.ai_piece) or 
                    self.winning_move(board, self.player_piece) or 
                    self.get_valid_moves(board) == False)

        def get_valid_moves(self, board):

            valid_moves = []

            for col in range(constants.COLS):
                if board[constants.ROWS - 1][col] == 0:
                    valid_moves.append(col)

            return valid_moves
            
        def format_board(self, board, mode):
            
            if mode == 1:
                
                formatted_board = numpy.zeros((constants.ROWS, constants.COLS))
                
                for row in range(constants.ROWS):
                    for col in range(constants.COLS):
                        
                        if board[row][col] == constants.RED:
                            formatted_board[row][col] = self.player_piece
                            
                        elif board[row][col] == constants.YELLOW:
                            formatted_board[row][col] = self.ai_piece
                            
                return numpy.flip(formatted_board, 0)
            
            elif mode == 2:
                
                formatted_board = numpy.zeros((constants.ROWS, constants.COLS))
                
                for row in range(constants.ROWS):
                    for col in range(constants.COLS):
                        
                        if board[row][col] == self.ai_piece:
                            formatted_board[row][col] = self.yellow
                            
                        elif board[row][col] == self.player_piece:
                            formatted_board[row][col] = self.red
                            
                return numpy.flip( formatted_board, 0 )

    def minimax(self, board, depth, alpha, beta, isMax):

        valid_moves = self.HelperMethods.get_valid_moves(board)
        is_terminal = self.HelperMethods.is_terminal(board)

        if is_terminal or depth == 0:

            if is_terminal:

                if self.HelperMethods.winning_move(board, self.ai_piece):
                    return None, 1000000
                
                elif self.HelperMethods.winning_move(board, self.player_piece):
                    return None, -1000000

                else:
                    return None, 0

            else:
                return None, self.score_board(board)

        if isMax:

            bestScore = -math.inf
            bestCol = random.choice(valid_moves)

            for col in valid_moves:

                board_copy = board.copy()
                self.HelperMethods.drop_piece(board_copy, col, self.ai_piece)

                new_score = self.minimax(board_copy, depth - 1, alpha, beta, False)[1]

                if new_score > bestScore:
                    bestScore = new_score
                    bestCol = col

                alpha = max(alpha, bestScore)
                if alpha >= beta:
                    break

            return bestCol, bestScore

        if not isMax:

            bestScore = math.inf
            bestCol = random.choice(valid_moves)

            for col in valid_moves:

                board_copy = board.copy()
                self.HelperMethods.drop_piece(board_copy, col, self.player_piece)

                new_score = self.minimax(board_copy, depth - 1, alpha, beta, True)[1]

                if new_score < bestScore:
                    bestScore = new_score
                    bestCol = col

                beta = min(beta, bestScore)
                if alpha >= beta:
                    break

            return bestCol, bestScore

        

def bestMove(boardInp):

    ai = Computer()
    board = ai.HelperMethods.format_board(boardInp, 1)

    return ai.minimax(board, constants.LEVEL, -math.inf, math.inf, True)

    
    

                
            
            
        
        
                    
