import pygame
from fs.osfs import OSFS
from Window import Window
from Button import Button
from ScrollPane import ScrollPane
from Input import Input

class FileBrowser(Window):
	def __init__(self, x, y, w, h, parent):
		self.buttons = []
		self.file_system = OSFS('/')
		self.width = w
		self.height = h
		self.selected = ''
		self.surface = pygame.Surface((self.width, self.height))
		self.scroll_pane = ScrollPane(10,30,self.width-20, self.height-70, 10)
		Window.__init__(self, x, y, w, h, parent, 'File Browser')
		self.okaybtn = Button(10,self.height-30, 'Okay', self.surface, (50,50,50))
		self.okaybtn.x = self.width-self.okaybtn.surface.get_width()-10
		self.okaybtn.render()
		self.complete = False
		self.textinput = Input(10, self.height-28, self.width - 30 - self.okaybtn.width)
		self.render()

	def render(self):
		self.buttons = []
		self.buttons.append(Button(0, 10, '...', self.surface, (255,255,255), vpad=0))
		currenty = 30
		for directory in self.file_system.listdir():
			if directory[0] != '.':
				self.buttons.append(Button(10,currenty,directory, self.surface, (255,255,255), hpad =0, vpad=0))
				currenty += 20
		self.scroll_pane.content_height = currenty+10
		if self.scroll_pane.content_height < self.scroll_pane.height:
			print 'changing'
			self.scroll_pane.content_height = self.scroll_pane.height + 10
		self.scroll_pane.render()

		Window.render(self)

	def update(self, mouseclick, scrolldown, scrollup, keypressed):
		self.scroll_pane.scrolldown = scrolldown
		self.scroll_pane.scrollup = scrollup
		self.scroll_pane.update(self.x+self.scroll_pane.x, self.y+self.scroll_pane.y)
		self.textinput.update(self.x+self.textinput.x, self.y+self.textinput.y, mouseclick, keypressed)
		if scrolldown or scrollup:
			mouseclick = False
		mx, my = pygame.mouse.get_pos()
		if mx>self.x+self.scroll_pane.x and mx < self.x+self.scroll_pane.x + self.scroll_pane.width and my > self.y+self.scroll_pane.y and my < self.y+self.scroll_pane.y+self.scroll_pane.height:
			for button in self.buttons:
				if button.is_clicked(self.x+self.scroll_pane.x+button.x, self.y+self.scroll_pane.y+self.scroll_pane.content_y+button.y, mouseclick):
					if button.text == '...':
						path = self.file_system.getsyspath('/').split('/')
						for item in path:
							if item == '':
								path.remove(item)
						path = path[:-1]
						path = '/'.join(path)
						try:
							if path[len(path)-1] == '/':
								path = path[:-1]
						except:
							path = ''
						path = '/'+path
						print path
						self.file_system = OSFS(path)

						self.render()
					elif self.file_system.isdir(button.text):
						self.file_system = self.file_system.makeopendir(button.text)
						print self.file_system.getsyspath('/')
						self.render()
					else:
						self.selected = button.text
						self.textinput.text = button.text
						self.textinput.render()
				if button.text == self.selected and button.colour == (255,255,255):
					button.colour = (200,220,255)
					button.surface.fill(button.colour)
					button.render()
				elif button.text != self.selected and button.colour == (200,220,255):
					button.colour == (255,255,255)
					button.surface.fill(button.colour)
					button.render()

		if self.okaybtn.is_clicked(self.x+self.okaybtn.x, self.y+self.okaybtn.y, mouseclick):
			self.complete = True

		self.selected = self.textinput.text

		Window.update(self,mouseclick, scrolldown, scrollup)

	def draw(self):
		for button in self.buttons:
			button.draw(self.scroll_pane.content_surface)
		self.okaybtn.draw(self.surface)
		self.textinput.draw(self.surface)
		self.scroll_pane.draw(self.surface)
		
		Window.draw(self)		

