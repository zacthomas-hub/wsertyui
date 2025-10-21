#WE NOT GONNA DO APPLE CATCH
#starting settings and variales
import turtle
import random
import time
import os

screen = turtle.Screen()
screen.setup(width=2000, height=800, startx=0, starty=-242)

turtle.speed(0)
turtle.delay(0)
Begin = 1

#rendering turts
screen.register_shape('bg 1.gif')
BG = turtle.Turtle()
BG.shape('bg 1.gif')
BG.hideturtle

screen.register_shape('left.gif')
left = turtle.Turtle()
left.shape('left.gif')

screen.register_shape('left2.gif')
left2 = turtle.Turtle()
left2.shape('left2.gif')

screen.register_shape('right.gif')
right = turtle.Turtle()
right.shape('right.gif')

screen.register_shape('up.gif')
up = turtle.Turtle()
up.shape('up.gif')

# decision scene 1

def leftway(x, y):
    print('rah')


if Begin == 1 :
    global Leftway
    
    screen.bgpic("bg 1.gif")
    left.penup()
    left.speed(0)
    left.setpos(-780 , -100)
    left2.penup()
    left2.speed(0)
    left2.setpos(-780 , -100)
    right.penup()
    right.speed(0)
    right.setpos(780 , -100)
    up.penup()
    up.speed(0)
    up.setpos(500 , 200)
    print ('before you lie 3 paths, pick a path to carry forward.')

    left2.onclick(leftway)
  

else:
    print ("ahhhhhh")




def move_test(event):
    x = turtle.Screen().cv.canvasx(event.x) / turtle.Screen().xscale
    y = - turtle.Screen().cv.canvasy(event.y) / turtle.Screen().yscale

    if -700 > x > -950 and (50 > y > -250):
        left.hideturtle()
        left2.showturtle()
    else:
        left.showturtle()
        left2.hideturtle()
        

        


turtle.Screen().cv.bind("<Motion>", move_test, None)

#end
turtle.mainloop()
