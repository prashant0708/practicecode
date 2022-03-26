#!/usr/bin/env python
# coding: utf-8

# In[2]:


l=['name','emailid','phonno','address']
for i in range(len(l)):
    print(i, l[i])


# In[3]:


s="ineuron"
for i in s:
    print(i)


# In[4]:


l


# In[6]:


for i in l:
    if i=="phonno":
        break
    print(i)
else:
    print("check this statement")
    


# In[7]:


a=1
while a<6:
    print(a)
    a=a+1


# In[16]:


a=1
while a<6:
    print(a)
    if a==4:
        break
    a=a+1


# In[19]:


a=1
while a<6:
    print(a)
    a=a+1
    if a==3:
        continue
        


# In[ ]:





# In[20]:


a=1
while a<5:
    continue


# In[23]:


range(6)


# In[26]:


list(range(3,50,5))


# In[27]:


list(range(3,10,-1))


# In[30]:


list(range(10,6,-1))


# In[32]:


list(range(-5,10,(2)))


# In[33]:


for i in range(7):
    print(i)


# In[38]:



for i in range(0,20):
    for j in range(0,i+1):
        print("*" , end=" ")
    print("\r")


# In[46]:


l=[1,2,3,43,555,6,7,78]
for i in  range(len(l)):
                print(i, l[i])


# In[ ]:





# In[40]:


t=(3,4,5,6,7,8)


# In[41]:


for i in t:
    print(i)


# In[47]:


t


# In[48]:


t[::-1]


# In[62]:


for i in range (len(t)-1,-1,-1):
    print (t[i],end=" ")


# In[53]:


t


# In[63]:


d={"a":"jdfngjhf","b":"gffudhgud","c":[1,2,3,4,5],"d":(4,5,6,7),"e":"sudh"}


# In[68]:


for i in d.:
    print(i,d[i])


# In[70]:


for i in d.items():
    print(i)


# In[69]:


d.items()


# In[66]:


d.keys()


# In[67]:


d.values()


# In[71]:


s={1,2,3,4,5,5,5,6,7,7,8,8,8,9,9,9,8,7,6,5,4,3,2}


# In[72]:


s


# In[78]:


for i in s:
    print(i,end=" ** ")


# In[ ]:




