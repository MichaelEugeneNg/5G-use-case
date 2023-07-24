import turtle
import numpy as np
import _tkinter

def drawCellTowers(x1,y1,r1,x2,y2,r2,x3,y3,r3,solution_x,solution_y,true_x,true_y):
  turtle.screensize(10000, 10000)
  myPen = turtle.Turtle()
  myPen.hideturtle()
  # myPen.tracer(0)
  myPen.speed(0)
  window = turtle.Screen()
  window.bgcolor("#F0F0F0")

  myPen.color("#ff5744")
  myPen.penup()
  myPen.goto(true_x,true_y)
  myPen.pendown()
  myPen.dot(10)
  myPen.penup()

  myPen.color("#ff5744")
  myPen.penup()
  myPen.goto(x1-5,y1)
  myPen.pendown()
  myPen.goto(x1+5,y1)
  myPen.penup()
  myPen.goto(x1,y1-5)
  myPen.pendown()
  myPen.goto(x1,y1+5)
  myPen.penup()
  
  myPen.goto(x1,y1-r1)
  myPen.pendown()
  myPen.circle(r1)
  
  myPen.color("#41befc")
  myPen.penup()
  myPen.goto(x2-5,y2)
  myPen.pendown()
  myPen.goto(x2+5,y2)
  myPen.penup()
  myPen.goto(x2,y2-5)
  myPen.pendown()
  myPen.goto(x2,y2+5)
  myPen.penup()
  
  myPen.goto(x2,y2-r2)
  myPen.pendown()
  myPen.circle(r2)
  myPen.penup()
  
  myPen.color("#52bf54")
  myPen.goto(x3-5,y3)
  myPen.pendown()
  myPen.goto(x3+5,y3)
  myPen.penup()
  myPen.goto(x3,y3-5)
  myPen.pendown()
  myPen.goto(x3,y3+5)
  myPen.penup()
  
  myPen.goto(x3,y3-r3)
  myPen.pendown()
  myPen.circle(r3)
  myPen.penup()
  
  myPen.goto(solution_x,solution_y)
  myPen.pendown()
  myPen.dot(10)
  myPen.penup()
  
  myPen.getscreen().update()

  turtle.mainloop()
  # return x1,y1,r1,x2,y2,r2,x3,y3,r3