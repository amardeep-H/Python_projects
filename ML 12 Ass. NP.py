#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1: Create a 4X2 integer array and Prints its attributes
# • The shape of an array.
# • Array dimensions.
# • The Length of each element of the array in bytes.

import numpy as np 
ad = np.array([[1,2],
              [3,4],
              [5,6],
              [7,8]])


# In[2]:


print("Printing numpy array Attributes : ")
print("Array shape is : "  + str(ad.shape))


# In[3]:


print("Array dimensions are : " + str(ad.ndim))


# In[4]:


print("Length of each element in the array is : "+ str(ad.itemsize))


# In[5]:


# Question 2: Create a 5X2 integer array from a range between 100 to 200
# such that the difference between each element is 10

ap = np.arange(100,200,10)
ap.reshape(5,2)


# In[6]:


# Question 3: Following is the provided numpy array. return array of
# items in the third column from all rows.

aj = np.array([[1,2,3],[4,5,6], [7,8,9]])


# In[7]:


aj


# In[8]:


aj[:, 2:].reshape(1,3)


# In[9]:


# Question 4: Following is the given numpy array return array of odd
# rows and even columns

ar = np.arange(3, 61,3).reshape(5,4)
ar


# In[10]:


af = ar[::2,1::2]
print(af)

# OR
ap = ar[0::2]
ap


# In[11]:


at = ar[::, 1::2]
at


# In[12]:




ag = np.intersect1d(at, ap).reshape(3,2)
ag


# In[13]:


# Question 5: Split the array into four equal-sized sub-arrays
# Note: Create an 8X3 integer array from a range between 10 to 34 such that
# the difference between each element is 1 and then Split the array into four
# equal-sized sub-arrays.

am = np.arange(10,34,1).reshape(8,3)
print(am)
print("Dividing 8X3 array in 4 equal parts")
print(np.split(am, 4))


# In[14]:


# Question 6: Create an 8x8 matrix and fill it with a checkerboard pattern.


# In[ ]:





# In[19]:


ab = np.zeros((8,8), dtype=int)

ab[1::2,::2] = 1
ab[::2,1::2] = 1
ab


# In[ ]:


ab[1]

