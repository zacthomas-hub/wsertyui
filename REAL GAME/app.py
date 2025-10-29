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
Dec2 = 0

#rendering turts
screen.register_shape('bg 1.gif')
BG = turtle.Turtle()
BG.shape('bg 1.gif')
BG.hideturtle

screen.register_shape('left.gif')
left = turtle.Turtle()
left.shape('left.gif')

screen.register_shape('left2.gif')
screen.register_shape('up2.gif')
screen.register_shape('right2.gif')


screen.register_shape('right.gif')
right = turtle.Turtle()
right.shape('right.gif')

screen.register_shape('up.gif')
up = turtle.Turtle()
up.shape('up.gif')

screen.register_shape('up bg.gif')
upBG = turtle.Turtle()
upBG.shape('up bg.gif')

screen.register_shape('UNICORN.gif')
corn = turtle.Turtle()
corn.shape('UNICORN.gif')

# decision scene 1

def leftway(x, y):
    print('rah')
    left.hideturtle()



def upway(x, y):
    print('you decide to press on forward up your original path, and find something quite intresting....')
    up.hideturtle()
    right.hideturtle()
    left.hideturtle()
    BG.hideturtle()
    upBG.showturtle()
    corn.showturtle()
    print('The unicorn of the forest finds you and instantly kills you, you die')
    time.sleep(4.5)
    turtle.bye()

    print('⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠰⢂⠂⢀⠀⠀⠀⠀⠀⠂⡄⠀⠀⠀⠀⡀⣀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢆⠀⠀⣀⣼⢠⢆⢀⠀⠰⠀⠐⡈⡀⡀⡄⠀⠀⠀⠄⠤⢀⠀⠂⠘⡎⠀⠀⠀⠀⠀⠀\n⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⡀⡄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠠⠀⡐⢠⢸⡴⢆⣶⣮⣃⣾⢭⢺⠴⡈⣰⢚⢑⡵⣰⡠⠀⠁⠊⠰⡅⢃⠊⠀⠀⠈⠀⣀⡺⢂⠀⠀\n⠄⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠠⣎⠐⠀⠁⢀⠀⠀⠀⠀⠀⠀⡀⠌⠮⠀⣁⣤⣾⣶⣿⣿⣶⣤⣬⣔⣡⡍⠛⠷⣿⢻⡳⣷⣹⣒⣝⠄⡴⡁⡄⡂⢀⠠⠀⠊⠀⠠⠒⠁⢎⡳⡄⠀\n⠖⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⡰⢥⡂⠀⠀⢄⠃⡀⠀⠄⢀⠐⠅⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣜⣥⡬⣉⠿⠿⢹⣶⣷⡭⠞⡔⡡⠃⠀⠀⠀⠀⠀⠠⠀⠈⠁⠐⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠵⣣⢟⡽⣺⢄⢦⡀⠀⣄⡣⠄⡈⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣣⣡⠏⠓⠿⣪⢞⢂⠄⠈⡀⠄⠊⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠎⡹⠧⡛⠲⣍⢳⡵⣞⣿⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣯⣷⣶⣶⣤⡈⠑⣶⠬⠀⡀⠀⠀⠀⠀⠂⠀⠀⠀\n⠘⡡⠀⠀⢄⣆⠀⠀⠀⠀⠀⠀⠀⠀⣄⢐⣱⣾⡼⣿⢽⢯⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣟⡳⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠓⢺⡎⡢⠀⠊⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⢾⣽⣿⣟⣯⣯⡿⢯⣟⣧⡽⣽⢷⡊⠀⠻⢿⢿⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠈⠀⠀⠀⠀⡀⠀\n⠀⠀⠀⠀⠀⠀⠌⢀⣠⣜⣧⣾⣿⣿⣯⣿⣯⣯⣟⣷⣯⣾⢿⢺⢿⣪⡵⠁⢀⢈⠙⠳⠿⠿⠛⠛⣉⣽⣿⠟⣨⣿⣿⣿⣿⣿⣿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢱⠂\n⠀⠀⠀⠀⠠⠜⢠⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣯⣿⣿⣿⣿⠛⢞⢲⠠⠤⣀⡓⢕⢄⢒⡠⣢⠗⣿⣽⣿⢍⠐⣿⠏⢻⣿⣿⣿⣿⣶⣦⣑⢚⢿⣿⣿⣿⣿⣿⣿⡄⢀⠀⠀⠀⠀⠁\n⠀⠀⠀⢈⣤⣾⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⠻⠿⠿⣯⡑⢦⡙⢥⣳⢽⣗⠱⣮⣿⣿⢫⢼⣾⡿⣶⡈⢿⣿⢿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⠑⣀⡀⠀⢤⡰⢄\n⠀⠀⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡭⡯⠿⣛⣳⢴⡻⣢⣹⡕⠇⣿⣼⣵⡟⠿⠃⢈⢷⣿⠧⢽⡣⠈⠻⣯⣟⣿⣿⣿⣿⣿⣿⣟⣿⣿⡿⠋⠀⠀⠀⠀⠀⠑⠈\n⣀⢞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣿⣽⣏⢾⢎⡓⢧⢾⣽⡧⡇⣿⢫⡘⣢⠁⠄⠄⣲⡿⣣⣛⣿⠆⢀⡈⠁⠛⠻⠾⠷⠟⠋⠘⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⢞⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣳⣯⣟⣮⢧⡈⠂⣧⢣⠳⠿⡿⠻⠀⠀⠈⠩⢡⣺⠧⣮⣿⣓⢋⣉⡢⢀⠄⠀⠀⠀⢀⢒⢉⡔⢄⠀⡀⠀⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢧⣼⣧⣿⣧⡿⡼⣤⣁⠀⢹⢸⣤⠼⠀⠀⠀⠈⠀⢠⣏⣧⢿⣹⣄⣏⣿⣀⡉⠡⡈⢄⠤⢏⡼⡦⡠⣼⣄⣏⣀⠁⠀⠀⠀⠀⠀⠈\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣻⣿⣿⣷⣶⣿⣿⢥⢑⠂⠀⠹⣿⣄⡀⠀⠀⠀⠀⢀⡮⣋⣬⢼⣿⠶⠂⣐⡮⠑⣮⡱⡱⣹⡼⣃⢴⠏⢂⣫⣕⡂⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣾⣟⣾⣷⢿⣭⣿⣳⢌⡀⠄⠙⢿⣷⡄⣄⣠⡄⣾⣍⣕⣦⣴⠒⢊⠐⠊⠑⠷⣢⡹⢱⣿⣿⢏⢲⡽⣻⡵⣷⡂⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣽⣷⢿⣾⣟⣦⣆⢐⢀⠉⠻⠿⠟⠛⠋⠉⠉⠀⠀⠤⣙⢶⡢⡠⣈⢱⣾⣿⡿⢇⣾⣟⢧⡗⣼⡏⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣻⣿⣯⣿⣯⣄⣀⡂⢀⠠⡀⠀⣠⠁⠂⠶⡜⢯⢾⢻⣶⣸⣿⣿⣟⢽⣿⣳⢿⡾⡯⡂⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣽⣿⣿⣽⣷⣭⣟⣒⠖⢼⣛⡇⣷⣻⣛⣺⢲⢳⣳⣸⣿⣿⣿⣯⣚⣾⣭⣿⣾⣫⠃⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣛⣿⣿⣟⡉⠞⣹⢿⣿⣿⣿⣿⣿⣿⣿⣏⣧⣟⣏⣏⠿⣵⡿⡾⡹⣧⡻⣽⣿⣿⣿⣿⣷⣻⣿⣿⣭⣿⣟⠄⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⡿⢿⣷⣠⠡⡘⢼⡟⢏⡿⠚⠛⣿⣿⣿⣿⣷⣿⣿⣿⡿⡷⣽⠷⣈⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣷⣿⣬⠀⠀⠀⠀⡀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣿⠛⠳⢿⣾⣤⠉⠀⠀⢀⣼⣿⢟⣿⣿⣿⣿⣷⣿⣿⣿⡻⢖⣿⣿⣿⢿⣿⣿⣽⣿⣟⣿⡿⣷⠟⠀⠀⠀⠀⠙⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣟⡳⣤⣄⡟⠙⠻⢶⣶⠿⣿⡿⠿⡿⢻⣿⣿⣿⣿⣿⣿⣵⣯⣿⣿⣿⣿⣿⣿⣿⣿⣽⡯⢷⡟⠇⠀⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣙⣓⠶⣴⣤⣀⣹⠀⣴⣵⣾⣿⡿⣟⣿⣿⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣷⠃⠀⠀⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣽⣿⠿⢿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡿⣽⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⢿⡈⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠢⠁⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡳⢇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡾⡑⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    

def rightway(x, y):
    print('rah (right)')
    right.hideturtle()






left.onclick(leftway)
right.onclick(rightway)
up.onclick(upway)


if Begin == 1 :

    upBG.hideturtle()
    corn.hideturtle()
    screen.bgpic("bg 1.gif")
    left.penup()
    left.speed(0)
    left.setpos(-780 , -100)

    right.penup()
    right.speed(0)
    right.setpos(780 , -100)
    up.penup()
    up.speed(0)
    up.setpos(500 , 200)
    print ('before you lie 3 paths, pick a path to carry forward.')
else:
    print ("ahhhhhh")






def move_test(event):
    x = turtle.Screen().cv.canvasx(event.x) / turtle.Screen().xscale
    y = - turtle.Screen().cv.canvasy(event.y) / turtle.Screen().yscale
    





# left clicking
    if -700 > x > -950 and (50 > y > -250):
        left.shape('left2.gif')

# right clicking
    elif 700 < x < 950 and (50 > y > -250): 
        right.shape('right2.gif')

# up clicking
    elif 380 < x < 720  and (120 < y < 380):
        up.shape('up2.gif')
#no clicking
    else:  
        right.shape('right.gif')
        left.shape('left.gif')
        up.shape('up.gif')


# right clicking




        

        

        


turtle.Screen().cv.bind("<Motion>", move_test, None)

#end
turtle.mainloop()
