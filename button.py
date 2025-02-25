import pygame
from windows_config import *

class Button():
    def __init__(self, x, y, width, height, color='red', text='', action=None, action_args=None):
        print(action)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.update_color(color)
        self.text = text
        self._on_click_action = action
        self._action_args = action_args

        self.layout = None
        self.text_box = None
        self.font = pygame.font.Font(None, 24)
        self.update_layout()
        self.update_text()
        return

    def update_color(self, color):
        self.color = colors[color]

    def update_layout(self):
        self.layout = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen, p=False):
        if self.layout:
            pygame.draw.rect(screen, self.color, self.layout)

        if self.text_box:
            if p:
                print(f"----> {self.y}")
            screen.blit(self._text_render, self.text_box)

    def update_text(self):
        if self.text != '':
            font = pygame.font.Font(None, 24)
            self._text_render = font.render(self.text, True, colors['black'])
            self.text_box = self._text_render.get_rect(center=self.layout.center)
        return

    def update_text_lines(self, lines):
        for i, line in enumerate(lines):
            font = pygame.font.Font(None, 24)
            self._text_render = font.render(line, True, colors['black'])
            # self.text_box = self._text_render.get_rect(center=self.layout.center)
            # self.text_box.y += i*1
            # self.x.blit(self._text_render, self.text_box)
        return

    def click(self):
        if self._on_click_action is not None:
            if self._action_args is None:
                self._on_click_action(self)
            else:
                self._on_click_action(self._action_args)