#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Ecuaciones de segundo grado")


# In[2]:


a = int(input("introduce el valor de a: "))


# In[3]:


b = int(input("introduce el valor de b: "))


# In[4]:


c = int(input("introduce el valor de c: "))


# In[5]:


print("Esta es la ecuacion: " + str(a) + "x^2 + " + str(b) +  "x +  "  + str(c) +  " = 0 ")


# In[6]:


if b**2 > (4*a*c):
    e = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))


# In[7]:


if b**2 < (4*a*c):
    e = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("El resultado esta en numeros complejos")
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))


# In[ ]:




