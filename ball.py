from turtle import *
colormode(255)
screen_size= 640,480
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
		self/color= color

		def move(self):
			currentx=self.xcor()
			currenty=self.ycor()
			new_x= currentx+self.dx
			new_y= currenty+self.dy
			right_side_ball= new_x+radius
			left_side_ball= new_x-radius
			bottom_side_ball = new_y - radius
			top_side_ball = new_y + radius
			self.goto(new_x, new_y)

			if right_side_ball >=screen_width:
				self.dx= -self.dx
			if left_side_ball <= -screen_width:
				self.dx= -self.dx
			if top_side_ball >=screen_height:
				self.dx= -self.dx
			if bottom_side_ball <= -screen_height:
				self.dx= -self.dx