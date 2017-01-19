
class Moving(Object):

	def getNewPosition(pos):
		screen = curses.initscr()
		try:
			curses.noecho()
			curses.curs_set(0)
			screen.keypad(1)
			event = screen.getch()
		finally:
			curses.endwin()
		
		if event == curses.KEY_LEFT:
			pos = pos - 1
			if(pos < 0):
				pos = 0
		elif event == curses.KEY_RIGHT:
			pos = pos + 1
			if(pos > (maxX * maxY) - 1):
				pos = maxX * maxY - 1
		
		return pos
