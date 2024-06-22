import turtle

#Dibuja una linea de (x1, y1) to (x2,y2)
def drawLine(x1,y1,x2,y2):
    turtle.penup()

    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)

#Write a string s at the specifies location (x,y)
def writeText(s,x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown() 
    turtle.write(s)

#DRAW A POINT AT THE SPECIFIED LOCATION (X,Y)
def drawPoint(x,y):
    turtle.penup()
    turtle.goto(x. y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

#DRAW A CIRCLE CENTERED AT (x, y)
def drawCircle(x = 0, radius = 10):
    turtle.penup()
    turtle.goto(x, y -radius)
    turtle.pendown()
    turtle.circle(radius)

#DRAW A RECTANGLE AT (X,Y) WITH THE SPECIFIED WIDTH AND HEIGHT
def drawRectangle(x =0, y =0; width = 10, height = 10):
    turtle.penup()
    turtle.goto(x + width / 2, y + height /2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.penup()
    turtle.goto(x, y - radius)
    


