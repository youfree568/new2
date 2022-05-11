import pygame

class StarShip:

	def __init__(self, ai_game):
		"""беремо екран з alien_invasion.py"""
		self.screen = ai_game.screen
		"""беремо rect екрану"""
		self.screen_rect = ai_game.screen.get_rect()
		"""завантажуємо картинку корабля"""
		self.image = pygame.image.load('images/star_ship.bmp')
		"""беремо rect "квадрат" картинки корабля"""
		self.rect = self.image.get_rect()
		"""робимо позицію корабля на екрані"""
		self.rect.center = self.screen_rect.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)