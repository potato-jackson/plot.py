import curses

gradient = int(input("Enter the gradient (m)\t:\t"))
yIntercept = int(input("Enter the y intercept (c)\t:\t"))


def main(screen):
	curses.curs_set(0)

	maxY, maxX = screen.getmaxyx()

	originY = maxY // 2
	originX = maxX // 2

	## Graph Axes ##
	
	for midX in range(maxX):
		if midX != originX:
			screen.addstr(originY, midX, "─")
			screen.refresh()
		else:
			screen.addstr(originY, midX, "┼")
			screen.refresh()

	for midY in range(maxY):
		if midY != originY:
			screen.addstr(midY, originX, "│")
			screen.refresh()

	## Draw Plots ##
	
	level = 0

	for plotRight in range(originX, maxX):
		try:
			screen.addstr(originY - yIntercept - level, plotRight, "×")
			screen.refresh()

			level += gradient 
		except:
			pass
	
	level = 0
	
	for plotLeft in range(0, originX):
		try:
			screen.addstr(originY - yIntercept + level, originX - plotLeft, "×")
			screen.refresh()
			level += gradient 
		except:
			pass

	screen.getch()

curses.wrapper(main)
