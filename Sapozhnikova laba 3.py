
# In[1]:


#задание чтение индекса из файла

import turtle as t

def load_digits(file_name):
   digits = []   
   with open(file_name, "r", encoding="utf-8") as file:
      for line in file:
        line = line.strip()
        if line:
           digit = []
           for ps in line.split(', '):
              digit.append(tuple(map(int,ps.split(':'))))              
           digits.append(digit)   
   return digits   
   
   
def draw_digit(digit, x0, y0, digits):
   for i,point in enumerate(digits[digit]):
       if i == 0:             
           t.pu()
       else:
           t.pd()
       x = x0 + point[0]
       y = y0 - point[1]
       t.goto(x, y)

post_index = '141700'
digits = load_digits("font.txt") # загружаем числа от 0 до 9

# Начальная точка
x0, y0 = -t.window_width()//2+20 , t.window_height()//2-20 

for i in post_index:
  draw_digit(int(i), x0, y0, digits)
  x0 += 100

t.pu()
t.home()
t.done()


# In[1]:


# задание "рисование индекса"

import turtle as t
points = [ (0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)]

digits = [(0, 2, 4, 5, 3, 1, 0),  # 0
    (2, 1, 3, 5),  # 1
    (0, 1, 3, 4, 5),  # 2
    (0, 1, 2, 3, 4),  # 3
    (0, 2, 3, 5, 1),  # 4
    (1, 0, 2, 3, 5, 4),  # 5
    (1, 2, 4, 5, 3, 2),  # 6
    (0, 1, 2, 4),  # 7
    (0, 2, 4, 5, 3, 2, 3, 1, 0),  # 8
    (4, 3, 1, 0, 2, 3)]  # 9


def draw_digit(digit, x0, y0, digits, points):
    points_indexes = digits[digit]
    for i, point_index in enumerate(points_indexes):
        if i == 0:   
            t.pu()
        else:
            t.pd()

        x = x0 + line_length * points[point_index][0]
        y = y0 - line_length * points[point_index][1]
        t.goto(x, y)


post_index = '141700'  

line_length = 50 

x0, y0 = -t.window_width()//2+20 , t.window_height()//2-20 

for i in post_index:
   draw_digit(int(i), x0, y0, digits, points)
   x0 += int(1.5 * line_length)

t.pu()
t.home()
t.ht()
t.done()


# In[4]:


#задание "Движение газа"

import turtle as t
import random
t.speed(0)
t.pu()
t.ht()
t.width(5)
t.color('blue')
t.goto(200,200)
t.pd()
t.goto(200,-200)
t.goto(-200,-200)
t.goto(-200,200)
t.goto(200,200)
t.ht()
    
balls=[]
k=10
for i in range(k):
    ball=t.Turtle()
    ball.ht()
    ball.shape('circle')
    ball.pu()
    randx=random.randint(-190,190)
    randy=random.randint(-190,190)
    red=random.random()
    green=random.random()
    blue=random.random()
    ball.color(red,green,blue)
    ball.goto(randx,randy)
    ball.showturtle()
    dx=random.randint(-5,5)
    dy=random.randint(-5,5)
    balls.append([ball, dx, dy])
for i in balls:
    print(i)
while True:
    for i in range(k):
        balls[i]
        x,y=balls[i][0].position()
        if x+balls[i][1]>=190 or x+balls[i][1] <=-190:
            balls[i][1]=-balls[i][1]
        if y+balls[i][2]>=190 or y+balls[i][2]<=-190:
            balls[i][2]=-balls[i][2]
        balls[i][0].goto(x+balls[i][1],y+balls[i][2])


# In[3]:


#задание броуновское движение
   
import turtle as t
import random
t1=t.Turtle()
t2=t.Turtle()
t3=t.Turtle()
t1.color('blue')
t2.color('red')
t3.color('green')
t1.speed(30)
t2.speed(30)
t3.speed(30)
k=0
while k<=2000:
   t1.setheading(random.randint(0,360))
   t1.forward(random.randint(-30,30))
   t2.setheading(random.randint(0,360))
   t2.forward(random.randint(-20,20))
   t3.setheading(random.randint(0,360))
   t3.forward(random.randint(-15,15))
   k=k+1
t.done()    


# In[ ]:


# бросание мячика (скачущий мячик)

import turtle  as t
import math

x0, y0 = -t.window_width()//2+20 , 0

ground= t.Turtle()
ground.color('green')
ground.width(5)
ground.pu()
ground.goto(x0,0)
ground.pd()
ground.goto(t.window_width()/2-20,0)
ground.pu()

ball= t.Turtle()
ball.shape('circle')
ball.color('red')
ball.width(2)
ball.pu()
ball.setpos(x0, y0)
ball.pd()

dt = 1
g = 1
Vx = 20
Vy = 20
alpha = math.radians(80)

t = 0
while Vx>0 and Vy>0:
  
   # Движение тела, брошенного под углом к горизонту 
   x = Vx*t*math.cos(alpha)
   y = Vy*t*math.sin(alpha)-g*t**2/2     
   
   t += 0.5   
      
   if y < 0:  # Касание земли
       x0 += x
       y0 = 0              
       t = x = y = 0         
       
       # Потеря скорости
       Vx -= 2   
       Vy -= 2
       
   ball.setpos(x0+int(x), y0+int(y))       
      
ball.pu()
t.done()
   

