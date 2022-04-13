#!/usr/bin/env python
# coding: utf-8

# In[1]:


#oops is nothing but object orianted programming language . It is provide more stracture to the program , It also 
#increase the reuse ability of the program and in oops concept we consider everything as object to program


# In[ ]:


#class is nothing but blueprint and object is real world entity , in OOP we drive everything as class and object .opps is nothing but where we bind the entire program 
#statement as class and object. 


# In[2]:


class car:
    pass  # if we don't write any thing we just right pass


# In[11]:


class car:
    def __init__(self,brand_name,fuletype,body_type ):
        self.brand_name=brand_name
        self.fuletype=fuletype
        self.body_type=body_type
    def desc_car(self):
        print(self.brand_name,self.fuletype,self.body_type)
        
#__init__ it is inbuilt function and called constructor , it help to provide the data to the class
#self is act as pointer and it is not reserve keyword , we can use any thing in place of self.


# In[14]:


inova=car("toyota","Petrol","SUV")
nexon=car("Tata","Petrol","min suv")
fortunr=car("toyota","Disel","SUV")


# In[13]:


inova.desc_car()


# In[15]:


nexon.desc_car()


# In[16]:


fortunr.desc_car()


# In[18]:


fortunr.body_type # when we call to bodytype it is calling to self.bodytype because class only understand self.bodytype veriable 
                  # class don't undrstand the variable only body_type. 


# In[20]:


fortunr.desc_car()


# In[29]:


class car:
    def desc_car(self):
        print("this is my first class on prng without __init__")
#in this case we are not providing any data to class just creating some function . 
#self is pointer in that .


# In[ ]:





# In[30]:


x=car()
#variable of class is called object where x is object of car 


# In[31]:


x.desc_car()


# In[43]:


class list_parcel:
    def parcel(self,a):
        if type(a)==list:
            for i in a:
                print (i,end=" ")
    def reverse_list(self,z):
        if type(z)==list:
            return z[::-1]
        


# In[44]:


b=list_parcel()


# In[45]:


b.parcel([1,2,3,4,5,6,7,8,9,10])


# In[47]:


b.reverse_list([1,2,3,4,5,6,7,8,9,10])


# In[49]:


class list_parcel:
    def __init__(self,l):
        self.x=l
    def parcel(self):
        if type(self.x)==list:
            for i in self.x:
                print (i,end=" ")
    def reverse_list(self):
        if type(self.x)==list:
            return self.x[::-1]
        


# In[51]:


b=list_parcel([1,2,3,4,5,6,7,789,675,78846.356])


# In[52]:


b.parcel()


# In[53]:


b.reverse_list()


# In[ ]:


#create a class to pass the dictonary
1. write a function to give all the key.
2. write a function to give all the values.
3. write a function to throw an exception in case of not passing dictonary
4.write a finction to take user input and throw key and value out of dictonary
5. write a function to insert new key value pair into dictonery 


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
            self.d[k]=v
            print("value entered")
                


# In[ ]:


pr.giveinput()


# In[3]:


pr=dic({"a":10,"b":20,"c":"prashant"})


# In[ ]:


pr.mykey()


# In[ ]:


pr.myvalue()


# In[6]:


pr=dic((4,5,6,7))


# In[7]:


pr.notdict()


# In[23]:


pr=dic({"a":10,"b":20,"c":"prashant"})


# In[8]:


pr.giveinput()


# In[ ]:


pr.newvalue("k2",56)


# In[ ]:


#try the above function with module function 


# In[3]:


open("mydict.py","w")


# In[1]:


pwd()


# In[4]:


ls


# In[ ]:




