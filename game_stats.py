class GameStats:
	"""tracking game statistics"""
	def __init__(self, ai_game):
		"""game initialization"""
		self.settings = ai_game.settings
		self.reset_stats()
		# Start game in an active state.
		self.game_active = False

	def reset_stats(self):
		"""statistics initialization, what can change during game"""
		self.ships_left = self.settings.ship_limit