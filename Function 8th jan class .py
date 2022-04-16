#!/usr/bin/env python
# coding: utf-8

# In[7]:


def test (a,*sudh,b,c):
    return a,sudh,b,c


# In[9]:


test(45,6,7,8,9,5,[3,4,5,6,"sudh"],b=5,c=6)


# In[ ]:





# In[6]:


a


# In[19]:


def test1(*args):# * called staric , when we use staric with variable it mean we can input multiple list or number can assigmned to the function to perform .
    l=[]
    for i in args:
        if type(i)==list:
            l.append(i)
    return l
        


# In[20]:


test1(1,2,3,4,5,6,[1,56,78,45,"fghg",5+7j],[56,78,45,867,5+8j,"ghtgnd"])


# In[21]:


# if we want dic value and key as retun in function , we use double staric function .
def type7(**kwarg):
    return kwarg


# In[22]:


type7(a=56,b=45,c=56)


# In[24]:


type7(a=56,b=56,c=[1,2,3,4,5,6,"gfgjf"])


# In[25]:


def type8(**kwarg):
    return kwarg


# In[26]:


type8(name="prashant",age="27",phone="812367446845",email_id="gthyu@grig.com",address="bangalore")


# In[27]:


def type10(a,**kwarge):
    return a, kwarge


# In[29]:


type10(45,t=56,b=["dgd",56,45,78],c=45,d=78)


# In[30]:


def type11(a,**kwarge,*awarge):  # we can't pass fist n number of key argumnts then n number of arguments together , we need to change the sequence.
    return a, kwarge,awarge


# In[31]:


def type12(a,*awarge,**kwarge):
    return a,awarge,kwarge


# In[32]:


type12(3,4,5,6,7,d=56,t=56)


# In[36]:


a= lambda a,b: (a*b,a+b)


# In[37]:


a(45,45)


# In[38]:


a= lambda *a:a


# In[39]:


a(45,56,78)


# In[45]:


a= lambda **kwarge:kwarge


# In[46]:


a(b=56,c=34)


# # 

# In[51]:


a=10
def type12(c,d):
    c=5
    return c*d


# In[52]:


type12(a,50)


# In[55]:


l=[1,2,3,4,5,6,78,98,7]
l1=[]


# In[57]:


for i in l:
    l1.append(i+2)
print(l1)


# In[58]:


def type17(a):
    l1=[]
    for i in l:
        l1.append(i+2)
    return l1
    


# In[59]:


type17(l)


# In[63]:


a= lambda a: [i+2 for i in a]


# In[64]:


a(l)


# In[66]:


[i**2 for i in l]


# In[67]:


[(i**2,i+i) for i in l]


# In[68]:


[(i**2,i+i) for i in l if i<4]


# In[3]:


d1={}
for i in range (10):
    d1[i]=i**2


# In[4]:


d1


# In[5]:


a=56
for i in a:
    print (a)


# In[13]:


s="sudh"
for i in range (len(s)-1,-1,-1) :
    print (s[i],end=" ")


# In[ ]:





# In[10]:


next(s)


# In[14]:


b=iter(s)


# In[15]:


b


# In[16]:


next(b)


# In[17]:


next(b)


# In[18]:


next(b) #iterabl is some thing which can be acessable in sequence wise.


# In[20]:


l=[1,2,3,4,5,6,7,8,9]


# In[21]:


next(l)


# In[22]:


a=iter(l)


# In[24]:


next(a)


# In[25]:


next(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




