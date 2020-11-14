

# In[1]:


"""
   Упражнение 1

На одном графике изобразите время затраченное на вычисление с использованием массивов numpy и стандартных списков в питоне.

Для более точных результатов замеряйте время выполнения функции несколько раз и усредняйте.
    Используйте функцию z = 2*x**2 + 4*y
	Перемножение матриц размера n на n
"""

import math
import time
import numpy as np
import matplotlib.pyplot as plt

# Тест1. Вычисление ф-ции

def test1_numpy(x, y):
    start = time.time()
    z = 2 * x ** 2 + 4 * y
    t = time.time() - start
    return t 

def test1_list(x, y):
    start = time.time()
    z = []
    for i in range(len(x)):
       z.append(2 * x[i] ** 2 + 4 * y[i])
    t = time.time() - start
    return t   

def test1(n, m):   # n размер, m количество повторов для усреднения
    # numpy
    x = np.random.random(n)
    y = np.random.random(n)    
    numpy_time = 0
    for i in range(m):
       numpy_time += test1_numpy(x, y)
   
    # list
    x = x.tolist()
    y = y.tolist()
    list_time = 0
    for i in range(m):
       list_time += test1_list(x, y)
       
    return numpy_time/m, list_time/m
    
# Тест2. Перемножение матриц  
  
def test2_numpy(x, y):
    start = time.time()
    z = np.dot(x, y)
    t = time.time() - start
    return t 

def test2_list(x, y):
    start = time.time()
    range_ = range(len(x))
    z = [ [ 0. for _ in range_] for _ in range_ ]
    for row in range_:
       for col in range_:
          for i in range_:
             z[row][col] += x[row][i]*y[i][col]                      
    t = time.time() - start
    return t 
    
def test2(n, m):  # n размер, m количество повторов для усреднения
    # numpy
    x = np.random.random((n,n))
    y = np.random.random((n,n))
    
    numpy_time = 0
    for i in range(m):
       numpy_time += test2_numpy(x, y)
   
    # list
    x = x.tolist()
    y = y.tolist()
    
    list_time = 0
    for i in range(m):
       list_time += test2_list(x, y)
       
    return numpy_time/m, list_time/m
    
np.random.seed()  
  
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

print("Подождите идут вычисления ...")

# Тест1. Вычисление ф-ции
n_values = np.arange(1000, 10000+1, 1000)  
numpy_time_values = np.empty(len(n_values))   
list_time_values =  np.empty(len(n_values))
for i, n in enumerate(n_values):
    numpy_time_values[i], list_time_values[i] = test1(n, 20)

ax1.plot(n_values, list_time_values, color='red') 
ax1.plot(n_values, numpy_time_values, color='blue')
ax1.legend(['list', 'numpy.ndarray'], loc='upper center')

# Тест2. Перемножение матриц 
n_values = np.arange(10, 100+1, 10)
numpy_time_values = np.empty(len(n_values))   
list_time_values =  np.empty(len(n_values))
for i, n in enumerate(n_values):
    numpy_time_values[i], list_time_values[i] = test2(n, 5)

ax2.plot(n_values, list_time_values, color='red') 
ax2.plot(n_values, numpy_time_values, color='blue')
ax2.legend(['list of lists', 'numpy.ndarray'], loc='upper center')

plt.show()


# In[2]:


""" 
  Упражнение 2  
  Создайте массив чисел от 2 до 75. Выведите только нечётные. 
  Присвойте нечётным числам этого массива значение -1.
"""

import numpy as np

a = np.arange(2, 75, 1) 

print("Нечетные:\n", a[a%2!=0])

a[a%2!=0] = -1
     
print("После присвоения:\n", a)   


# In[3]:


""" 
Упражнение 3
 	Найдите в документации функцию, которая удаляет из одного массива элементы, которые есть в другом. 
	Приведите примеры использования.
"""

import numpy as np

# будем генерировать массивы произвольно
np.random.seed()
a = np.random.randint(0, 10, 10)
b = np.random.randint(5, 15, 10)

# Разница множеств (массивов)
c = np.setdiff1d(a, b)  

print('a= ', a)
print('b= ', b)
print('a-b= ', c)


# In[4]:


""" 
Упражнение 4
	Создайте случайную квадратную матрицу случайного размера от 10 до 100. 
	Найдите максимум и сумму элементов.
	Поделите каждый элемент матрицы на максимум.
	Отнимите от каждой строки матрицы среднее по строке.
	Замените максимальное значение на -1.
"""

import numpy as np


np.random.seed()

low = 10
high = 100

size = np.random.randint(low, high, size=2)
a = np.random.uniform(low, high, size=size)

