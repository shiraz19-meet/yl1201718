from turtle import *
colormode(255)
class Square(Turtle):
	def __init__(self,shapesize):
		Turtle.__init__(self)
		self.shapesize(shapesize)
		self.shape("square")
	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)
square1= Square(10)

mainloop()