from meet import *
ball1={"radius":10,"y":-7,"x":-5,"dy":1,"dx":1}
ball2={"radius":15,"y":6,"x":9,"dy":-1,"dx":-1}
ball3={"radius":5,"y":0,"x":0,"dy":1,"dx":1}
ball4={"radius":20,"y":-6,"x":-9,"dy":-1,"dx":-1}
cells=[]

circle1=create_cell(ball1)
cells.append(circle1)
circle2=create_cell(ball2)
cells.append(circle2)
circle3=create_cell(ball3)
cells.append(circle3)
circle4=create_cell(ball4)
cells.append(circle4)

def borders(cells):
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if (cell.xcor()>width):
			cell.set_dx(-cell.get_dx())
		if (cell.ycor()>height):
			cell.set_dy(-cell.get_dy())


def borders(cells):
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if (cell.xcor()>width):
			cell.set_dx(cell.get_dx())
		if (cell.ycor()>height):
			cell.set_dy(cell.get_dy())
while(True):
	move_cells(cells)
	borders(cells)

