import pygame
import threading
import sys

class Window():
    def __init__(self):
        self._running = False
        self._thread = threading.Thread(target=self.run_window)
        self._thread.start()

    def run_window(self):
        pygame.init()

        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("System")
        pygame.mouse.set_visible = False

        background_image = pygame.image.load(rf"media\background.jpg")
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale to fit the window

        button_rect = pygame.Rect(20, 20, 100, 100)  # x, y, width, height
        button_color = (255, 0, 0)

        self._running = True
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass

            screen.blit(background_image, (0, 0))
            pygame.draw.rect(screen, button_color, button_rect)
            font = pygame.font.Font(None, 24)
            text = font.render("Prime95", True, (0, 0, 0))
            text_rect = text.get_rect(center=button_rect.center)
            screen.blit(text, text_rect)
            pygame.display.flip()

        pygame.quit()
