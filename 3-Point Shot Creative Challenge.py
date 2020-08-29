############################################
##### 3-Point Shot Creative Challenge ######
##### By Sarah Ahmed #######################
##### March 16th, 2020 #####################
############################################
from tkinter import*
from random import*
from time import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=800, background="sky blue" )
screen.pack()

##################
### BACKGROUND ###
##################
#grassy field
grass = screen.create_rectangle(0,670, 800,800, fill = "green", outline = "black")

#trees
for n in range(4):
    tree1 = screen.create_rectangle(650-200*n,400, 700-200*n,685, fill = "saddle brown", outline = "black")
    leaf1 = screen.create_oval(600-200*n,300, 750-200*n,450, fill = "chartreuse4")

#sun
xsun = randint(500,700)
xxsun = xsun + 100
ysun = 10
yysun = ysun + 100
screen.create_oval(xsun,ysun, xxsun,yysun, fill = "yellow")

#ground
ground = screen.create_rectangle(0, 700, 800, 800, fill = "gray", outline = "black")
pointline = screen.create_line(0,800, 300,790, 400,780, 500,760, 540,705, 540,700, fill =
                                "white", width = 15, smooth = True)
crease = screen.create_line(0,750, 300,750, 300,700, width = 15, fill = "white")
midcircle = screen.create_oval(650,710, 1000,750, outline = "white", width = 15)
midline = screen.create_line(800,700, 800,800, fill = "white", width = 15)

#basketball stand
backboard = screen.create_polygon(100,300, 100,400, 150,385, 150,200, fill = "white", outline = "black")

pole1 = screen.create_line(100, 290, 100, 400, width = 15, fill = "black")
pole2 = screen.create_line(100, 290, 30, 425, width = 15, fill = "black")
pole3 = screen.create_line(40, 400, 108, 400, width = 15, fill = "black")
connectingpiece = screen.create_polygon(60,400, 20, 400, 20, 450, fill = "black")
standingpole = screen.create_line(20,375, 20,700, width = 15, fill = "black")
bottompiece = screen.create_polygon(60,700, 50,650, 20,650, 20,700, fill = "black")

# basketball hoop
rimEdge = screen.create_polygon(150,375, 160,350, 160,345, 150,345, fill = "orange", outline = "black")
rim = screen.create_polygon(160,350, 230,350, 230,345, 160,345, smooth = True, fill = "orange", outline = "black")
for n in range(0,30):
    x1net = 2*n + 160
    y1net = 351
    x2net = 2*n + 172
    y2net = 355
    net1 = screen.create_rectangle(x1net,y1net, x2net,y2net, outline= "white")
for n in range(0,30):
    x1net = 2*n + 165
    y1net = 356
    x2net = 2*n + 167
    y2net = 360
    net2 = screen.create_rectangle(x1net,y1net, x2net,y2net, outline= "white")
for n in range(0,25):
    x1net = 2*n + 170
    y1net = 361
    x2net = 2*n + 172
    y2net = 365
    net3 = screen.create_rectangle(x1net,y1net, x2net,y2net, outline= "white")
for n in range(0,20):
    x1net = 2*n + 175
    y1net = 366
    x2net = 2*n + 177
    y2net = 370
    net4 = screen.create_rectangle(x1net,y1net, x2net,y2net, outline= "white")
for n in range(0,15):
    x1net = 2*n + 180
    y1net = 371
    x2net = 2*n + 182
    y2net = 375
    net5 = screen.create_rectangle(x1net,y1net, x2net,y2net, outline= "white")

