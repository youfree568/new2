import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""клас що представляє одного прибульця"""
	def __init__(self, ai_game):
		# наслідоемо клас Sprite
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		# завантажуємо зображення прибульця
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		# позиціонуємо прибульця
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# позиція прибульця по координаті x
		self.x = float(self.rect.x)

	def check_edges(self):
		"""turn TRUE if alien is on edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""змінити розташування прибульця"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x