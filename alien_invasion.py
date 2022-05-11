import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint

class AlienInvasion:
	"""загальний клас"""
	def __init__(self):

		"""ініціалізувати гру, стврити ресурси гри"""
		pygame.init()
		"""screen settings"""
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		# self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		# self.settings.screen_width = self.screen.get_rect().width
		# self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption('Hello Alien')
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		# self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()
		self._create_fleet()	
		"""create a ship"""
		# self.screen_rect = self.screen.get_rect()
		# self.image = pygame.image.load('images/ship.bmp')
		# в даному випадку я позиціоную корабель в рамках картинки ship
		# тобто якщо ship.bmp 100х100 то це моя область роботи і з розмірами к
		# self.rect = self.image.get_rect()
		# self.rect.midbottom = self.screen.get_rect().midbottom

	# def blitme(self):
		"""відображаємо корабель"""
		# self.screen.blit(self.image, self.rect)

	def run_game(self):
		"""check event and show screen"""
		while True:
			self._check_events()
			self.ship.update()
			self.bullets.update()
			# видаляти кулі при покидані екрану
			self._update_bullets()
			self._update_screen()

	def _check_events(self):
		"""перевірити значення кнопки"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			# припинення руху
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		# реакція на натискання клавіші
		if event.key == pygame.K_RIGHT:
			# рух вправо
			self.ship.move_right = True
		elif event.key == pygame.K_LEFT:
			# рух вліво
			self.ship.move_left = True
		elif event.key == pygame.K_UP:
			# рух вверх 
			self.ship.move_up = True
		elif event.key == pygame.K_DOWN:
			# рух вниз
			self.ship.move_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
			
	def _check_keyup_events(self, event):
		# реакція на відпускання клавіші
		# вправо
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = False
		# вліво
		elif event.key == pygame.K_LEFT:
			self.ship.move_left = False
		# вверх
		elif event.key == pygame.K_UP:
			self.ship.move_up = False
		# вниз
		elif event.key == pygame.K_DOWN:
			self.ship.move_down = False
			
	def _fire_bullet(self):
		"""створити нову кулю та додати її до групи куль"""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""оновити позицію колі та позбавитись старих куль"""
		# оновити поціції куль
		self.bullets.update()
		# позбавитись кулі що зникла
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _create_fleet(self):
		# беремо зірку
		# 13-1
		star = Star(self)
		# додаємо зірку до списку
		# при додаванні тут зірки вона буде відображатися у своєму списку як
		# дефолтна і буде дублюватись, тому тут цей рядок дублює першу зірку 
		#  без потреби
		# self.stars.add(star)
		# беремо ширину зірки
		star_width = star.rect.width
		# скільки місця є для зірок
		available_space_x = self.settings.screen_width - (2 * star_width)
		# кількість зірок в ряді
		star_number_x = available_space_x // (2 * star_width)
		# створення першого ряду зірок
		for star_number in range(star_number_x):
			# створити зірку та поставити її в ряд
			# random_number = randint(-10, 10) - додати у формулу star.x
			# print(random_number)
			star = Star(self)
			star.x = star_width + 2 * star_width * star_number
			star.rect.x = star.x
			self.stars.add(star)

			# this commit is test 1
			# this commit is test 2
	# def _create_fleet(self):
		# """Створити флот прибульців"""
	# 	# створити прибульця
	# 	alien = Alien(self)
	# 	alien_width, alien_height = alien.rect.size
	# 	available_space_x = self.settings.screen_width - (2 * alien_width)
	# 	number_alien_x = available_space_x // (2 * alien_width)
	# 	# створити перший ряд прибульців
		# for alien_number in range(number_alien_x):
			# self._create_alien(alien_number)

		# визначити, яка кількість рядів прибульців поміщається на екрані.
		# ship_height = self.ship.rect.height
		# available_space_y = (self.settings.screen_height -
		# 					(alien_height * 3) - ship_height)
		# number_rows = available_space_y // (2 * alien_height)
		# створити повний флот прибульців.
		# for row_number in range(number_rows):
		# 	for alien_number in range(number_alien_x):
		# 		self._create_alien(alien_number, row_number)


	# def _create_alien(self, alien_number, row_number):	
	# 	# створити прибульця та поставити його до ряду
	# 	alien = Alien(self)
	# 	alien_width, alien_height = alien.rect.size
	# 	alien.x = alien_width + 2 * alien_width * alien_number
	# 	alien.rect.x = alien.x
	# 	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	# 	self.aliens.add(alien)
	
	def _update_screen(self):
		"""обновляємо екран"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.stars.draw(self.screen)
		# намалювани іншопланетянена 
		# self.aliens.draw(self.screen)
		pygame.display.flip()
# print(sys.__doc__)
# help(sys)
# help(pygame)
if __name__ == '__main__':
	"""create copy game and run game"""
	ai = AlienInvasion()
	ai.run_game()