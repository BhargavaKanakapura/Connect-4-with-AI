import pygame
import board
import constants
import UserInterface

class Game:
    
    def __init__(self, screen):
        
        self.board = board.Board(screen)
        self.player = constants.RED
        self.winner = None
        self.running = True
        self.screen  = screen
        self.drawBoard()

    def reset(self):
        
        self.board.clear_board()
        self.player = constants.RED
        self.winner = None
        self.running = True
        
    def manage_drop(self, col):
        
        self.winner = self.board.check_win(self.board.board)
        
        if self.winner == None:
            sucess = self.board.manage_drop(col, self.player)
            
        if self.winner != None:
            
            pos = lambda row, col: (col * constants.SQUARE_SIZE + constants.SQUARE_SIZE // 2, 
                                   (row+1) * constants.SQUARE_SIZE + constants.SQUARE_SIZE // 2)
            self.board.winLine(
                pos( self.winner[1][0][0], self.winner[1][0][1] ), 
                pos( self.winner[1][1][0], self.winner[1][1][1] ) )

            sucess = False

            if self.winner == 10:
                UserInterface.Text("YELLOW WINS", constants.SQUARE_SIZE, 0, 0, constants.YELLOW).blit_text(self.screen)
            
            if self.winner == -10:
                UserInterface.Text("RED WINS", constants.SQUARE_SIZE, 0, 0, constants.RED).blit_text(self.screen)

            pygame.display.flip()

        if sucess:      
            self.changePlayer()

        self.drawBoard()
        
    def changePlayer(self):
        
        if self.player == constants.RED:
            self.player = constants.YELLOW
            
        else:
            self.player = constants.RED
            
    def drawBoard(self):
        self.board.draw_board()
        
    def ai_move(self):
        return self.board.ai_move()

    