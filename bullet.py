import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Створити об'єкт bullet у поточній позиції корабля"""
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		# стоворити rect кулі у (0, 0) та задати правильну позицію
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		# Зберігати позицію корабля як десяткове заначення.
		self.y = float(self.rect.y)

	def update(self):
		"""просунути кулю на гору екраном"""
		# оновити десяткову позицію кулі.
		self.y -= self.settings.bullet_speed
		# оновити позицію rect
		self.rect.y = self.y

	def draw_bullet(self):
		"""намалювати кулю на екрані"""
		pygame.draw.rect(self.screen, self.color, self.rect)