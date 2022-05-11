import sys
import pygame 

from settings_attack import SettingsAttack
from attack_ship import AttackShip
from attack_bullet import AttackBullet
from star_right import Star

class Attack:

	def __init__(self):
		# ініціалізація гри
		pygame.init()
		self.settings = SettingsAttack()
		# створення параметрів екрану
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		# назва гри над вікно
		pygame.display.set_caption("Attack left")
		# малюємо корабля
		self.ship = AttackShip(self)
		self.bullets = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		# запуск гри
		while True:
			self._check_event()
			self.ship.update()
			self._update_screen()
			

	def _check_event(self):
		# перебираємо цикли перевіряючи статус гри
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()			
			elif event.type == pygame.KEYDOWN:
				# реакція на нажаття клавіші
				self._check_event_down(event)
			elif event.type == pygame.KEYUP:
				# реакція на відпускання клавіші
				self._check_event_up(event)

	def _check_event_down(self, event):
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_UP:
			self.ship.move_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.move_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_event_up(self, event):
		if event.key == pygame.K_UP:
			self.ship.move_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.move_down = False

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = AttackBullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""оновити позицію куль та позбавитися старих куль"""
		self.bullets.update()
			# позбавитись старих куль
		for bullet in self.bullets.copy():
			if bullet.rect.left > self.ship.screen_rect.right:
				self.bullets.remove(bullet)
		print(len(self.bullets))

	def _create_fleet(self):
		"""намалювати зірку"""
		star = Star(self)
		star_height, star_width = star.rect.size
		available_space_y = self.settings.screen_height - (2 * star_height)
		number_stars_y = available_space_y // (2 * star_height)
		# визначити, яка кількість рядківа зірок поміщається на екрані.
		ship_width = self.ship.rect.width
		available_space_y = (self.settings.screen_width - (star_width * 3) - ship_width)
		number_rows = available_space_y // (2 * star_width)		
		# print(number_rows)
		for row_number in range(number_rows):
			# створити перший стовбець прибульців
			for star_number in range(number_stars_y):
				self._create_star(star_number, row_number)

	def _create_star(self, star_number, row_number):
			star = Star(self)
			star_height, star_width = star.rect.size
			star.y = star_height + 2 * star_height * star_number
			star.rect.y = star.y
			star.rect.x = star.rect.width + star.rect.width + row_number
			self.stars.add(star)

	def _update_screen(self):
		# фон екрану
		self.screen.fill(self.settings.bg_color)
		# відображаємо корабельmi
		self.ship.blitt()
		self._update_bullets()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.stars.draw(self.screen)
		# показуємо останній намальований екран
		pygame.display.flip()

if __name__ == "__main__":
	# створити екземпляр гри та запустити
	at = Attack()
	at.run_game()
