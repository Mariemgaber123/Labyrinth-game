import pygame, sys
from button import Button
from maze import generate_maze



pygame.init()

class InputBox:
    def __init__(self, x, y, w, h, font, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('white')
        self.text = text
        self.font = font
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = pygame.Color('dodgerblue') if self.active else pygame.Color('white')

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode.isdigit():
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
        return None

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_value(self):
        try:
            return int(self.text)
        except:
            return None
def maze_menu():
    SCREEN = pygame.display.set_mode((1678, 1000))
    screen_width, screen_height = SCREEN.get_size()
    
    background_image = pygame.image.load("labyr.jpg")
    background_image = pygame.transform.scale(background_image, (1678, 944))  
    input_box = InputBox(730, 400, 200, 60, get_font(40))
    start_button = Button(image=None, pos=(830, 600), 
                          text_input="START", font=get_font(60), base_color="White", hovering_color="Green")
    

    while True:
       SCREEN.blit(background_image, (0, 0))
       MENU_MOUSE_POS = pygame.mouse.get_pos()
       
       title = get_font(22).render("Enter difficulty of this level (from 1 to 100)", True, "white")
       SCREEN.blit(title, title.get_rect(center=(860, 200)))
       

       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            val = input_box.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
             if start_button.checkForInput(MENU_MOUSE_POS):
               difficulty = input_box.get_value()
               if difficulty is not None and 1 <= difficulty <= 100:
            # Black screen moment
                SCREEN.fill((0, 0, 0))
                pygame.display.update()
                pygame.time.delay(300)  # 300 milliseconds = 0.3 second delay

                play(difficulty)
               else:
                print("Invalid difficulty input!")


       
       input_box.draw(SCREEN)
       start_button.changeColor(MENU_MOUSE_POS)
       start_button.update(SCREEN)

       pygame.display.update()


SCREEN = pygame.display.set_mode((1678, 944))
pygame.display.set_caption("Menu")

BG = pygame.image.load("wallhaven-lmwdyl2.jpg")
BG_rect = BG.get_rect(topleft=(0,0))

game_sfx = pygame.mixer.Sound("Isabella's Lullaby.mp3")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)



def play(difficulty):
    maze = generate_maze(10, 10, difficulty)
    cell_size = 60
    offset_x = 550
    offset_y = 100

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                color = {
                    '#': (40, 40, 40),
                    '.': (200, 200, 200),
                    'S': (0, 255, 0),
                    'E': (255, 0, 0),
                    '*': (0, 255, 255)
                }.get(cell, (255, 255, 255))

                pygame.draw.rect(SCREEN, color,
                                 (offset_x + j * cell_size, offset_y + i * cell_size, cell_size - 2, cell_size - 2))

        
        PLAY_BACK = Button(image=None, pos=(825, 800),
                           text_input="BACK", font=get_font(60), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

    
def options():
   
    
    while True:
        global game_sfx
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill((255, 255, 255))

        OPTIONS_TEXT = get_font(45).render("OPTIONS SCREEN", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(840, 300))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        VOLUME_UP = Button(image=None, pos=(830, 350),text_input="VOLUME UP", font=get_font(50), base_color="Black", hovering_color="Green")
        VOLUME_DOWN = Button(image=None, pos=(830, 450),text_input="VOLUME DOWN", font=get_font(50), base_color="Black", hovering_color="Yellow")
        MUTE = Button( image=None,pos=(830, 550),text_input="MUTE", font=get_font(50), base_color="Black", hovering_color="Red")

        OPTIONS_BACK = Button( image=None,pos=(830, 700),text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

       
        for button in [VOLUME_UP, VOLUME_DOWN, MUTE, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOLUME_UP.checkForInput(OPTIONS_MOUSE_POS):
                    game_sfx.set_volume(min(game_sfx.get_volume() + 0.1, 1.0))   
                if VOLUME_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                    game_sfx.set_volume(max(game_sfx.get_volume() - 0.1, 0.0))  
                if MUTE.checkForInput(OPTIONS_MOUSE_POS):
                    game_sfx.set_volume(0.0)  # كتم الصوت
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()



        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, BG_rect)

        game_sfx.play()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(120).render("MAIN MENU", True, "orange")
        MENU_RECT = MENU_TEXT.get_rect(center=(830, 160))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(830, 500), 
                            text_input="PLAY", font=get_font(80), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(830, 650), 
                            text_input="OPTIONS", font=get_font(80), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(830, 800), 
                            text_input="QUIT", font=get_font(80), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    maze_menu()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()