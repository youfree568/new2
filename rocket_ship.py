import pygame

class RocketShip:
	"""налаштування корабля"""
	def __init__(self, bob):
		"""ініціалізувати корабаль та задати його початкову позицію"""
		self.screen = bob.screen
		self.settings = bob.settings
		self.screen_rect = bob.screen.get_rect()
		# завантаження зображення корабля та отримати його rect
		self.image = pygame.image.load('images/star_ship.bmp')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False
		# self.speed = 0.1
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""оновити поточну позицію корабля"""
		if self.move_left and self.rect.left > -16:
			self.x -= self.settings.speed
		if self.move_right and self.rect.right < self.screen_rect.right + 16:
			self.x += self.settings.speed
		if self.move_up and self.rect.top > 0:
			self.y -= self.settings.speed
		if self.move_down and self.rect.bottom < self.screen_rect.bottom + 5:
			self.y += self.settings.speed

		self.rect.x = self.x
		self.rect.y = self.y
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
