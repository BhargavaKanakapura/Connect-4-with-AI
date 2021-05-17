import pygame
import constants

class PygameNotInstalled(Exception):
    
    def __init__(self):
        self.message = "Python Pygame not installed"
        super().__init__(self.message)
        
class FileNotFound(Exception):
    
    def __init__(self):
        self.message = "File not found"
        super().__init__(self.message)
        
class InvalidInput(Exception):
    
    def __init__(self):
        self.message = "Invalid Input"
        super().__init__(self.message)
        
class InvalidLogin(Exception):
    
    def __init__(self):
        self.message = "Invalid Username or Password"
        super().__init__(self.message)
        
def valid_pass(username, password):
    
    username_list = list(constants.LOGINS.keys())

    if (username in username_list) and (password == constants.LOGINS[username]):
        return True
        
    return False
    

class Text:

    def __init__(self, text, size, x, y, color):
        self.text = text
        self.pos = (x, y)
        self.color = color
        self.size = size
        self.text_img = self.renderText()

    def renderText(self):
        font = pygame.font.Font("freesansbold.ttf", self.size)
        text = font.render(self.text, True, self.color, constants.BLACK)
        return text
        
    def blit_text(self, display):
        display.blit(self.text_img, self.pos)
        