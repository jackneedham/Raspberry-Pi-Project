import pygame
import sys

# custom GUI library imports
from MainWindow import MainWindow

class PiPaint:
	def __init__(self):
		self.width = 1280
		self.height = 720
		self.screen = pygame.display.set_mode((self.width,self.height))
		# background window is not included in self.windows so it can be styled individually
		# possibly add type attribute to Window.py to solve this
		self.background_window = MainWindow(0, 0, self.width, self.height, self.screen)
		self.background_window.surface.fill((200,200,200))

		self.mainloop()

	def mainloop(self):	
		shift = False
		while True:
			# scroll variables, easily replaced with just one var. Do this.
			scrolldown = False
			scrollup = False
			mb_up = False # regular mb var
			keypressed = ''

			# event handling
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					# regular mouse is clicked var
					mb_up = True
					# scrolling vars
					if event.button == 5:
						scrolldown = True
					if event.button == 4:
						scrollup = True
				if event.type == pygame.KEYDOWN:
					print event.key
					try:
						if event.key == 303:
							shift = True
						elif event.key == 8:
							keypressed = 'back'
						elif event.key == 276:
							keypressed = 'left'
						elif event.key == 275:
							keypressed = 'right'
						else:
							key = event.key
							if shift and event.key != 32:
								key -= 32
							keypressed = chr(key)
					except:
						pass # pokemon, catch em all
						# unfortunately this is neccesary as I can not
						# account for every 'hot key' that a user might press
						# well I could, but it would take a zillion lines of
						# code
						
				if event.type == pygame.KEYUP:
					if event.key == 303:
						shift = False

			# DRAWING/RENDERING
			self.background_window.draw()
			self.background_window.update(mb_up, scrolldown, scrollup, keypressed)

			pygame.display.update()



if __name__ == '__main__':
	PiPaint()
