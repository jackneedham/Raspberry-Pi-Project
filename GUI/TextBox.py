import pygame

class TextBox:
	def __init__(self, x, y, width, text):
		self.x = x
		self.y = y
		self.width = width
		self.text = text
		self.lineheight = 5
		pygame.font.init()
		self.font = pygame.font.SysFont('Sans', 12)
		self.render()

	def render(self):
		lines = []
		line = []
		currentw = 0
		for word in self.text.split(' '):
			w, h = self.font.size(word)
			if word == '\n':
				lines.append(line)
				line = []
				currentw = 0
			elif w + currentw +5 < self.width:
				line.append(word)
				currentw += w
			else:
				lines.append(line)
				line = []
				currentw = w
				line.append(word)
		lines.append(line)

		w, mh = self.font.size('A') # get maximum height for current font
		self.height = 0
		for line in lines:
			self.height += h + self.lineheight
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill((255,255,255))
		currenty = 0
		for line in lines:
			linesurf = pygame.Surface((self.width, h))
			linesurf.fill((255,255,255))
			currentx = 0
			for word in line:
				w, h = self.font.size(word+' ')
				linesurf.blit(self.font.render(word+' ', True, (0,0,0)), (currentx, 0))
				currentx += w
			self.surface.blit(linesurf, (0, currenty))
			currenty += h + self.lineheight

	def draw(self, p):
		p.blit(self.surface, (self.x, self.y))