#################
### ANIMATION ###
#################
#person jumping up with ball in hand
yball = 320
for n in range(30):
    head = screen.create_polygon(700,410- 2*n, 680,430- 2*n, 680,450- 2*n, 720,480- 2*n, 725,470- 2*n, 740,450- 2*n,
                                 730,430- 2*n, fill = "LightSalmon4", smooth = True, outline = "black", width = 5)

    jersey = screen.create_polygon(735,540- 2*n, 705,560- 2*n, 690,540- 2*n, 685,530- 2*n, 690,480- 2*n, 685,450- 2*n, 735,480- 2*n, 740,485-2*n,
                                fill = "firebrick3", smooth = True, outline = "black")
    arm = screen.create_polygon(720,485- 2*n, 715,480- 2*n, 670,450- 2*n, 670,430-2*n, 680,400- 2*n, 700,330- 2*n, 690,430- 2*n,
                                fill = "LightSalmon4", smooth = True, outline = "black")
    eye = screen.create_oval(705,430- 2*n, 710,435- 2*n,
                                 fill = "black")
    

    ear = screen.create_line(725,445-2*n, 725,435- 2*n, 735,445- 2*n, 725,455 - 2*n, 725,445 - 2*n, smooth = True)

    pants = screen.create_polygon(740,540- 2*n, 685,540- 2*n, 685,630- 2*n, 740,630- 2*n, fill = "black", smooth = True)

    leg = screen.create_oval(700,620- 2*n, 722,680- 2*n, fill = "LightSalmon4", outline = "black")
    leg2 = screen.create_oval(710,620- 2*n, 732,680- 2*n, fill = "LightSalmon4", outline = "black")

    shoes = screen.create_oval(680,675- 2*n, 725,700- 2*n, fill = "saddle brown")
    shoes2 = screen.create_oval(690,675- 2*n, 735,700- 2*n, fill = "saddle brown")

    ball = screen.create_oval(660, yball - 2*n, 700, 360- 2*n, fill = "orange")                             

    screen.update()
    sleep(0.03)
    screen.delete(ball, head, jersey, arm, eye, pants, leg, leg2, shoes, shoes2, ear)

#person begins to come back down due to gravity (0.01)

for f in range(25):
    head = screen.create_polygon(700,410- 2*n +0.1*f**2, 680,430- 2*n+0.1*f**2, 680,450- 2*n+0.1*f**2, 720,480- 2*n+0.1*f**2, 725,470- 2*n+0.1*f**2, 740,450- 2*n+0.1*f**2,
                                 730,430- 2*n+0.1*f**2, fill = "LightSalmon4", smooth = True, outline = "black", width = 5)

    jersey = screen.create_polygon(735,540- 2*n+0.1*f**2, 705,560- 2*n+0.1*f**2, 690,540- 2*n+0.1*f**2, 685,530- 2*n+0.1*f**2, 690,480- 2*n+0.1*f**2, 685,450- 2*n+0.1*f**2, 735,480- 2*n+0.1*f**2, 740,485-2*n+0.1*f**2,
                                fill = "firebrick3", smooth = True, outline = "black")
    arm = screen.create_polygon(720,485- 2*n+0.1*f**2, 715,480- 2*n+0.1*f**2, 670,450- 2*n+0.1*f**2, 670,430-2*n+0.1*f**2, 680,400- 2*n+0.1*f**2, 700,330- 2*n+0.1*f**2, 690,430- 2*n+0.1*f**2,
                                fill = "LightSalmon4", smooth = True, outline = "black")
    eye = screen.create_oval(705,430- 2*n+0.1*f**2, 710,435- 2*n+0.1*f**2,
                                 fill = "black")
    

    ear = screen.create_line(725,445-2*n+0.1*f**2, 725,435- 2*n+0.1*f**2, 735,445- 2*n+0.1*f**2, 725,455 - 2*n+0.1*f**2, 725,445 - 2*n+0.1*f**2, smooth = True)

    pants = screen.create_polygon(740,540- 2*n+0.1*f**2, 685,540- 2*n+0.1*f**2, 685,630- 2*n+0.1*f**2, 740,630- 2*n+0.1*f**2, fill = "black", smooth = True)

    leg = screen.create_oval(700,620- 2*n+0.1*f**2, 722,680- 2*n+0.1*f**2, fill = "LightSalmon4", outline = "black")
    leg2 = screen.create_oval(710,620- 2*n+0.1*f**2, 732,680- 2*n+0.1*f**2, fill = "LightSalmon4", outline = "black")

    shoes = screen.create_oval(680,675- 2*n+0.1*f**2, 725,700- 2*n+0.1*f**2, fill = "saddle brown")
    shoes2 = screen.create_oval(690,675- 2*n+0.1*f**2, 735,700- 2*n+0.1*f**2, fill = "saddle brown")

#ball releases from persons hand in parabolic shape as person is going down
    xball = -10*f + 650
    yball = 0.1*f**2 - 5.8*f + 280
    ball = screen.create_oval(xball,yball, xball + 40, yball +40, fill = "orange")

    screen.update()
    sleep(0.03)
    screen.delete(head, jersey, arm, eye, pants, leg, leg2, shoes, shoes2, ear, ball)

