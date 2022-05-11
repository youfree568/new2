import pygame

from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self, al_game):
		super().__init__()
		self.screen = al_game.screen
		self.screen_rect = al_game.screen.get_rect()
		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()

		self.rect.center = self.screen_rect.center
		self.rect.y = self.rect.height