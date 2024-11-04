import turtle

#Set up screen
screen=turtle.Screen()
screen.bgcolor('lightblue') #Background color

#Function to draw an equilateral triangle
def draw_triangle(side_length):
    turtle.fillcolor('yellow') #Fill color for tringle
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()

#Function to draw a rectangle
def draw_rectangle(width, height):
    turtle.fillcolor('green') #Fill color for rectangle
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

#Function to draw a hexagon
def draw_hexagon(side_length):
    turtle.fillcolor('red') #Fill color for hexagon
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(side_length)
        turtle.left(60)
    turtle.end_fill()

#Main drawing sequence
turtle.penup()
turtle.goto(-100, 0) #Position for triangle
turtle.pendown()
draw_triangle(100)

turtle.penup()
turtle.goto(-100, -75) #Position for rectangle
turtle.pendown()
draw_rectangle(150, 75)

turtle.penup()
turtle.goto(100, 0) #Position for hexagon
turtle.pendown()
draw_hexagon(50)

turtle.hideturtle()
turtle.done()