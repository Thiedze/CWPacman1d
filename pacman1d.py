import unicornhat
import time
import math
import numpy as np
import curses

maxX = 8
maxY = 4
gamePlan = list()

def getPixel(pos):
	x = int(math.floor(pos / maxX))
	if(x%2 == 0):
		y = pos % (maxX * 2)
	else:
		y = abs((maxX -1) - (pos % maxX))
	return(x,y)

def resetGamePlan():
	gamePlan = list()
	for planPos in range(maxX * maxY):
		gamePlan.append([255,255,255])
	return gamePlan

def setGamePlan():
	for planPos in range(len(gamePlan)):
		x,y = getPixel(planPos)
		unicornhat.set_pixel(x, y, gamePlan[planPos][0], gamePlan[planPos][1], gamePlan[planPos][2])
	unicornhat.show()		

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

pos = 0
while True:
	gamePlan = resetGamePlan()
	gamePlan[pos] = [0,200,0]
	setGamePlan()
	pos = getNewPosition(pos)
	

raw_input()
