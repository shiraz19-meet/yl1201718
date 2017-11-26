from turtle import *
import random
colormode(255)


0
class rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		register_shape("rectangle",((0,0),(0,height),(width,height),(width,0),(0,0)))
		self.setheading(90)
		self.shape("rectangle")
# register_shape("Hexagon",((0,0)(30,-20)(0,-70)(-30,-50)))
# class Hexagon(Turtle):
# 	def __init__(self,shapesize):
# 		Turtle.__init__(self)
# 		self.shapesize(shapesize)
# 		self.shape("hexagon")
rect1 = Rectangle(50,100)
class Square(Turtle):
	def __init__(self,size):
		rectangle.__init__(self,size,size)
		self.
		self.shape("square")
	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)
square1= Square(10)
square1.random_color()
mainloop()