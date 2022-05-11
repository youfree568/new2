import pygame

class AttackShip:
	def __init__(self, at_game):
		self.screen = at_game.screen
		self.screen_rect = at_game.screen.get_rect()
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.rect.midleft = self.screen_rect.midleft
		self.settings = at_game.settings
		self.y = float(self.rect.y)
		# індикатор руху
		self.move_up = False
		self.move_down = False

			

	def update(self):
		# рух корабля вгору та вниз
		# оновити значення self.y а не rect
		if self.move_up and self.rect.top > 0:
			self.y -= self.settings.speed
		elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.speed

		# оновити об'єкт rect із self.y
		self.rect.y = self.y

	def blitt(self):
		self.screen.blit(self.image, self.rect)
