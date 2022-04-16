#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[1,2,3,4,6]


# In[2]:


next(l)


# In[3]:


l=iter(l)


# In[4]:


next(l)


# In[5]:


next(l)


# In[7]:


r=range(6)


# In[8]:


next (r)


# In[12]:


g=range(0,45,3)


# In[15]:


for i in g:
    print(i,end=" ")


# In[22]:


def gencube(n):
    l=[]
    for i in range(n):
        l.append(i**3)
    return (l)
        


# In[28]:


def gencube(n):
    for i in range(n):
        yield i**3
                           #yeild function generate the gencube like range function .


# In[29]:


gencube (10)


# In[30]:


for i in gencube(9):
    print (i)


# In[ ]:


#fibonacci number 


# In[31]:


def fib(n):
    a=1
    b=1
    for i in range (n):
        yield a,i
        a,b=b,a+b
    


# In[35]:


for i in fib(10):
    print (i)


# In[38]:


def fib1(n):
    a=1
    b=1
    output=[]
    for i in range (n):
        output.append(a)
        a,b=b,a+b
    return output


# In[39]:


fib1(10)


# In[48]:


f=open("test.txt","w")


# In[42]:


pwd()


# In[52]:


ls


# In[ ]:


f.open('test.txt',"w")


# In[53]:


f.write("this is my first file opration")


# In[54]:


f.close()


# In[45]:


pwd()


# In[3]:


f=open("test3.txt",'w')


# In[5]:


ls


# In[6]:


f.write("This is my first reading file , I am very happy to write this , I don't know what to do for it . I have plan to complete Jan class by this week")


# In[7]:


f.close()


# In[3]:


f=open("test4.txt",'w')


# In[4]:


pf=open('test5.txt',"w")


# In[5]:


pf.write("I am not happy with your attitide as you ar doing")


# In[6]:


pf.close()


# In[12]:


sd=open("test6.doc","w")


# In[13]:


sd.write("I am very glad that i have joined ineuron to learn Data science ")


# In[14]:


sd.close()


# In[15]:


ls


# In[18]:


get_ipython().run_cell_magic('writefile', 'hello.txt', 'this is a data i would like to save in my file , i am glade to know that you are my friend')


# In[19]:


ls


# In[21]:


f=open('test.txt','r')


# In[22]:


f.read()


# In[27]:


f=open("test5.txt",'r')


# In[28]:


f.read()


# In[29]:


s=f.read()


# In[30]:


s


# In[31]:


f=open("test5.txt",'r')


# In[32]:


s=f.read()


# In[33]:


s


# In[34]:


type(s)


# In[36]:


for i in s:
    print (i,end=" **")


# In[37]:


f.read()


# In[38]:


f.seek(5)


# In[39]:


f.read()


# In[40]:


f.seek(0)


# In[41]:


f.read()


# In[42]:


f.read()


# In[44]:


f=open("test5.txt",'r')


# In[45]:


f.read()


# In[46]:


f.read()


# In[47]:


f.seek(1)


# In[48]:


f.read()


# In[50]:


f.tell()


# In[51]:


f=open("test.txt","r+")


# In[52]:


f.read()


# In[54]:


f.seek(0)


# In[55]:


f.readline()


# In[56]:


f.readline()


# In[57]:


f.readline()


# In[58]:


f.readline()


# In[59]:


f.readline()


# In[60]:


f.readline()


# In[61]:


f.readline()


# In[62]:


f.close()


# In[64]:


f=open("test.txt","r+")
for i in f:
    print(i,end=" ")


# In[65]:


f.write("fnfdihgudndgdgd")


# In[67]:


f=open("test.txt","r+")
for i in f:
    print(i,end=" ")


# In[68]:


f.seek(5)


# In[69]:


f.write(" I am happy person")


# In[109]:


f=open("test.txt","r+")


# In[71]:


f.close()


# In[8]:


f=open("test.txt","r+")


# In[7]:


f.replace ["got"="Prashant"]


