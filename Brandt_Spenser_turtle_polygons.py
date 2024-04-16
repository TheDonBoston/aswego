# Program asks user to input a number of sides, and color of their desired polygon
# Grey background is generally more pleasing than a white screen.
# Try "8" and "red" for a stop sign!
import turtle
turtle.title("Create your own polygon!")
t = turtle.Turtle()
s = t.getscreen()
turtle.bgcolor("grey")

# Ask the user to input an integer of their desired number of sides
sides = int(input("Enter the number of sides for your polygon: "))

# Calculating the interior angle; sides has been defined as the int input by the user
interior = (sides - 2) * 180 / sides

# Ask the user for their desired color
color = input("Enter the color of your polygon: ")
t.fillcolor(color)
t.begin_fill()

# The programmer chose this value due to the aesthetics of the size
for i in range(sides):
    t.bk(90)
    t.rt(180 - interior)
    """This is done so the angles stay right angles, which is what a polygon contains"""

# This stays down here because first, the polygon needs to be drawn, then filled in.
t.end_fill()    

# Hides turtle after drawing your polygon; keeps my turtle screen from closing!
t.hideturtle()
turtle.mainloop()