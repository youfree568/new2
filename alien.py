import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""клас що представляє одного прибульця"""
	def __init__(self, ai_game):
		# наслідоемо клас Sprite
		super().__init__()
		self.screen = ai_game.screen
		# завантажуємо зображення прибульця
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		# позиціонуємо прибульця
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# позиція прибульця по координаті x
		self.x = float(self.rect.x)