# In[9]:


f[1]


# In[13]:


f=open("google.txt","r+")


# In[17]:


f.write()


# In[18]:


f.read()


# In[19]:


p=open("google.txt","r+")


# In[21]:


p.write("""Google LLC is an American multinational technology company that focuses on artificial intelligence,[10] search engine, online advertising, cloud computing, computer software, quantum computing,[11] e-commerce, and consumer electronics. It has been referred to as the "most powerful company in the world" and one of the world's most valuable brands due to its market dominance, data collection, and technological advantages in the area of artificial intelligence.[12][13][14] It is considered one of the Big Five American information technology companies, alongside Amazon, Apple, Meta, and Microsoft.

Google was founded on September 4, 1998, by Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of the stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly-owned subsidiary of Alphabet Inc.. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's Internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet.[15]

The company has since rapidly grown to offer a multitude of products and services beyond Google Search, many of which hold dominant market positions. These products address a wide range of use cases including email (Gmail), navigation (Maps), cloud computing (Cloud), web browsing (Chrome), video sharing (YouTube), productivity (Workspace), operating systems (Android), cloud storage (Drive), language translation (Translate), photo storage (Photo), video calling (Meet), smart home (Nest), smartphones (Pixel), wearable technology (Fitbit), gaming (Stadia), music streaming (YouTube Music), video on demand (TV), artificial intelligence (Assistant), machine learning APIs (TensorFlow), AI chips (TPU), and more. The company is also notorious for its vast portfolio of discontinued or replaced products,[16][17] which includes Google Glass, Google+, Reader, Play Music, Nexus, Hangouts, and Inbox by Gmail.

Google is well-known for it highly ambitious technological innovations aimed at solving humanity's biggest problems.[18] Some of these innovations include quantum computing (Sycamore), self-driving cars (Waymo, formerly the Google self-driving project), smart cities (Sidewalk Labs), and transformer models (Google Brain).""")


# In[22]:


p.close()


# In[24]:


p=open("google.txt","r+")


# In[25]:


p.read()


# In[27]:


p.seek(0)


# In[28]:


p.readline()


# In[29]:


for i in p:
    print(i,end=" ")


# In[30]:


serch="Google"


# In[31]:


re="Google prashant"


# In[32]:


p=open("google.txt","r")


# In[33]:


data=p.read()


# In[34]:


data=data.replace(serch,re)


# In[35]:


p=open("google.txt","w")


# In[36]:


p=p.write(data)


# In[39]:


p=open("google.txt","r+")


# In[40]:


p.read()


# In[42]:


p.seek(0)


# In[48]:


p.seek(0)


# In[49]:


len(p.readlines())


# In[50]:


l=p.readlines()


# In[51]:


l


# In[53]:


p.seek(0)


# In[54]:


l=p.readlines()


# In[55]:


l


# In[56]:


type(l)


# In[57]:


l


# In[60]:


l2=l[0].split()


# In[61]:


l2


# In[65]:


l3=[]
for i in l2:
    l3.append(i[0])
print (l3)


# In[66]:


len(l3)


# In[67]:


p.close()


# In[76]:


p=open("google.txt","r+")
p.name


# In[77]:


l4=["this is my 1st line ","this is my 2nd line ","this is my 3rd line ","this is my 4th line "]


# In[78]:


p.writelines(l4)


# In[79]:


p.close()


# In[81]:


p=open("google.txt","r+")
p.fileno()


# In[82]:


p.close()


# In[83]:


import os


# In[84]:


os.remove("google.txt")


# In[85]:


ls


# In[86]:


os.remove("google.txt")


# In[88]:


os.remove("google_wiki.text")


# In[90]:


os.remove("google_wiki.txt")


# In[95]:


os.remove("goolge_wiki")


# In[94]:


os.remove("goolge_wiki.txt")


# In[5]:


pwd()


# In[3]:


import os
os.getcwd()


# In[ ]:





# In[ ]:





# In[ ]:





# In[45]:


l


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




