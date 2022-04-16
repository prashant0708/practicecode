#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#INHARIANTANCE 
Inharitance is nothing but some kind of personality occupied from grandmafather, father , mother like voice , body stracture , nature.


# In[2]:


class xyz:#init is constructor which provide the data to class from objct
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def test(self):
        print ("this is my first test method of xyz class ")
    def test1(self):
        print ("this is a tst1 meth of xyz class")
    def test2(self):
        print ("this is my test2 meth of xyz class")
        


# In[5]:


p=xyz(1,2,3)# p is varialble of xyz


# In[6]:


p.test1()


# In[ ]:





# In[3]:


class xyz1(xyz):#how to reutlize the xyz class in xyz1 class.
    pass


# In[7]:


q=xyz1()# it is throwing error because we have not provided a,b,c which is assigned in xyz class , becuase we have rutliz the xyz class in xyz1 class 


# In[10]:


q=xyz1(3,4,5)


# In[11]:


q.test1()


# In[12]:


q.test2()


# In[13]:


class xyz1(xyz):
    def test(self):
        print("this is a test meth avilable in the xyz1")


# In[14]:


g=xyz1(4,5,6)


# In[15]:


g.test()


# In[2]:


class xyz():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def test(self):
        print("this is a meth of xyz class")
class xyz1:
    def __init__(self,p,q,v):
        self.p=p
        self.v=v
        self.q=q
    def test1(self):
        print ("this is a meth from class xyz1")


class  child(xyz,xyz1):
    pass


# In[3]:


n=child()   #here it is asking only three variabes a,b,c bwcause xyz is entered first , if we change the position let say xyz1 firts , t will show p,q,r as missing .


# In[19]:


n.


# In[10]:


class xyz():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def test(self):
        print("this is a meth of xyz class")
class xyz1:
    def __init__(self,p,q,v):
        self.p=p
        self.v=v
        self.q=q
    def test1(self):
        print ("this is a meth from class xyz1")


class  child(xyz,xyz1):
    def __init__(self,*args):#staric arges we write so we can use more variables .
        xyz. __init__(self,*args)
        xyz1.__init__(self,*args)
#here we can constrat both class variable , a,b,c,p,q,r


# In[11]:


n= child(4,5,6)


# In[12]:


n.p


# In[13]:


class xyz():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def test(self):
        print("this is a meth of xyz class")
class xyz1:
    def __init__(self,p,q,v):
        self.p=p
        self.v=v
        self.q=q
    def test1(self):
        print ("this is a meth from class xyz1")


class  child(xyz,xyz1):
    def __init__(self,*args,**kwargs):#staric arges we write so we can use more variables .
        xyz. __init__(self,*args,)
        xyz1.__init__(self,**kwargs)


# In[14]:


t=child(4,5,6)#here it is asking p,q,r vlaues as well.


# In[15]:


t=child(4,5,6,p=3,q=4,v=5)


# In[16]:


t.a


# In[17]:


t.b


# In[18]:


t.p


# In[20]:


t.test()


# In[21]:


t.test1()


# In[22]:


class xyz():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def test(self):
        print("this is a meth of xyz class")
class xyz1(xyz):
    def test1(self):
        print ("this is a meth from class xyz1")
class xyz2(xyz1):
    def test2(self):
        print("this is a meth from class 2")

#this is called multiinheriant class xyz taken in xyz1 and xyz1 taken in xyz2.


# In[23]:


v=xyz2()


# In[25]:


v=xyz1(5,6,7)


# In[26]:


v.test1()


# In[ ]:


#q1- create a file class for reading data from respective file with amethod name read and write.
#q2- try to inherit read and write method from parent class to child class to perform read and write operation 


# In[37]:


import logging 

logging.basicConfig(filename="text.log",level="DEBUG",format='%(acstime)s,%(levelname)s,%(message)s')
class filetask():
    def __init__ (self,filename,filetype):
        self.filename=filename
        self.filetype=filetype
    def write (self):
        try:
            f=open(self,"w")
            f.write("this is my class work for file operation on class opps methods")
            f.close()
        except Exception as e:
            print(e)
            
    def read (self):
        try:
            f=open(self.filename,'r')
            print(f.read())
            f.close()
        except Exception as e:
            print (e)
