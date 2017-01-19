
import curses

pos = 0
while True:
	gamePlan = resetGamePlan()
	gamePlan[pos] = [0,200,0]
	setGamePlan()
	pos = getNewPosition(pos)
