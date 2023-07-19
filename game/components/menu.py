import pygame

from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, summary1, summary2):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.update_message(message)
        self.summary_message1(summary1)
        self.summary_message2(summary2)
        
    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    on_start()

    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon ,self.icon_rect)
        screen.blit(self.textSummary1, self.textSummary1_rect)
        screen.blit(self.textSummary2, self.textSummary2_rect)
        pygame.display.flip()

    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def summary_message1(self, summary1):
        self.summaryMessage1 = summary1
        self.textSummary1 = self.font.render(self.summaryMessage1, True, (0, 0, 255))
        self.textSummary1_rect = self.text.get_rect()
        self.textSummary1_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 70)

    def summary_message2(self, summary2):
        self.summaryMessage2 = summary2
        self.textSummary2 = self.font.render(self.summaryMessage2, True, (0, 0, 255))
        self.textSummary2_rect = self.text.get_rect()
        self.textSummary2_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)

