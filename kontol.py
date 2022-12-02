import turtle

t = turtle.Turtle()
# t.color('') # i like them black
t.pensize(2)
turtle.title('Kontol')
# t.speed(10) change the speed however you like it

t.circle(49)
t.home()
t.forward(300)
t.right(90)
t.circle(39)
t.penup()
t.home()
t.left(90)
t.forward(99)
t.right(90)
t.pendown()
t.forward(350)
t.circle(-39)
t.penup()
t.home()
t.left(90)
t.forward(300)
t.pendown()
t.write('I <3 You', True, align='left', font=('Arial', 15, 'italic'))
turtle.exitonclick()
