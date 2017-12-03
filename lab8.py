from turtle import *
import turtle
import random
import math

class Ball(Turtle):
	def __init__ (self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)
	

ball1 =Ball(7,"Blue", 5)
ball2 =Ball(10, "Red", 5)
ball1_x = ball.xcor()
ball1_y = ball.ycor()
ball2_x = ball.xcor()
ball2_y = ball.ycor()

def check_collision(ball1,ball2):
	if(ball.shapesize() +ball2.shapesize() > (((ball2_x-ball_x)^2)+ (ball2_y-ball_y)^2)*0.5:
		print("f")

turtle.mainloop()
