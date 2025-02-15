import pygame
from windows_config import *

class SysCode():
    def __init__(self, num_Of_digits=4):
        self.code = '0000'
        self.num_Of_digits = num_Of_digits
        print(BORD_X)
        print(BORD_Y)
        print(BORD_WIGHT)
        print(BORD_HIGHT)
        self._bord = pygame.Rect(BORD_X, BORD_Y, BORD_WIGHT, BORD_HIGHT)
        self._digits_list = [Digit(i) for i in range(num_Of_digits)]
        # pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, colors['white'], self._bord)
        for digit in self._digits_list:
           digit.draw(screen)

    

class Digit():
    def __init__(self, digit_index):
        self.digit_index = digit_index
        D = self.digit_index * (2*PIN_SHORT + PIN_LONG + 10)
        self._pins = [pygame.Rect(BORD_X+11+PIN_SHORT+D, BORD_Y+16, PIN_LONG, PIN_SHORT),
                      pygame.Rect(BORD_X+11+D, BORD_Y+16+PIN_SHORT, PIN_SHORT, PIN_LONG),
                      pygame.Rect(BORD_X+11+PIN_SHORT+D, BORD_Y+16+PIN_SHORT+PIN_LONG, PIN_LONG, PIN_SHORT),
                      pygame.Rect(BORD_X+11+PIN_SHORT+PIN_LONG+D, BORD_Y+16+PIN_SHORT, PIN_SHORT, PIN_LONG),
                      pygame.Rect(BORD_X+11+D, BORD_Y+16+2*PIN_SHORT+PIN_LONG, PIN_SHORT, PIN_LONG),
                      pygame.Rect(BORD_X+11+PIN_SHORT+D, BORD_Y+16+2*PIN_SHORT+2*PIN_LONG, PIN_LONG, PIN_SHORT),
                      pygame.Rect(BORD_X+11+PIN_SHORT+PIN_LONG+D, BORD_Y+16+2*PIN_SHORT+PIN_LONG, PIN_SHORT, PIN_LONG),
                    ]

    def draw(self, screen):
        for pin in self._pins:
           pygame.draw.rect(screen, colors['red'], pin) 
