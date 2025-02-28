import pygame
from windows_config import *
from button import Button
import threading
import random
from time import sleep

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
        self._thread = threading.Thread(target=self.run_nums)
        self._thread_red_flag = False
        self._thread.start()
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

    def run_nums(self):
        while(not self._thread_red_flag):
            sleep(0.01)
            for b in self.bords:
                b.text = self._create_new_line(60)
                b.update_text()

            # self._bord.update_text_lines([self._create_new_line(60) for i in range(5)])
            # self._bord.update_text_lines([self.create_par()])

    def _create_new_line(self, length):
        line = "0" * (length // 2) + "1" * (length // 2)
        shuffle = list(line)
        random.shuffle(shuffle)
        return "".join(shuffle)

    def create_par(self):
        par = ""
        for i in range(3):
            par += self._create_new_line(60)
            par += "\n"
        print(par)
        return par


    def close(self):
        print(f"closing app")
        self._thread_red_flag = True
        self._thread.join()
