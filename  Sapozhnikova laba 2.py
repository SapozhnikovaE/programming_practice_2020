#!/usr/bin/env python
# coding: utf-8

# In[3]:


#  буква S

import turtle as t
t.shape('turtle')
t.color('blue')
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.pu()
t.left(90)
t.forward(50)
t.pd()
t.color('green')
t.write("Sapozhnikova", font=18)
t.ht()
t.done()


# In[ ]:


# квадрат

import turtle as t
t.shape('turtle')
t.color('pink')
for i in range(4):
    t.forward(50)
    t.left(90)
t.done()


# In[ ]:


# круг

import turtle as t
t.shape('turtle')
t.color('red')
t.pensize(3)
sides=60
for i in range(sides):
    t.forward(10)
    t.left(360/sides)
t.done()


# In[ ]:


# 10 квадратов увеличивающегося размера

import turtle as t
t.shape('turtle')
t.speed(10)
t.color('green')
k=0
x=0
y=0
while k<=10:
   x+=-10
   y+=-10
   t.pu()
   t.goto(x,y)
   t.pd()
   t.forward(10+20*k)
   t.left(90)
   t.forward(10+20*k)
   t.left(90)
   t.forward(10+20*k)
   t.left(90)
   t.forward(10+20*k)
   t.left(90)
   k+=1
t.done()


# In[ ]:


#паук

import turtle as t
t.shape('turtle')
t.speed(10)
t.color('lightblue')
for i in range(36):
  t.forward(100)
  t.right(180)
  t.stamp()
  t.forward(100)
  t.right(190)
t.done()


# In[ ]:


#спираль

import turtle
import math
turtle.shape('turtle')
for i in range(1000):
   t=i/50*math.pi
   dx=t*math.cos(t)
   dy=t*math.sin(t)
   turtle.goto(dx,dy)
t.done()


# In[ ]:


# квадратная спираль

import turtle as t
t.shape('turtle')
t.speed(10)
t.color('green')
k=1
for i in range (99999):
    t.forward(2*k)
    t.left(90)
    t.forward(2*k)
    k+=1
t.done()


# In[ ]:


#    правильные многоугольники

import turtle as t
import math as m
t.color('red')
t.speed(10)
t.color('green')
k=0
n=3
r=15
def polygon(n,L):
    a=(n-2)*180/n
    for i in range(n):
        t.right(180-a)
        t.fd(L)
while k<999:
    L=2*r*m.sin(m.pi/n)
    ang=((n-2)*180/n)/2
    t.right(ang)
    polygon(n,L)
    t.left(ang)
    t.pu()
    t.fd(15)
    t.pd()
    r+=15
    n+=1
    k+=1
t.done() 


# In[ ]:


#  цветок из окружностей

import turtle as t
t.shape('turtle')
t.speed(50)
t.color('purple')
for i in range(6):
   t.circle(70)
   t.right(60)
t.done() 


# In[ ]:


# бабочка

import turtle as t
t.shape('turtle')
t.speed(20)
t.color('blue')
r=30
n=0
t.right(90)
for i in range(30):
   t.circle(r+n)
   t.right(180)
   t.circle(r+n)
   t.left(180)
   r+=3
   n+=1
t.done()   


# In[ ]:


# пружинка
 
import math
import turtle as t

def draw_arc(x0, y0, r, start_angle, end_angle):
   inc = 1 if start_angle<end_angle else -1
   for angle in range(start_angle, end_angle, inc):      
      x = r*math.cos(math.radians(angle))+x0
      y = r*math.sin(math.radians(angle))+y0
      t.goto(x,y)  

t.shape('turtle')

# Радиусы дуг
r1= 50  # верхней 
r2= 10  # нижней

# Начальная точка
x0, y0 = -t.window_width()//2+20, t.window_height()//2-100

t.penup()
t.goto(x0,y0)  
t.pendown()
t.speed(50)

for i in range(0,6):
   x = t.pos()[0] + r1    # x-координата центр верх. дуги
   draw_arc(x, y0, r1, 180, 0)
   
   x = t.pos()[0] - r2    # x-координата центр ниж. дуги 
   draw_arc(x, y0, r2, 360, 180)
      
t.pu()
t.home()
t.ht()
t.done()


# In[ ]:


# смайл

import turtle as t
t.shape('turtle')
t.speed(10)
t.pu()
t.goto(0,-100)
t.pd()
t.begin_fill()
t.fillcolor('yellow')
t.circle(100)
t.end_fill()
t.pu()
t.goto(-67,-40)
t.setheading(-60)
t.pd()
t.color('red')
t.width(5)
t.circle(80,120)
t.pu()
t.goto(0,5)
t.pd()
t.color('black')
t.width(5)
t.goto(0,-25)
t.fillcolor('blue')
t.color('blue')
for i in range(-35,105,90):
    t.pu()
    t.goto(i,35)
    t.pd()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
t.ht()
t.done()


# In[ ]:


#звезды

import turtle as t
t.shape('turtle')
t.speed(5)
t.color('red')
t.pu()
t.goto(-150,70)
t.pd()
t.left(180)
t.circle(100,extent=720,steps=5)
t.pu()
t.goto(250,0)
t.pd()
t.color('blue')
t.speed(10)
def star(n,dlina):
    if n%2!=0:
        for i in range(n):
            t.fd(dlina)
            y=n//2*360/n
            t.left(y)
    else:
        n=n+1
        star(n,dlina)
star(11,200)
t.ht()