#person reaches the ground, redraws person outside of for loop so person is not deleted
head = screen.create_polygon(700,410- 2*n +0.1*f**2, 680,430- 2*n+0.1*f**2, 680,450- 2*n+0.1*f**2, 720,480- 2*n+0.1*f**2, 725,470- 2*n+0.1*f**2, 740,450- 2*n+0.1*f**2,
                             730,430- 2*n+0.1*f**2, fill = "LightSalmon4", smooth = True, outline = "black", width = 5)

jersey = screen.create_polygon(735,540- 2*n+0.1*f**2, 705,560- 2*n+0.1*f**2, 690,540- 2*n+0.1*f**2, 685,530- 2*n+0.1*f**2, 690,480- 2*n+0.1*f**2, 685,450- 2*n+0.1*f**2, 735,480- 2*n+0.1*f**2, 740,485-2*n+0.1*f**2,
                            fill = "firebrick3", smooth = True, outline = "black")
arm = screen.create_polygon(720,485- 2*n+0.1*f**2, 715,480- 2*n+0.1*f**2, 670,450- 2*n+0.1*f**2, 670,430-2*n+0.1*f**2, 680,400- 2*n+0.1*f**2, 700,330- 2*n+0.1*f**2, 690,430- 2*n+0.1*f**2,
                            fill = "LightSalmon4", smooth = True, outline = "black")
eye = screen.create_oval(705,430- 2*n+0.1*f**2, 710,435- 2*n+0.1*f**2,
                             fill = "black")

ear = screen.create_line(725,445-2*n+0.1*f**2, 725,435- 2*n+0.1*f**2, 735,445- 2*n+0.1*f**2, 725,455 - 2*n+0.1*f**2, 725,445 - 2*n+0.1*f**2, smooth = True)

pants = screen.create_polygon(740,540- 2*n+0.1*f**2, 685,540- 2*n+0.1*f**2, 685,630- 2*n+0.1*f**2, 740,630- 2*n+0.1*f**2, fill = "black", smooth = True)

leg = screen.create_oval(700,620- 2*n+0.1*f**2, 722,680- 2*n+0.1*f**2, fill = "LightSalmon4", outline = "black")
leg2 = screen.create_oval(710,620- 2*n+0.1*f**2, 732,680- 2*n+0.1*f**2, fill = "LightSalmon4", outline = "black")

shoes = screen.create_oval(680,675- 2*n+0.1*f**2, 725,700- 2*n+0.1*f**2, fill = "saddle brown")
shoes2 = screen.create_oval(690,675- 2*n+0.1*f**2, 735,700- 2*n+0.1*f**2, fill = "saddle brown")
    
#basketball continues path from last frame
for f in range(25, 82):  
    xball = -10*f + 650
    yball = 0.1*f**2 - 5.8*f + 280

    #if xball is greater than 140(where the backboard is), continue in normal parabolic path
    if xball > 140:
        ball = screen.create_oval(xball,yball, xball + 40, yball +40, fill = "orange")

        screen.update()
        sleep(0.03)
        screen.delete(ball)

    #else, hits backboard before going into net to make it more **realistic**
    else:
        xball = 0.003*f**2 + 150
        yball = 0.1*f**2 -6*f + yball

        #as ball is passing through the net, delete and redraw the rim to make it more realistic
        if 160<= xball <= 230:
            screen.delete(rim)
            ball = screen.create_oval(xball,yball, xball + 40, yball +40, fill = "orange")
            rim = screen.create_polygon(160,350, 230,350, 230,345, 160,345, smooth = True, fill = "orange", outline = "black")
            screen.update()
            sleep(0.03)
            screen.delete(ball)
        
#basketball post-animation (bounces once, then stays on ground)
bounce = 5
for m in range(51):
    xball = xball
    yball = 0.1*m**2 - bounce*m + 660
    ball = screen.create_oval(xball,yball, xball + 40, yball +40, fill = "orange")
    screen.update()
    sleep(0.03)
    screen.delete(ball)

screen.create_oval(xball,yball, xball + 40, yball +40, fill = "orange")

#celebratory text
celebration = screen.create_text(400,200, text = "Goal! Way to go, future NBA star!", font = 30)

