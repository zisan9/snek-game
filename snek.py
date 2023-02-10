
from OpenGL.GL import *
from OpenGL.GLUT import *
import time
import math
import pymsgbox
import random
import numpy as np





COLUMNS =40
ROWS = 40
FPS = 10
gridX = 0
gridY = 0


def drawline(x1, y1, x2, y2):
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy;
    incNE = 2 * (dy - dx);
    y = y1;
    points = []
    for x in range(x1, x2 + 1):
        # WritePixel(x, y);
        points.append([x, y])
        if (d > 0):
            d = d + incNE;
            y = y + 1;
        else:
            d = d + incE;
    return points


def findzone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = 0;
    if (abs(dx) >= abs(dy)):
        if dx > 0 and dy > 0: zone = 0
        if dx <= 0 and dy > 0: zone = 3
        if dx <= 0 and dy <= 0: zone = 4
        if dx > 0 and dy <= 0: zone = 7
    else:
        if dx > 0 and dy > 0: zone = 1
        if dx <= 0 and dy > 0: zone = 2
        if dx <= 0 and dy <= 0: zone = 5
        if dx > 0 and dy <= 0: zone = 6

    return zone


def convert20(x1, y1, zone):
    if (zone == 0): a, b = x1, y1
    if (zone == 1): a, b = y1, x1
    if (zone == 2): a, b = y1, -x1
    if (zone == 3): a, b = -x1, y1
    if (zone == 4): a, b = -x1, -y1
    if (zone == 5): a, b = -y1, -x1
    if (zone == 6): a, b = -y1, x1
    if (zone == 7): a, b = x1, -y1
    return a, b


def revert(x, y, zone):
    if (zone == 0): a, b = x, y
    if (zone == 1): a, b = y, x
    if (zone == 2): a, b = -y, x
    if (zone == 3): a, b = -x, y
    if (zone == 4): a, b = -x, -y
    if (zone == 5): a, b = -y, -x
    if (zone == 6): a, b = y, -x
    if (zone == 7): a, b = x, -y
    return a, b


def WritePixel(x,y):
    # glPointSize(2.0)
    #glColor3f(0,0,0)
    glBegin(GL_POINTS)
    glVertex2d(x,y)
    glEnd()

def square(xmin,ymin,xmax,ymax):
    line(xmin,ymin,xmax,ymin)
    line(xmin,ymin,xmin,ymax)
    line(xmax,ymax,xmax,ymin)
    line(xmax,ymax,xmin,ymax)
def line(x1, y1, x2, y2):
    zone = findzone(x1, y1, x2, y2)
    x1, y1 = convert20(x1, y1, zone)
    x2, y2 = convert20(x2, y2, zone)
    points = drawline(x1, y1, x2, y2)
    for i in points:
        i[0], i[1] = revert(i[0], i[1], zone)
        WritePixel(i[0], i[1])

def initGrid(x, y):
    global gridX
    gridX = x
    global gridY
    gridY = y

def unit(x, y):
    # glLoadIdentity()
    glLineWidth(1.0)
    if(x==0 or y==0 or x==39 or y==39):
        glColor3f(1.0, 0,0)
    else:
        glColor3f(1.0, 1.0, 0)


    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x + 1, y)
    glVertex2f(x + 1, y)
    glVertex2f(x + 1, y + 1)
    glVertex2f(x + 1, y + 1)
    glVertex2f(x, y + 1)
    glVertex2f(x, y)
    glEnd()

def drawGrid():
    for i in range(gridX):
        for j in range(gridY):
            unit(i, j)
snakeMaxLength =60
snakeLength =5
index =0
posX= [-1]*60
#posX= np.array(60,np.int8)
#posY= np.array(60,np.int8)
posY= [-1]*60
# for i in range(snakeLength):
#     np.insert(posX,i,20)
#     np.insert(posY, i, 20-i)
#     #posX[i] =20
#     #posY[i] =20-i
posX[0]=20
posX[1]=20
posX[2]=20
posX[3]=20
posY[0]=20
posY[1]=19
posY[2]=18
posY[3]=17
gameOver = False
score = 0
def draw_snake():
    global posX
    global posY
    global gameOver
    global food
    global snakeLength
    global score
    i= snakeLength-1
    while(i>0):
        posX[i] = posX[i-1]
        posY[i] = posY[i-1]
        i-=1
    if(sDirection== UP):  #head block
        posY[0]+=1
    elif (sDirection == DOWN):
        posY[0] -= 1
    elif (sDirection == RIGHT):
        posX[0] += 1
    elif (sDirection == LEFT):
        posX[0] -= 1
    for i in range(snakeLength):
        if(i==0):
            glColor3f(0.2,0,0.5)
        else:
            glColor3f(0, 0, 1)
        glRectd(posX[i], posY[i], posX[i] + 1, posY[i] + 1)
        #square(posX[i],posY[i],posX[i]+1,posY[i]+1)


    if(posX[0]==0 or posX[0]==39 or posY[0]==0 or posY[0]==39):
        gameOver= True
    if(posX[0]==foodX and posY[0]==foodY):
        snakeLength+=1
        score+=1
        if(snakeLength>60):
            snakeLength=60
        food=True

food = True
foodX=0
foodY=0
def drawFood():
    global food
    global foodX
    global foodY
    if(food):
        foodX = (random.randint(2,38))
        foodY = (random.randint(2, 38))
        #print(foodX,foodY)
    food= False
    glColor3f(1,0,0)
    #x=foodX
    y=foodY
    for i in range(10):
        x = foodX
        for j in range(10):
            glBegin(GL_LINES)
            glVertex2f(x, y)
            glVertex2f(x + 0.1, y)
            glVertex2f(x + 0.1, y + 0.1)
            glVertex2f(x, y + 0.1)
            glEnd()
            x+=0.1
        y += 0.1


    #glRectd(foodX,foodY,foodX+1,foodY+1)






def init():
    glClearColor(170/255.0, 240/255.0, 120/255.0, 0.0)


"""def init():
    glClearColor(1.0, 0.0, 0.0)
    initGrid(COLUMNS,ROWS)"""
initGrid(COLUMNS, ROWS)


def timer_callback(fps):  # new frame will be dispalyed everytime this function is called
    glutPostRedisplay()
    glutTimerFunc(200, timer_callback, 1)
    return
#controls
UP =1
DOWN =-1
RIGHT =2
LEFT =-2
sDirection =RIGHT
def keyboard_callback(key, x,y):
    global sDirection, UP, DOWN, RIGHT, LEFT
    if(key ==GLUT_KEY_UP):
       if(sDirection!=DOWN):
           sDirection= UP
    elif(key ==GLUT_KEY_DOWN):
        if (sDirection != UP):
            sDirection = DOWN
    elif (key == GLUT_KEY_RIGHT):
        if (sDirection != LEFT):
            sDirection = RIGHT

    elif (key == GLUT_KEY_LEFT):
        if (sDirection != RIGHT):
            sDirection = LEFT






def reshape_callback(w, h):  # need to define the viewport here
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, COLUMNS, 0.0, ROWS, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


#global index


def move():
    #global index
    #index = 0
   """ while (index < 20):
        glRectd(index, 20, index + 2, 22)
       # index +=2"""

    #index = 0



def display_callback():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    """global index
    #index = 0
    #print(index)
    glColor3f(0,0,1)
    glRectd( index,20, index+2,22)
    index+=1
    if (index>40):
        index=0"""
    drawGrid()
    draw_snake()
    drawFood()


    glutSwapBuffers()
    if(gameOver):
        pymsgbox.alert('Your Score : '+str(score), 'Kh3la Sh3sh')
        exit(0)



print(index)
glutInit()
glutInitDisplayMode(
    GLUT_RGBA |  GLUT_DEPTH)  # double buffer window : one is to display and another one is being drawn
glutInitWindowPosition(10, 10)  # initializes the window position
glutInitWindowSize(500, 500)  # window size of display
glutCreateWindow("Snek")
glEnable(GL_DEPTH_TEST)

glutDisplayFunc( display_callback)
glutReshapeFunc(
    reshape_callback)  # called at first when the window is created and when the screen is maximized ore minimized
glutTimerFunc(0,timer_callback,0)
glutSpecialFunc(keyboard_callback)

init()
glutMainLoop()