class child (filetask):
    pass


# In[38]:


prash=filetask("testingclass",".txt")


# In[41]:


#consept of publc , private protected concept 


# In[42]:


class test :
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
class test1 (test):
    pass 
u=test(4,5,6)


# In[43]:


u.a


# In[44]:


class test :
    def __init__(self):
        self.a=4
class test1 (test):
    def __init__(self):
        self.a=7
    
u=test()


# In[45]:


u.a


# In[46]:


v=test1()


# In[47]:


v.a


# In[48]:


class test:
    def __init__(self):
        self.a=4
class test1(test):
    def __init__(self):
        test.__init__(self)
        self.a=7
u=test()


# In[49]:


u.a


# In[50]:


v=test1()


# In[51]:


v.a


# In[54]:


class test:
    def __init__(self):
        self._a=4
class test1(test):
    def __init__(self):
        test.__init__(self)
        self._a=7
u=test()


# In[56]:


u._a


# In[57]:


v=test1()


# In[58]:


v._a


# In[ ]:


class test:
    def __init__(self):
        self.__a=4
class test1(test):
    def __init__(self):
        test.__init__(self)
        self.__a=7
u=test()


# In[59]:


u.__a


# In[60]:


v=test1()


# In[61]:


v.__a


# In[ ]:


# we can't acess the variable as python is not allowing it to acess called private variable.


# In[ ]:


# we can acess these variable with dfferent method which is following 


# In[73]:


#incapsulation of class 
class test:
    def __init__(self,a,b,c):
        self._a=a # a is protected variables
        self.__b=b # b is private variables 
        self.c=c
class test1(test):
    pass
v=test(4,5,6)


# In[64]:


v._a #here one underscore is allowing to acess the varable  "a is protected variables "


# In[65]:


v.__b #here we use double underscore in the class and if we try toacess with double underscore as well python will not allow to acess. 

"b is private variables here "


# In[66]:


#we have another methods to acess these kind if variables .


# In[67]:


v._test__b # thi is the methods to acess private variables .


# In[75]:


u=test1(4,5,6)


# In[76]:


u.c


# In[78]:


u._a


# In[85]:


u._test1__b


# In[84]:


u._test__b


# In[118]:


class bonusclaculator:
    def __init__(self,empid,emprating):
        self.empid=empid
        self.emprating=emprating
        self.__bonusratingA="70%"
        self.__bonusratingB="60%"
        self.__bonusratingC="40%"
    def bonuscalculator (self):
        if self.emprating=="A":
            bonus=self.__bonusratingA
            return bonus
        elif self.emprating=="B":
            bonus=self.__bonusratingB
            return bonus
        else:
            bonus=self.__bonusratingC
            return bonus
        


# In[94]:


emp1=bonusclaculator(101,"A")
emp2=bonusclaculator(102,"B")


# In[95]:


emp1.bonuscalculator()


# In[123]:


emp2.bonuscalculator()


# In[125]:


emp1._bonusclaculator__bonusratingB="60%"


# In[126]:


emp1.empid=104


# In[127]:


emp1.empid


# In[128]:


emp1.emprating="B"


# In[129]:


emp1.bonuscalculator()


# In[130]:


emp1.__bonusratingB='90%'


# In[131]:


emp1.bonuscalculator()


# In[132]:


emp2.emprating


# In[133]:


emp2.bonuscalculator()


# In[134]:


emp1.bonuscalculator()


# In[159]:


class empcalculator :
    def __init__(self,empid,emprating):
        self.empid=empid
        self.emprating=emprating
        self.__empratingA="70%"
        self.__empratingB="60%"
        self.__empratingC="40%"
    def empcalculator(self):
        if  self.emprating=="A":
            bonus=self.__empratingA
            return bonus
        elif self.emprating=="B":
            bonus=self.__empratingB
            return bonus
        else:
            bonus=self.__empratingC
            return bonus


# In[160]:


emp10=empcalculator(123,"A")


# In[161]:


emp10.empid


# In[162]:


emp10.emprating


# In[163]:


emp10.empcalculator()


# In[166]:


emp10._empcalculator__empratingA="90%"


# In[167]:


emp10.empcalculator()


# In[ ]:




