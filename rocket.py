# 12-4

import pygame
import sys

from rocket_settings import RocketSettings
from rocket_ship import RocketShip

class Rocket:
	"""інструкції до ракети"""
	def __init__(self):		
		pygame.init()
		self.settings = RocketSettings()
		# вивести дисплей
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		# вивести корабель 
		self.rocket = RocketShip(self)
		self.x = float(self.rocket.rect.x)
		# напис з назвою програми
		pygame.display.set_caption("Rocket")
		
	def run_game(self):
		"""розпочати гру"""
		while True:
			self._check_events()
			self.rocket.update()
			self._update_screen()

	def _check_events(self):
		"""рефакторінг подій гри"""	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
				
	def _check_keydown_events(self, event):
		"""реакція на натискання клавіші"""
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_LEFT:
			self.rocket.move_left = True
		elif event.key == pygame.K_RIGHT:
			self.rocket.move_right = True
		elif event.key == pygame.K_UP:
			self.rocket.move_up = True
		elif event.key == pygame.K_DOWN:
			self.rocket.move_down = True

	def _check_keyup_events(self, event):
		"""реакція на відпускання клавіші"""
		if event.key == pygame.K_LEFT:
			self.rocket.move_left = False
		elif event.key == pygame.K_RIGHT:
			self.rocket.move_right = False
		elif event.key == pygame.K_UP:
			self.rocket.move_up = False
		elif event.key == pygame.K_DOWN:
			self.rocket.move_down = False


	def _update_screen(self):
		"""рефакторин обновлення екрану"""
		# заливаємо фон 
		self.screen.fill(self.settings.bg_color)
		# виводимо корабель
		self.rocket.blitme()
		# виводимо екран
		pygame.display.flip()
if __name__ == '__main__':
	# створити екземпляр гри на запустити
	ro = Rocket()
	ro.run_game()