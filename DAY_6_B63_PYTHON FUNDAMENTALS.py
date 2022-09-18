#!/usr/bin/env python
# coding: utf-8

# In[6]:


#ORGANISING  THE LIST DATATYPE:
cars = ['audi','rolls royas','bmw','tata','maruthi','rangerover','suzuki','alto']
print(cars)


# In[7]:


cars.sort()....#temparuary approch...
print(cars)


# In[10]:


print(sorted(cars))....#permenent approch...


# In[14]:


len(cars)


# In[16]:


print(cars,'=',len(cars))


# In[17]:


cars.reverse()  #reverse order ....z--a
print(cars)


# In[18]:


#SLICING THE LIST DATATYPE..

students = ['divya','roohi','jasmine','neha','zaheer']
print(students)


# In[19]:


print(students[0:1])....#here we need divya and roohi but we are getting just divya ....so the other step is,,


# In[20]:


print(students[0:2])...here we get right because in slice we take +1 to indecate the value


# In[22]:


print(students[1:3])....if we enter the first value as 1 it takes as 1(divya) but we have to take 2 value as +1 then we get output


# In[24]:


print(students[2:4])


# In[25]:


print(students[0:4:1])....# we should enter +1 as at last because without entering we wont get last value


# In[26]:


print(students[0:5:1])...#like this 


# In[ ]:




