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
		self.alien_speed = 1
		self.fleet_drop_speed = 15
		# fleet direction 1 mins turn right -1 = turn left
		self.fleet_direction = 0.3