# imports in built turtle function
import turtle
# this assigns turtle to the variable t
import turtle as t
# setting turtle speed
t.speed(800)
pattern=(0)

# sets the screen to a pink colour
scr=turtle.Screen()
scr.bgcolor("blue")
# this is starting our spiral
for i in range(200):
    for color in ["cyan","magenta","yellow"]:
        t.color(color)
        t.forward(pattern)
        t.right(90)
        t.right(1)
        pattern+=1


turtle.done()
