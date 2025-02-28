import pygame
from windows_config import *
from button import Button

class AppWindow():
    def __init__(self, x, y, hight, wight, action, action_args=None):
        self.wight = wight
        self.hight = hight
        self.x = x
        self.y = y
        # self._bord = pygame.Rect(self.x, self.y, self.wight, self.hight)
        self._bord = Button(self.x, self.y, self.wight, self.hight, color='white', text='x')
        self.bords = [Button(self.x, self.y+i*(self.hight/10), self.wight, self.hight/10, color='white', text='x') for i in range(8)]
        self._bar = pygame.Rect(self.x, self.y-APP_BAR_HIGHT, self.wight, APP_BAR_HIGHT)
        self._close_button = Button(self.x+self.wight-APP_BAR_HIGHT, self.y-APP_BAR_HIGHT, APP_BAR_HIGHT, APP_BAR_HIGHT, color='red', text='x', action=action, action_args=action_args)
        return

    def draw(self, screen):
        # pygame.draw.rect(screen, colors['white'], self._bord)
        pygame.draw.rect(screen, colors['gray'], self._bar)
        # self._bord.draw(screen)
        for b in self.bords:
            print(b.text)
            b.draw(screen, True)
        self._close_button.draw(screen)

    def get_button(self):
        return self._close_button





