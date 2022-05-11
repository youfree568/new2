import sys
import pygame

class Check:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((600, 400))	
		# фон - self.bg_color = (255, 255, 0)
		pygame.display.set_caption("'My check'")
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					print('even.key')

			# задати фон
			self.screen.fill((255, 255, 255))
			# показати останній намальований екран 
			pygame.display.flip()
if __name__ == '__main__':
	Check().run()