import pygame

class SettingsAttack:
	"""налаштування """
	def __init__(self):
		self.screen_width = 640
		self.screen_height =  400
		self.bg_color = (200, 200, 200)
		self.speed = 0.2
		# налаштування кулі
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)
		self.bullet_speed = 0.2
		self.bullet_allowed = 5