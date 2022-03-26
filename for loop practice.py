#!/usr/bin/env python
# coding: utf-8

# In[5]:


s="This is basic python class"


# In[6]:


len(s)


# In[8]:


count=0
for i in s :
    #count=count+1
    count+=1
print(count)


# In[9]:


s[::-1
 ]


# In[10]:


for i in range(len(s)-1,-1,-1):
    print(s[i],end="")


# In[11]:


s


# In[13]:


i=len(s)-1
while i>=0:
    print(s[i],end="")
    i=i-1


# In[14]:


a="ineuron"
v="AaEeIiOoUu"


# In[25]:


for i in a:
        if i in v:
            print (i," is Voval ")
        else:
            print (i,"not voval",)
        
       


# In[29]:


a="eye"
for i in a:
    


# In[57]:


s="eye"
s[len(s)-3-1]


# In[4]:


w=input()
s=w.lower()
for i in range(len(s)):
    if s[i] !=s[len(s)-i-1]:
        print ("it is not palidrom")
        break
else:
    print ("it is palidrom")
        
    


# In[102]:


s[len(s)-i-1]


# In[6]:


d={"India":"IN","CHINA":"CH","Canada":"Ca","United nation":"UN"}


# In[7]:


"India" in d


# In[8]:


"China" in d


# In[9]:


"CHINA" in d


# In[21]:


l_small=[]
l_grater=[]
for i in d:
    if len(i)<=5:
        l_small.append(i)
    else:
        l_grater.append(i)
print(l_small)
print (l_grater)
        


# d_1={  "ineuron" :{"a":14,
#                     "b":10,
#                     "c":4},
#             "course" :{"d":45,
#                         "e":34,
#                         "f":1
#                        }
# 
# 
# }

# In[21]:


d_1={ "ineuron" :{"a":50,"b":10,"c":20},
     "course" :{"d":45, "e":34, "f":1 }
    }


# In[2]:


d_1


# In[24]:


l2=[]
for i in d_1.values():
    for j in i.values():
        l2.append(j)
    print(max(l2))
        


# In[14]:


d.keys()


# In[ ]:


s[::-1]


# In[36]:


s[::-1]


# In[37]:


i


# In[13]:


l1=[]
s="This is my first Python Class"
for i in range (len(s)-1,-1,-1):
    l1.append(s[i])


# In[15]:


print(l1,end=" ")


# In[30]:


s="THIS IS MY FIRST PAYTHON CLASS"
i=(len(s)-1)
while i>=0:
    print (s[i],end=" ")
    i=i-1


# In[27]:


s="THIS IS MY FIRST PAYTHON CLASS"
i=(len(s)-1)


# In[28]:


i


# In[35]:


s="THIS IS MY FIRST PAYTHON CLASS"
for i in range (len(s)-1,-1,-1):
    print (s[i],end=" ")


# In[38]:


s="THIS IS MY FIRST PAYTHON CLASS"
i=len(s)-1
while i>=0:
    print(s[i],end='')
    i=i-1


# In[64]:





# In[71]:


a="ineuron"
v="AaEeIiOoUu"
count=0
for i in a:
    if i in v:
        count=count+1
print(count)
       # print (i,"is voval"
   # else:
        #print(i,"is not voval")


# In[108]:


a="eye"
for i in range (len(a)):
    if a[i]!=a[len(a)-i-1]:
        print("it is not palidrom")
        break
else:
    print("It is palidrom")


# In[106]:


a="eye"
for i  in range (len(a)):
    print(i)


# In[98]:


b="eye"
for i in range(len(b)-1,-1,-1):
    print(b[i])


# In[104]:


b[len(b)-i,-1]


# In[125]:


d={"India":"IN","CHINA":"CH","Canada":"Ca","United nation":"UN"}
l=[]
s=[]
for i in d:
    if len(i)<=5:
        l.append(i)

    if len(i)>5:
        s.append(i)
print(s)
print(l)
    


# In[127]:


d_1={ "ineuron" :{"a":50,"b":10,"c":20},
     "course" :{"d":45, "e":34, "f":1 }
    }


# In[128]:


d_1.keys()


# In[163]:


l3=[]
l4=[]
for i in d_1.values():
    #print (i)
    for j in i.values():
        print(j,end=' ')
        l3.append(j)


    
        


# In[164]:


l3


# In[167]:


l4=l3


# In[168]:


l4


# In[180]:


del l3[3:5]


# l3

# In[181]:


l3


# In[182]:


l4


# In[ ]:




