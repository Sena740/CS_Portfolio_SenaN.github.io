#Recursion using graphics.py
#2024/10/21 By Sena Nishimura
from graphics import *
import random
#Draws an circle on different position every time the function get's called
def draw_circle(win, center, radius, range, x, y): 
    if range == 0:
        return
    #Sets random colors for the circles
    random_color = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    circle.setOutline(random_color)
    circle.draw(win)
    circle = Circle(center, radius)

    center = Point(x,y)
    
    draw_circle(win, center, radius * 0.8, range - 1, x - 50, y)
    draw_circle(win, center, radius * 0.8, range - 1, x + 50, y)
    draw_circle(win, center, radius * 0.8, range - 1, x, y - 50)
    draw_circle(win, center, radius * 0.8, range - 1, x, y + 50)
    

def main(): #Sets up an initial circle and the screen
    win = GraphWin("", 800, 800)
    win.setBackground("black")

    x = 400
    y = 400
    center = Point(x, y)
    radius = 200
    range = 6

    draw_circle(win, center, radius, range, 400, 400)

    win.getMouse()
    win.close()

main()
