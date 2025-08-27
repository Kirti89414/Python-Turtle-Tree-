from turtle import *
t= Turtle()
w=Screen()
w.bgcolor('black')
t.color('orange')
t.pensize(2)
t.left(90)
t.backward(100)
t.shape('turtle')
t.hideturtle()
t.speed(600)

def tree(i) :
    if i<10 :
         return
    else :
         t.forward(i)
         t.color('orange')
         t.circle(2)
         t.color('brown')
         t.left(30)
         tree(3*i/4)
         t.right(60)
         tree(3*i/4)
         t.left(30)
         t.backward(i)

tree(100)
done()