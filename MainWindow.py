import pygame
from GUI.Window import Window
from GUI.Button import Button
from GUI.Toolbar import Toolbar
from GUI.FileBrowser import FileBrowser
from GUI.ToolbarButton import ToolbarButton # possibly put this in GUI.Toolbar
from ToolWindow import ToolWindow
from ColorWheelWindow import ColorWheelWindow
from CanvasWindow import CanvasWindow

class MainWindow(Window):
	def __init__(self,x,y,w,h,p):
		Window.__init__(self,x,y,w,h,p)
		self.windows = []
		self.windows.append(Window(10,10,250,250,self.parent)) # testing window appended
		self.windows.append(ColorWheelWindow(100,300,280,260,self.parent)) # testing window appended

		# create toolbar
		self.toolbar = Toolbar(self.parent)
		self.toolbar.items.append(ToolbarButton(0,0,'View', self.parent, ['Tools']))
		self.toolbar.render() # item appended, needs to be re-rendered
		self.draw()

	def draw(self):
		self.bar.draw()
		Window.draw(self)
			

	def update(self, mb_up, scrolldown, scrollup):
		self.surface.fill((200,200,200))
		
		# handle toolbar events
		self.toolbar_events(mb_up)

		# toolbar rendering/drawing
		# Dealing with a list, so it's surrounded by try/except (in the event that no windows are on the screen)
		check_toolbar  = False
		try:
			if not self.windows[len(self.windows)-1].isClicked():
				check_toolbar = True
		except:
			check_toolbar = True

		if check_toolbar:
			for item in self.toolbar.items:
				mx, my = pygame.mouse.get_pos()
				if item.is_clicked(item.x, item.y, pygame.mouse.get_pressed()[0]):
					item.show_menu = True
					item.render()
					item.menu.render()
				elif item.show_menu:
					if mx > item.menu.x and mx<item.menu.x+item.menu.surface.get_width() and my > 0 and my < item.menu.y+item.menu.surface.get_height():
						item.show_menu = True
					else:
						item.show_menu = False
				elif pygame.mouse.get_pressed()[0]:
					item.show_menu = False
					item.render()

		# WINDOW MANAGEMENT #
		for w in xrange(len(self.windows)):
			if w == len(self.windows)-1:
				self.windows[w].update(mb_up, scrolldown, scrollup)
				# pass the absolute position
				if self.windows[w].exit_btn.is_clicked(self.windows[w].x+self.windows[w].exit_btn.x, self.windows[w].y+self.windows[w].exit_btn.y, mb_up):
					self.windows.remove(self.windows[w])
					break
			elif self.windows[w].isClicked() and not self.windows[w-1].isClicked() and not self.windows[len(self.windows)-1].isClicked() and not self.windows[len(self.windows)-1].clicked:
				storage = self.windows[w]
				self.windows.remove(self.windows[w])
				self.windows.append(storage)
			self.windows[w].draw()
			if self.windows[w].title == 'File Browser':
				if self.windows[w].complete:
					image_file = pygame.image.load(self.windows[w].file_system.getsyspath('/')+'/'+self.windows[w].selected)
					self.windows.append(CanvasWindow(300,300,self.parent,image_file)) # testing window appended
					self.windows.remove(self.windows[w])
		self.toolbar.draw()

	def toolbar_events(self, mouseclick):
		toolbar_clicked = self.toolbar.get_clicked(mouseclick) # returns a list of all clicked elements
		for clicked in toolbar_clicked:
			if clicked.text == 'Exit': # identification done using text, seems effiecient enough
				pygame.quit()
			elif clicked.text == 'Tools':
				self.windows.append(ToolWindow(100, 100, 400, 400, self.parent))
				mouseclick = False
			elif clicked.text == 'Open':
				self.windows.append(FileBrowser(0,0,600,400,self.parent))

	def testtask(self):
		self.surface.fill((200,200,200))
