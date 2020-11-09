

# In[ ]:


"""Дано действительное положительное число a и целоe число n.
 Вычислите a в степени n. Решение оформите в виде функции power (a, n). 
 Стандартной функцией возведения в степень пользоваться нельзя. 
 (pythontutor.ru, 8 урок, отрицательная степень) """

a=float(input())
n=int(input())
def power (a,n):
     res=1
     for i in range (abs(n)):
         res*=a
     if n>=0:
         return res
     else:
         return (1/res)
print(power (a,n)) 


# In[ ]:


"""Напишите функцию вычисляющие наибольшие общие делители (НОД) для множества пар чисел. """

a = int(input())
b = int(input())
def nod (a,b):
    while a!=b:
         if a>b:
             a=a-b
         else:
             b=b-a
    return (a)
print (nod(a,b))


# In[7]:


"""Напишите функцию, которая в зависимости от выбора 
   пользователя вычисляет площадь круга, прямоугольника или треугольника. 
   Для вычисления площади каждой фигуры должна быть написана отдельная функция. """

import math

def circle_square(r):
    return math.pi*(r**2)

def rectangle_square(a, b):
    return a*b   
   
def triangle_square(a, b, c):   
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c)) # формула Герона https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0_%D0%93%D0%B5%D1%80%D0%BE%D0%BD%D0%B0
    
if __name__=="__main__":     
    print("Для вычисления площади круга введите один параметр - радиус круга\n"
          "Для вычисления площади прямоугольника введите два параметра - две его стороны (через пробел)\n"
          "Для вычисления площади треугольника введите три параметра - три его стороны (через пробел)")
    
    line = input().strip()
    values =  [ float(s) for s in line.split() ]
    
    if len(values) == 1:
        print("Площадь круга:", circle_square(*values))
    elif len(values) == 2:
        print("Площадь прямоугольника:", rectangle_square(*values))
    elif len(values) == 3:
        print("Площадь треугольника:", triangle_square(*values))        
    else:    
        print("Ошибочный ввод!")   


# In[8]:


""" Напишите функцию, которая на вход принимает квадратную матрицу (например, в виде списка списков). 
Вычисляет сумму элементов главной или побочной диагонали в зависимости от выбора пользователя. Сумма элементов любой диагонали должна вычисляться в одной и той же отдельной функции """

"""
Главной диагональю матрицы называется диагональ, 
    проведённая из левого верхнего угла матрицы в правый нижний.

Побочной диагональю матрицы называется диагональ,
    проведённая из левого нижнего угла матрицы в правый верхний.
"""

import math

def diagonal_sum(matrix, main_diagonal):
    sum_ = 0
    if main_diagonal:
        for i in range(len(matrix)):        
            sum_ += matrix[i][i]   
    else:
        for i in range(len(matrix)):
            sum_ += matrix[len(matrix)-i-1][i]              
    return sum_    
          
if __name__=="__main__":     
   matrix = [
     [1, 3, 4],
     [5, 6, 7],
     [8, 9, 0]
   ]          
   
   text = "Для вычисления суммы главной диагонали введите '1', для побочной '0':"
   main_diagonal = bool(int(input(text)))
   print("Cумма:", diagonal_sum(matrix, main_diagonal))
   


# In[9]:


""" Вычислить значения нижеприведенной функции 
в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
 {
   y = x^2 при -5 <= x <= 5; 
   y = 2*|x|-1 при x < -5; 
   y = 2x при x > 5
 }.
   
 Вычисление значения функции оформить в виде программной функции,
 которая принимает значение x, а возвращает полученное значение функции (y). 
 Нарисуйте с помощью matplotlib график этой функции. """

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    if x< -5:
       return 2*abs(x)-1
    elif -5 <= x <= 5:
       return x**2
    else: 
       return 2*x 
          
if __name__=="__main__":
    a = -10
    b = 10
    h = 1  
    
    x_values = []     
    y_values = []
    
    for x in range(a, b+1, h):
        y = func(x)
        print("f({}) = {}".format(x,y)) 
        
        x_values.append(x)    
        y_values.append(y)

    plt.plot(x_values,y_values)
    plt.show()   


# In[ ]:




