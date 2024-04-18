from turtle import Screen, Turtle


scrn = Screen()
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70, -40, -10, 20, 50,80]

for turtle_index in range(0,6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-200,y=y_positions)

scrn.exitonclick()