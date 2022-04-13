#!/usr/bin/env python
# coding: utf-8

# In[1]:


class dic :
    def __init__(self,d):
        self.d=d
    def mykey(self):
        if type(self.d)==dict:
            return self.d.keys()


# In[2]:


x=dic({"a":10,"b":20,"c":"prashant"})


# In[3]:


x.mykey()


# In[1]:


class dic :
    def __init__(self,d):
        self.d=d
    def mykey(self):
        if type(self.d)==dict:
            return self.d.keys()
    def myvalue(self):
        if type(self.d)==dict:
            return self.d.values()
    def notdict(self):
            if type(self.d)!=dict:
                raise Exception ("enter value is not dict")
        
    def giveinput(self):
        self.d=eval (input())
        if  type(self.d)==dict:
            print (self.d.keys())
            print (self.d.values())
    def newvalue(self,k,v):
        if type(self.d)==dict:
            ty= self.d[k]=v
            print(ty)


# In[3]:


pr=dic({"a":10,"b":20,"c":"prashant"})


# In[ ]:


pr.giveinput()


# In[ ]:


pr.newvalue("k1",45)


# In[3]:


import  mydict


# In[4]:


mydict.dic


# In[5]:


d=mydict.dic({"a":10,"b":20,"c":"prashant"})


# In[7]:


d.mykey()


# In[ ]:


#Homework

q1. create your own package for your all the list function
q2. create your own package for your all the tuples function 
q3. create your own package for your all the dictonery function
q4.crate your own package for your all the set function 

restriction:
    always use exception handling
    never use print statment
    always use logging while writing a code and log every activity performed by code in respective logging file.
    

