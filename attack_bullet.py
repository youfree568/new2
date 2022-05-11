import pygame
from pygame.sprite import Sprite

class AttackBullet(Sprite):
	"""клас керування кулями випущеними з корабля"""
	def __init__(self, at_game):
		# наслідуємо клас Sprite
		super().__init__()
		self.screen = at_game.screen
		self.settings = at_game.settings
		self.color = self.settings.bullet_color
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midright =  at_game.ship.rect.midright
		self.x = float(self.rect.x)

	def update(self):
		"""просунути кулю нагору екраном"""
		# оновити десяткову позицію кулі
		self.x += self.settings.bullet_speed
		# оновити позицію кулі
		self.rect.x = self.x

	def draw_bullet(self):
		""" намалювати кулю на екрані"""
		pygame.draw.rect(self.screen, self.color, self.rect)