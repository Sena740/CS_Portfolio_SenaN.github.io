#Recursion using turtle
#2024/10/21 By Sena Nishimura
import turtle
import random

def draw_triangle(t, size): #Draws an triangle with randamozied outline color
    t.color(random.random(), random.random(), random.random())
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)

def main(t, size, depth): #Recursion with the triangle rotating slightly and decrease in size
    if depth == 0:
        return
    draw_triangle(t, size)
    t.left(10)
    main(t, size - 5, depth - 1)

#Setups for the screen
screen = turtle.Screen()
screen.setup(width = 850, height = 850)

tt = turtle.Turtle()
tt.speed(0) 
screen.bgcolor("black")

main(tt, 400, 80)

turtle.done()