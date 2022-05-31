import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint
from button import Button

class AlienInvasion:
	"""загальний клас"""
	def __init__(self):

		"""ініціалізувати гру, стврити ресурси гри"""
		pygame.init()
		"""screen settings"""
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		# self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		# self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		# self.settings.screen_width = self.screen.get_rect().width
		# self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption('Hello Alien')
		self.stats = GameStats(self)
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		# self.stars = pygame.sprite.Group()
		self._create_fleet()	
		self.play_button = Button(self, 'Play')
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
			if self.stats.game_active:
				self.ship.update()
				self.bullets.update()
				# видаляти кулі при покидані екрану
				self._update_bullets()
				self._update_alien()
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
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		"""if mouse click on "PLAY" button starts game"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# анулювати ігрову статистику
			self.stats.reset_stats()
			self.stats.game_active = True
			# позбавитися надлишку прибульців та куль.
			self.aliens.empty()
			self.bullets.empty()
			# створити влот і відцентрувати корабель
			self._create_fleet()
			self.ship.center_ship()
			pygame.mouse.set_visible(False)

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
		self._check_bullet_alien_collisions()	

	def _check_bullet_alien_collisions(self):
		"""reaction to a collision with a bullet"""
		# remove all bullets and aliens that collided
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)
		if not self.aliens:
			# destroy bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()


	def _create_fleet(self):
		# беремо зірку
		# 13-1
		alien = Alien(self)
		# додаємо зірку до списку
		# при додаванні тут зірки вона буде відображатися у своєму списку як
		# дефолтна і буде дублюватись, тому тут цей рядок дублює першу зірку 
		#  без потреби
		# self.stars.add(star)
		# беремо ширину та висту прибульця
		alien_width, alien_height = alien.rect.size
		# скільки місця є для прибульців
		available_space_x = self.settings.screen_width - (2 * alien_width)
		# кількість прибульців в ряді
		alien_number_x = available_space_x // (2 * alien_width)
		# number of rows
		available_space_y = (self.settings.screen_height - self.ship.rect.height 
		- (alien_height * 3))
		number_rows = available_space_y // (2 * alien_height)
		print(f"number of rows: {number_rows}")
		# create all fleet
		for row_number in range(number_rows):
			for alien_number in range(alien_number_x):
				# створити зірку та поставити її в ряд
				# random_number = randint(-10, 10) - додати у формулу star.x
				# print(random_number)
				self._create_alien(alien_number, row_number)
			
		

	def _create_alien(self, alien_number, row_number):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""реагує відповідно до того, чи досяг котрийсь із прибульців
		краю екрана
		"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""спуск всього флоту та зміна його напрямку"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _ship_hit(self):
		"""respond to hit alien with ship"""
		# reduce ships_left.
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			# позбавити надлишку прибульців та куль
			self.aliens.empty()
			self.bullets.empty()
			# створити новий флот та відцентрувати корабель
			self._create_fleet()
			self.ship.center_ship()
			# pause
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)
			print("Game over")

	def _check_aliens_bottom(self):
		"""check if the alien touch the bottom screen"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# зреагувати так ніби корабель було підбито
				self._ship_hit()
				break

	def _update_alien(self):
		"""
		check if fleet is on thr edge 
		of the screen and update all the aliens
		"""
		self._check_fleet_edges()
		self.aliens.update()
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		# make sure the alien touches the bottom of the screen
		self._check_aliens_bottom()

	def _update_screen(self):
		"""обновляємо екран"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		
		self.aliens.draw(self.screen)
		# намалювани іншопланетянена 
		# self.aliens.draw(self.screen)
		if not self.stats.game_active:
			self.play_button.draw_button()
			
		pygame.display.flip()
	
# print(sys.__doc__)
# help(sys)
# help(pygame)
if __name__ == '__main__':
	"""create copy game and run game"""
	ai = AlienInvasion()
	ai.run_game()
	