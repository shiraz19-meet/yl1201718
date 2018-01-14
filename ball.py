from turtle import *
colormode(255)
class Ball(Turtle):
	def __init__ (self, x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.penup()
		self.setposition(x,y)
		self.dx = dx
		self.dy = dy
		self.radius = radius
		turtle.shape('circle')
		self.shapesize (radius/10)

		r = random.randint (0,255)
		g = random.randint (0,255)
		b = random.randint (0,255)
		self.color(r,g,b)

		def move(self):
			currentx=self.xcor()
			currenty=self.ycor()
			new_x= currentx+self.dx
			new_y= currenty+self.dy
			right_side_ball= new_x+radius
			left_side_ball= new_x-radius
			self.goto(currentx+self.dx, currenty+self.dy)
