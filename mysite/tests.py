import turtle

def draw_square(turtles):

    for i in range(4):
        turtles.forward(100)
        turtles.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    for i in range(36):
        draw_square(brad)
        brad.right(10)


    window.exitonclick()
draw_art()