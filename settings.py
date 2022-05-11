class Settings:
	"""налаштування гри"""
	def __init__(self):
		"""setting for our game"""
		self.screen_width = 600
		self.screen_height = 470
		self.bg_color = (230, 230, 230)
		self.ship_speed = 0.5
		self.bullet_speed = 0.1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 5