print('Matrix:\n', a)

# максимум и сумму элементов.
print('Max: ', a.max())
print('Sum: ', a.sum())

# каждый элемент матрицы на максимум.
a = a/a.max()

# Отнимите от каждой строки матрицы среднее по строке.
a -= a.mean(axis=1, keepdims=True)

# Замените максимальное значение на -1.
max_pos = np.unravel_index(np.argmax(a), a.shape) 

print(f"Max: a{max_pos} =", a[max_pos])

a[max_pos] = -1

print('Matrix:\n', a)


# In[5]:


""" 
Упражнение 5
    Напишите функцию, которая берет многомерный вещественный массив 
    с пропущенными значениями (np.nan) и 
    возвращает его копию с заполненными пропусками 
    (заменять средним значением всех элементов массива).
    Если в массиве одни пропущенные значения, заполните их нулями.
"""

import numpy as np

def replace_nan_values(array_):  
   value= np.nanmean(array_) if not np.isnan(array_).all() else 0    
   return np.nan_to_num(array_, copy=True, nan=value)


a1 = np.array([[ 1, np.nan, 3], 
               [ np.nan, 5, 6], 
               [ 7, np.nan, np.nan]])
                
a2 = np.array([[ np.nan, np.nan], 
               [ np.nan, np.nan]])

                 
b1 = replace_nan_values(a1)                
print("Test1.Matrix has nan elements:\n", b1)            

b2 = replace_nan_values(a2)                
print("Test2.All elements of matrix is nan:\n", b2)            


# In[6]:


""" 
Упражнение 6
	Напишите функцию которая нормализирует заданный numpy-массив,
    так чтобы его значения лежали в интервале 

"""
# np.ptp это разница np.max-np.min 

import math
import numpy as np

def normalize_values(array_, new_min, new_max):  
    k = (new_max-new_min)/np.ptp(array_)    
    return (array_-np.min(array_))*k+new_min 
                           
a = np.array([ 0., 1., 2., 5., 10.])
print(a)

b = normalize_values(a, 0, 100)  
print(b)


# In[7]:


""" 
Упражнение 7
	Запишите numpy-array в файл.
	Считайте numpy-array из файла.
"""

import numpy as np

                           
a = np.array([[0., 1., 2.],
              [3., 4., 5.]])

np.savetxt('array.txt', a, delimiter=';', fmt='%1.4e') 

b = np.loadtxt('array.txt', dtype='float', delimiter=';')                 
print(b)


# In[6]:


""" 
Упражнение 8
	Создайте случайный массив
    Найдите в массиве элемент ближайший к данному
"""

import numpy as np

def find_nearest(array_, value):  # возвращает индекс ближайшего элемента
    return (np.abs(a-value)).argmin()
          
np.random.seed()
a = np.random.uniform(low=-50, high=50, size=10)

print("Array:\n", a)

index = find_nearest(a, value=10)

print(f"Nearest: a[{index}] = {a[index]}")


# In[9]:


""" 
Упражнение 9
	Напишите функцию, которая возвращает целочисленную матрицу
    с заданным значением на границах 
    матрицы и с заданным значением внутри
"""

import numpy as np


def create_filled_matrix(shape, out_value, in_value, dtype='int32'):
    a = np.empty(shape=shape, dtype=dtype)    
    a[:, 0] = a[:, -1] = out_value  # левая и правая граница
    a[0, 1:-1]= a[-1, 1:-1] = out_value # верх и низ  
    a[1:-1, 1:-1] = in_value # внутри           
    return a
    
a = create_filled_matrix(shape=(10,5),out_value= 1, in_value= 2)    
    
print(a)  


# In[7]:


""" 
Упражнение 10
  Напишите функцию, которая сортирует строки данной матрицы
  по значениям заданного столбца в порядке убывания. 
"""


import numpy as np

def sort_rows_by_column(array_, column):
   return array_[np.argsort(array_[:, column])[::-1]] # [::-1] это реверс (по убыванию)

np.random.seed()
a = np.random.randint(low=-10, high=10, size=(5,5))

print("Matrix:\n", a)

column = 1
b = sort_rows_by_column(a, column)

print(f"Matrix after sort by column {column}:\n", b)


# In[11]:


""" 
Упражнение 11
	Напишите функцию, которая создает двоичную матрицу шахматной доски с заданным shape
"""

import numpy as np

def chess_board(shape):
   a = np.zeros(shape=shape, dtype=int)
   # Заполняем через один(с шагом 2) 
   a[1::2, ::2] = 1    
   a[::2, 1::2] = 1
   return a

print(chess_board((4, 4)))


# In[ ]:




