import pygame
from windows_config import *
from button import Button
import threading
import random
from time import sleep

class VideoPlayer():
    def __init__(self, x, y, hight, wight, action, action_args=None):
        self.wight = wight
        self.hight = hight
        self.x = x
        self.y = y

        self.images = []
        for i in range(8):
            image = pygame.image.load(rf"media\g{i+1}.jpeg")
            image = pygame.transform.scale(image, (self.wight, self.hight))
            self.images.append(image)

        self._image_index = 0

        self._bar = pygame.Rect(self.x, self.y-APP_BAR_HIGHT, self.wight, APP_BAR_HIGHT)
        self._close_button = Button(self.x+self.wight-APP_BAR_HIGHT, self.y-APP_BAR_HIGHT, APP_BAR_HIGHT, APP_BAR_HIGHT, color='red', text='x', action=action, action_args=action_args)
        # self._thread = threading.Thread(target=self.run_nums)
        # self._thread_red_flag = False
        # self._thread.start()
        return

    def draw(self, screen):
        pygame.draw.rect(screen, colors['gray'], self._bar)
        screen.blit(self.images[self._image_index], (self.x, self.y))
        self._image_index = (self._image_index + 1) % len(self.images)
        # pygame.display.update()
        self._close_button.draw(screen)
        sleep(0.05)
        return

    def get_button(self):
        return self._close_button

    def close(self):
        print(f"closing app")
        # self._thread_red_flag = True
        # self._thread.join()
