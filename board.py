import pygame
import constants
import numpy
import AI

class Board:
    
    PADDING = 5
    RADIUS = constants.SQUARE_SIZE // 2 - PADDING

    def __init__(self, window):

        self.screen = window
        self._init()

    def _init(self):

        self.board = numpy.zeros(( constants.ROWS, constants.COLS ), dtype=tuple)
        self.move_log = []
        self.squares_left = 42
        
        if self.screen != None:
    
            for row in range(constants.ROWS):
                for col in range(constants.COLS):
    
                    pygame.draw.rect( self.screen, 
                                      constants.BLUE, 
                                      (col * constants.SQUARE_SIZE, (row+1) * constants.SQUARE_SIZE, 
                                      constants.SQUARE_SIZE, constants.SQUARE_SIZE) )
       
    def col_full(self, col, board):  
        return board[0][int(col)] != 0
        
    def next_valid_row(self, col, board):
        
        if self.col_full(col, board):
            return -1
            
        for row in range(constants.ROWS - 1):
            if board[row + 1][col] != 0:
                return row
                
        return 5
                
    def manage_drop(self, col, peice):
        
        row = self.next_valid_row(col, self.board)
        
        if row != -1:

            self.board[row][col] = peice
            self.squares_left -= 1

            return True

        return False
        
    def _equal(self, a, b, c, d):
        return(a == b and b == c and c == d and a != 0)
        
    def _score(self, player):
        
        if player == constants.YELLOW:
            return 10
        else:
            return -10
            
    def check_win(self, board, getPos=True):
        
        score = 0
        pos = 0
        
        for r in range(constants.ROWS):
            for c in range(constants.COLS - 3):
                
                if self._equal( board[r][c], board[r][c+1], board[r][c+2], board[r][c+3] ):
                    score = self._score( board[r][c] )
                    pos = ([r, c], [r, c + 3])
        
        for r in range(constants.ROWS - 3):
            for c in range(constants.COLS):
                
                if self._equal( board[r][c], board[r+1][c], board[r+2][c], board[r+3][c] ):
                    score = self._score( board[r][c] )
                    pos = ([r, c], [r + 3, c])
                    
        for r in range(3, constants.ROWS):
            for c in range(constants.COLS - 3):
                
                if self._equal( board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3] ):
                    score = self._score( board[r][c] )
                    pos = ([r, c], [r - 3, c + 3])
                    
        for r in range(constants.ROWS - 3):
            for c in range(constants.COLS - 3):
                
                if self._equal( board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3] ):
                    score = self._score( board[r][c] )
                    pos = ([r, c], [r + 3, c + 3])
                    
        if (not pos) and (not score):
            return None
        
        if getPos:
            return(score, pos)
            
        else:
            return(score)
            
        if self.squares_left == 0:
            return 0
    
    def draw_board(self):
        
        for row in range(constants.ROWS):
            for col in range(constants.COLS):
                
                pos = ( col * constants.SQUARE_SIZE + constants.SQUARE_SIZE // 2, 
                        (row + 1) * constants.SQUARE_SIZE + constants.SQUARE_SIZE // 2 )
                
                radius = self.RADIUS
                
                pygame.draw.circle(self.screen, constants.BLACK, pos, radius)
                
                if self.board[row][col] != 0:
                    pygame.draw.circle(self.screen, self.board[row][col], pos, radius)
                    
                    
        pygame.draw.rect( self.screen, constants.GREEN, (350, 0, 100, 50) )

    def winLine(self, startPos, endPos):
        pygame.draw.line( self.screen, constants.GREEN, startPos, endPos, self.PADDING )

    def ai_move(self):
        return AI.bestMove(self.board)
        
    def printBoard(self, board):
        for r in board:
            print(r)
            
    def reset_board(self):
        self.squares_left = 42
        self._init
        self.screen.fill(constants.BLACK)
        self.draw_board()
        pygame.display.update()
        
    def undo(self):
        self.board = self.board[-2]
            
    def __repr__(self):
        return self.board




                       
            
        