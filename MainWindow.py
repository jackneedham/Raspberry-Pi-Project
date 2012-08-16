import pygame
from GUI.Window import Window
from GUI.Button import Button
from GUI.Toolbar import Toolbar
from GUI.FileBrowser import FileBrowser
from GUI.ToolbarButton import ToolbarButton # possibly put this in GUI.Toolbar
from GUI.Ask import Ask
from ToolWindow import ToolWindow
from ColorWheelWindow import ColorWheelWindow
from CanvasWindow import CanvasWindow

class MainWindow(Window):
	def __init__(self,x,y,w,h,p):
		Window.__init__(self,x,y,w,h,p)
		self.windows = []
		
		self.windows.append(ColorWheelWindow(100,300,280,260,self.parent))
		self.current_color = (255,100,0)
	
		# blank canvas window
		newdoc = pygame.Surface((640,480))
		newdoc.fill((255,255,255))
		self.windows.append(CanvasWindow(300,300,self.parent,newdoc))
		
		# create toolbar
		self.toolbar = Toolbar(self.parent)
		self.toolbar.items.append(ToolbarButton(0,0,'File', self.parent, ['New', 'Open']))
		self.toolbar.items.append(ToolbarButton(0,0,'View', self.parent, ['Tools', 'Colours', 'Answer this']))
		self.toolbar.render() # item appended, needs to be re-rendered

		self.draw()
		
	def draw(self):
		self.bar.draw()
		Window.draw(self)
			

	def update(self, mb_up, scrolldown, scrollup, keypressed):
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

		
		try:
			# Update the last most element in the windows list, which is the one
			# currently in focus.
			self.windows[-1].update(mb_up, scrolldown, scrollup, keypressed)
			
			for w in xrange(len(self.windows)):
				if self.windows[w].title == 'File Browser':
					if self.windows[w].complete:
						image_file = pygame.image.load(self.windows[w].file_system.getsyspath('/')+'/'+self.windows[w].selected)
						self.windows.append(CanvasWindow(300,300,self.parent,image_file, self.windows[w].selected)) # testing window appended
						self.windows.remove(self.windows[w])
				elif self.windows[w].title[:6] == 'Canvas':
					self.windows[w].draw_color = self.current_color
				elif self.windows[w].title == 'Color Picker':
					self.current_color = self.windows[w].get_color()
				self.windows[w].draw()
				if self.windows[w].exit_btn.is_clicked(self.windows[w].x+self.windows[w].exit_btn.x,
				self.windows[w].y+self.windows[w].exit_btn.y, mb_up):
					self.windows.remove(self.windows[w])
					break
				if self.windows[w].is_clicked() and w != len(self.windows)-1:
					change = True
					for window in range(len(self.windows)-1,0,-1):
						if self.windows[window].clicked:
							change = False
						if window > w and self.windows[window].is_clicked():
							change=False
					if change:
						store = self.windows[w]
						self.windows.remove(self.windows[w])
						self.windows.append(store)
		except IndexError:
			pass # It's cool, there are just no windows on the screen.
			
		
		self.toolbar.draw()
		
	def toolbar_events(self, mouseclick):
		toolbar_clicked = self.toolbar.get_clicked(mouseclick) # returns a list of all clicked elements
		for clicked in toolbar_clicked:
			if clicked.text == 'Exit': # identification done using text, seems effiecient enough
				pygame.quit()
			elif clicked.text == 'Tools':
				self.windows.append(ToolWindow(100, 100, 400, 400, self.parent))
				mouseclick = False
			elif clicked.text == 'Colours':
				self.windows.append(ColorWheelWindow(100,300,280,260,self.parent))
			elif clicked.text == 'New':		
				newdoc =pygame.Surface((640,480))
				newdoc.fill((255,255,255))
				self.windows.append(CanvasWindow(300,300,self.parent,newdoc))
			elif clicked.text == 'Open':
				self.windows.append(FileBrowser(0,0,600,400,self.parent))
			elif clicked.text == 'Answer this':
				self.windows.append(Ask("Favourite Color?", self.parent, self.answergoeshere))
		

