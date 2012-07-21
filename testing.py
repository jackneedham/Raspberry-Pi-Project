import pygame
import sys
import random
import time

from GUI.Window import Window
from GUI.Button import Button
from GUI.Toolbar import Toolbar
from GUI.FileBrowser import FileBrowser
from GUI.ToolbarButton import ToolbarButton

from ToolWindow import ToolWindow
from MainWindow import MainWindow

# END IMPORTS

screen = pygame.display.set_mode((1280,720))

mainWindow = MainWindow(0,0,screen.get_width(),screen.get_height(), screen)
mainWindow.surface.fill((200,200,200))
windows = []
windows.append(Window(10, 10, 250, 100, screen))
windows.append(ToolWindow(100, 100, 400, 400, screen))
toolbar = Toolbar(screen)
toolbar.items.append(ToolbarButton(0,0,'View', screen, ['Tools']))
toolbar.render()

while True:
	scrolldown = False
	scrollup = False
	screen.fill((200,200,200))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 5:
				scrolldown = True
			else:
				scrolldown = False
			if event.button==4:
				scrollup = True
			else:
				scrollup = False
			mb_up = True
		else:
			mb_up = False

	clicked = toolbar.get_clicked(mb_up)
	for clickeditem in clicked:
		if clickeditem.text == 'Open':
			windows.append(FileBrowser((screen.get_width()/2)- 300, (screen.get_height()/2)-200, 600, 400, screen))
			mb_up = False
		elif clickeditem.text == 'Exit':
			pygame.quit()
		elif clickeditem.text == 'Tools':
			windows.append(ToolWindow(100, 100, 400, 400, screen))
			mb_up = False

	mainWindow.draw()

	# TOOLBAR STUFF
	# Dealing with a list, so it's surrounded by try/except (in the event that no windows are on the screen)
	check_toolbar = False# a little variable used to decide if checking the toolbar for clicks is appropriate
	try:
		if not windows[len(windows)-1].isClicked(): # Only check the toolbar if a window isn't being moved around
			check_toolbar = True
	except:
		check_toolbar = True

	if check_toolbar:
		for item in toolbar.items:
			mx, my = pygame.mouse.get_pos()
			if item.is_clicked(item.x, item.y, mb_up):
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
	# END TOOLBAR STUFF

	# WINDOW MANAGEMENT
	for w in xrange(len(windows)):
		if w == len(windows)-1:
			windows[w].update(mb_up, scrolldown, scrollup)
			if windows[w].exit_btn.is_clicked(windows[w].x+windows[w].exit_btn.x, windows[w].y+windows[w].exit_btn.y, mb_up): # pass the ABSOLUTE (x,y) as the mouse pos is from (0,0)
				windows.remove(windows[w])
				break
		elif windows[w].isClicked() and not windows[w-1].isClicked() and not windows[len(windows)-1].isClicked() and not windows[len(windows)-1].clicked:
			storage_window = windows[w] # just a temp variable 
			windows.remove(windows[w])
			windows.append(storage_window)
		windows[w].draw()
	# END WINDOW MANAGEMENT

	# Draw the toolbar, has to be last so it is on top.
	toolbar.draw()

	time.sleep(0.01)
	pygame.display.update()