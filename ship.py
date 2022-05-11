import pygame

class Ship:
	"""ship settings"""
	def __init__(self, ai_game):
		"""беремо екран з alien_invasion.py"""
		"""беремо rect екрану"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		"""беремо rect екрану"""
		self.screen_rect = ai_game.screen.get_rect()
		"""завантажуємо картинку корабля"""
		self.image = pygame.image.load('images/ship.bmp')
		"""беремо rect "квадрат" картинки корабля"""
		self.rect = self.image.get_rect()
		"""робимо позицію корабля на екрані"""
		self.rect.midbottom = self.screen_rect.midbottom
		# рух корабля праворуч
		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""обновити поточну позицію корабля на основі індикатора руху"""
		if self.move_right and self.rect.right < self.screen_rect.right:
			# рух вправо
			self.x += self.settings.ship_speed

		if self.move_left and self.rect.left > 0:
			# рух в ліво
			self.x -= self.settings.ship_speed

		if self.move_up and self.rect.top > 0:
			# рух вверх
			self.y -= self.settings.ship_speed
		
		if self.move_down and self.rect.bottom < self.screen_rect.bottom:
			# рух вниз
			self.y += self.settings.ship_speed

		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""намалювати корабель у його поточному розташувані"""
		self.screen.blit(self.image, self.rect)