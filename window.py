import pygame
import threading
import sys
from windows_config import *
from syscode import SysCode

class Window():
    def __init__(self, windows_events):
        self._windows_events = windows_events
        self.syscode = SysCode()
        self._running = False
        self._thread = threading.Thread(target=self.run_window)
        self._thread.start()
        self._running_prime = False

    def run_window(self):
        # Initialize Pygame
        pygame.init()

        # Screen dimensions
        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("System")
        pygame.mouse.set_visible = False
        # Colors
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)

        # Load background image
        background_image = pygame.image.load(rf"media\background.jpg")
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale to fit the window

        # Button properties
        # button_rect = pygame.Rect(20, 20, 100, 100)  # x, y, width, height
        # button_color = RED

        prime_button = Button(20, 20, 100, 100, text='Prime95', action=self.prime_button_action)
        # b2 = Button(140, 20, 100, 100, RED, 'n', self.prime_button_action)
        buttons_list = [prime_button]

        # Main loop
        self._running = True
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    self._windows_events.append('exit')

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the button is clicked
                    for button in buttons_list:
                        if button.layout.collidepoint(event.pos):
                            button.click()

                    # if b2.layout.collidepoint(event.pos):
                    #     b2.click()
                        
                    # if button_rect.collidepoint(event.pos):
                    #     self._windows_events.append('start prime95')
                    #     print("Button clicked!")
                    #     button_color = GREEN  # Change button color to green

            # Draw the background image
            screen.blit(background_image, (0, 0))

            # Draw the button
            for button in buttons_list:
                button.draw(screen)

            self.syscode.draw(screen)

            # pygame.draw.rect(screen, button_color, button_rect)
            # b2.draw(screen)

            # Draw button text
            # font = pygame.font.Font(None, 24)
            # text = font.render("Prime95", True, BLACK)
            # text_rect = text.get_rect(center=button_rect.center)
            # screen.blit(text, text_rect)

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        # sys.exit()

    def create_button(self, x, y, width, height, color, test):
        button_rect = pygame.Rect(20, 20, 100, 100)  # x, y, width, height
        button_color = RED

    def prime_button_action(self, button):
        self._running_prime = not self._running_prime
        state = 'start' if self._running_prime else 'stop'
        button.update_color('green' if self._running_prime else 'red') 
        self._windows_events.append(f'{state} prime95')
        print("Prime95 Button clicked!")



class Button():
    def __init__(self, x, y, width, height, color='red', text='', action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.update_color(color)
        self.text = text
        self._on_click_action = action

        self.layout = None
        self.text_box = None
        self.update_layout()
        self.update_text()
        return

    def update_color(self, color):
        self.color = colors[color]

    def update_layout(self):
        self.layout = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        if self.layout:
            pygame.draw.rect(screen, self.color, self.layout)

        if self.text_box:
           screen.blit(self._text_render, self.text_box)

    def update_text(self):
        if self.text != '':
            font = pygame.font.Font(None, 24)
            self._text_render = font.render(self.text, True, (0, 0, 0))
            self.text_box = self._text_render.get_rect(center=self.layout.center)

    def click(self):
        if self._on_click_action is not None:
            self._on_click_action(self)