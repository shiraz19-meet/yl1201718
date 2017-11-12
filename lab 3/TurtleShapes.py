import turtle
turtle.speed(400)
turtle.pensize(1)

# for i in range(5):
#     turtle.forward(100)
#     turtle.right(140)
# turtle.mainloop
        
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(50)
##turtle.right(60)
##turtle.forward(50)
##turtle.right(60)
##turtle.forward(50)
##turtle.right(60)
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(50)


#turtle.register_shape('weird',((0,0), (0,50), (50,50)))
#turtle.mainloop
angle = 0
for i in range(361):
	turtle.pendown()
	turtle.forward(120)
	turtle.right(50)
	turtle.forward(40)
	turtle.right(100)
	turtle.forward(20)
	turtle.penup()
	turtle.home()
	turtle.right(angle)
	angle = angle+1
turtle.mainloop()