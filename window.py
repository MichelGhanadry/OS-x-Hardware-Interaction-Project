import pygame
import threading
import sys
from windows_config import *
from button import Button
from syscode import SysCode
from app_window import AppWindow
from video_player import VideoPlayer

class Window():
    def __init__(self, windows_events):
        self._windows_events = windows_events
        self.syscode = SysCode()
        self._running = False
        self._thread = threading.Thread(target=self.run_window)
        self._thread.start()
        self._running_prime = False
        self._running_video = False
        self._in_sleep_mode = False

        self._black_screen = None
        return

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
        video_button = Button(130, 20, 100, 100, text='Video', action=self.video_button_action)
        # b2 = Button(140, 20, 100, 100, RED, 'n', self.prime_button_action)
        buttons_list = [prime_button, video_button]
        self.apps_dict = {}

        # Main loop
        self._running = True
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._windows_events.append('exit')
                    self._exit(to_join=False)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the button is clicked
                    for button in buttons_list:
                        if button.layout.collidepoint(event.pos):
                            button.click()

                    for app_name in self.apps_dict:
                        app = self.apps_dict[app_name]
                        if app:
                            button = app.get_button()
                            if button.layout.collidepoint(event.pos):
                                button.click()

                    if self._black_screen is not None:
                        if self._black_screen.layout.collidepoint(event.pos):
                            self._black_screen.click()

            # Draw the background image
            screen.blit(background_image, (0, 0))

            # Draw the button
            for button in buttons_list:
                button.draw(screen)

            for app_name in self.apps_dict:
                app = self.apps_dict[app_name]
                if app:
                    app.draw(screen)

            self.syscode.draw(screen)
            
            if self._in_sleep_mode:
                if self._black_screen is None:
                    self._black_screen = Button(0, 0, SCREEN_WIGHT, SCREEN_HIGHT, color="black", text='', action=self.wake_screen)
                self._black_screen.draw(screen)
            else:
                self._black_screen = None

            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        # sys.exit()

    def wake_screen(self, button):
        print("screen wake")
        self._windows_events.append(f'screen wake')
        return

    def _set_sleep_mode(self, mode):
        self._in_sleep_mode = mode
        return

    def create_button(self, x, y, width, height, color, test):
        button_rect = pygame.Rect(20, 20, 100, 100)  # x, y, width, height
        button_color = RED

    def prime_button_action(self, button):
        self._running_prime = not self._running_prime
        state = 'start' if self._running_prime else 'stop'
        button.update_color('green' if self._running_prime else 'red')
        if self._running_prime:
            self.apps_dict['Prime95'] = AppWindow(150,150,300,550, action=self.close, action_args=button)
        else:
            self.apps_dict['Prime95'].close()
            self.apps_dict['Prime95'] = None
        self._windows_events.append(f'{state} prime95')
        print("Prime95 Button clicked!")
        return
    
    def video_button_action(self, button):
        self._running_video = not self._running_video
        state = 'start' if self._running_video else 'stop'
        button.update_color('green' if self._running_video else 'red')
        if self._running_video:
            self.apps_dict['Video'] = VideoPlayer(200,180,300,550, action=self.close, action_args=button)
        else:
            self.apps_dict['Video'].close()
            self.apps_dict['Video'] = None
        self._windows_events.append(f'{state} video')
        print("Video Button clicked!")
        return

    def close(self, button):
        print('closing')
        self._running_prime = not self._running_prime
        state = 'start' if self._running_prime else 'stop'
        button.update_color('green' if self._running_prime else 'red')
        self.apps_dict['Prime95'].close()
        self.apps_dict['Prime95'] = None
        self._windows_events.append(f'{state} prime95')

    def _exit(self, to_join=True):
        for app_name in self.apps_dict:
            app = self.apps_dict[app_name]
            if app is not None:
                app.close()

        self._running = False
        if to_join:
            self._thread.join()
        
