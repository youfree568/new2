import pygame

from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		# завантаження зображення
		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()
		# визначення позиції
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)
