import UserInterface

try:
    import pygame
except:
    raise UserInterface.PygameNotInstalled()
    
try:
    import game
    import constants
except:
    raise UserInterface.FileNotFound()
    
import math

pygame.init()

DISPLAY = pygame.display.set_mode(( constants.WIDTH, constants.HEIGHT ))
CLOCK = pygame.time

def init():
    pass

def main():
    
    control = game.Game(DISPLAY)
    pygame.display.update()  
    running = control.running
    
    while running:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and (constants.MODE == "PVP" or control.player == constants.RED):
                
                col = event.pos[0] // constants.SQUARE_SIZE
                control.manage_drop(col)

                pygame.display.update()
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                control.board.reset_board()

            if constants.MODE == "PVP" or control.player == constants.RED and control.winner == None:

                x = pygame.mouse.get_pos()[0]
                pygame.draw.circle( DISPLAY, control.player, 
                                    (x - control.board.RADIUS // 2, constants.SQUARE_SIZE // 2), 
                                    control.board.RADIUS )
                
        if control.player == constants.YELLOW and constants.MODE == "PVC":
            
            col, score = control.ai_move()
            control.manage_drop(col)

            print("COL: {} || SCORE: {}".format(col, score))
            pygame.display.update()

        running = control.running

        if running == False:
            CLOCK.wait(2000)

        CLOCK.Clock().tick(30)
        pygame.display.update()
        pygame.draw.rect(DISPLAY, constants.BLACK, (0, 0, constants.WIDTH, constants.SQUARE_SIZE))

def exit():
    print("GOODBYE")
    pygame.quit()

init()    
main()
exit()

