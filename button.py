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