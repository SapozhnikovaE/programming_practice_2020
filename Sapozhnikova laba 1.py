
# In[2]:


import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-150,150,1)
plt.plot(x,np.log((x**2+1)*np.exp(-abs(x)/10))/np.log(1+np.tan(1+np.sin(x)*np.sin(x))**-1))
plt.show


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-100,100,1)
plt.plot(x,x*x-x-6)
plt.show


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
y=eval(input())
with plt.xkcd():
        plt.pie([45,35,20], labels=('Cats', 'Dogs', 'Birds'))
        plt.title('PETS', size=16)
plt.show


# In[15]:


x=int(input())
import numpy as np
y=np.log(np.exp((np.sin(x)+1)**-1)/(1,25+1/(5*x)))/np.log(1+x**2)
print(y)


# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(-2, 2, 0.01)
y_values = np.empty(x_values.size)   

def weierstrass(x, a, b, e):  # e это epsilon  точность вычисления
   y = 0
   n = 0
   while True:
      try: 
         s = (b**n)*math.cos((a**n)*math.pi*x)
         n += 1         
         y += s
         if math.fabs(s)<e:
             return y
      except: # 'y' нельзя вычислить при некоторых значениях 'x' 
         pass                 
  
a = 3 
b = 1/2

for i, x in enumerate(x_values):
   y_values[i] = weierstrass(x, a, b, 0.01)
      
plt.plot(x_values,y_values)
plt.show()


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
a = np.arange(0, 10, 0.001)
y = [1, 1.42, 1.74, 2, 2.24, 2.45]
p, v = np.polyfit(x, y, deg=1, cov=True)
c, d= np.polyfit(x, y, deg=2, cov=True)
e, h= np.polyfit(x, y, deg=3, cov=True)
p_f = np.poly1d(p)
c_f = np.poly1d(c)
e_f = np.poly1d(e)
plt.errorbar(x, y, xerr=0.05, yerr=0.08)
plt.plot(a,p_f(a))
plt.plot(a, c_f(a))
plt.plot (a,e_f(a))
plt.grid(True)
plt.show()


# In[ ]:




