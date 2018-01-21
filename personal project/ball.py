from ball import Ball
import time
from turtle import *
import random
colormode(255)
turtle.tracer(0)
turtle.hideturtle()

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH= turtle.getcamvas() .winfo_width()/2
SCREEN_HEIGHT= turtle.getcamvas() .winfo_height()/2

MY_BALL= Ball(0,0,10,50,100, "blue")

NUMBER_OF_BALLS=5
MIN_BALL_RADIUS=10
MAX_BALL_RADIUS=100
MIN_BALL_DX=-5
MAX_BALL_DX=5
MIN_BALL_DY=-5
MAX_BALL_DY=5

BALLS = []
for i in range (NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH) + int(MAX_BALL_RADIUS),int(SCREEN_WIDTH) - int(MAX_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT) + int(MAX_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAX_BALL_RADIUS))
	dx = random.randint(MIN_BALL_DX,MAX_BALL_DX)
	while dx == 0:
		dx= random.randint(MIN_BALL_DX,MAX_BALL_DX)
	dy = random.randint(MIN_BALL_DX,MAX_BALL_DX)
	while dy == 0:
		dy= random.randint(MIN_BALL_DY,MAX_BALL_DY)
	radius = random.randint(MIN_BALL_RADIUS, MAX_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	ball1 = Ball(self, x,y,dx,dy,radius, color)
	BALLS.append(ball1)

for z in BALLS:
	z.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	DISTANCE_BETWEEN_CORES= int(ball_a.pos())-int(ball_b.pos())
	if DISTANCE_BETWEEN_CORES+10<=ball_a.radius+ball_b.radius:
		return True
	else:
		return False

def check_all_balls():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)==True:
				radius_a=ball_a.radius
				radius_b=ball_b.radius
				x_coordinate = random.randint(int(-SCREEN_WIDTH) + int(MAX_BALL_RADIUS),int(SCREEN_WIDTH) - int(MAX_BALL_RADIUS))
				y_coordinate = random.randint(int(-SCREEN_HEIGHT) + int(MAX_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAX_BALL_RADIUS))
				x_axis_speed = random.randint(MIN_BALL_DX,MAX_BALL_DX)
				while x_axis_speed == 0:
					x_axis_speed = random.randint(MIN_BALL_DX,MAX_BALL_DX)
				y_axis_speed = random.randint(MIN_BALL_DX,MAX_BALL_DX)
				while y_axis_speed == 0:
					y_axis_speed = random.randint(MIN_BALL_DY,MAX_BALL_DY)
				radius = random.randint(MIN_BALL_RADIUS, MAX_BALL_RADIUS)
				r=random.randint(0,255)
				g=random.randint(0,255)
				b=random.randint(0,255)
				color = (r,g,b)
				if ball_a<ball_b:
					ball_a=Ball(x_coordinate,y_coordinate,x_axis_speed,y_axis_speed,radius,color)
					ball_b=+radius_b
				else:
					ball_a=Ball(x_coordinate,y_coordinate,x_axis_speed,y_axis_speed,radius,color)
					ball_b=+radius_b














mainloop()