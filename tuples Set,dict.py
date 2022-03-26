#!/usr/bin/env python
# coding: utf-8

# In[1]:


t=(1,2,3,4,5)


# In[2]:


type(t)


# In[13]:


l1=["sudh",345,45+67j,656.78,True]


# In[14]:


l1


# In[15]:


type(l1)


# In[9]:


t2=()


# In[10]:


type(t2)


# In[16]:


l1


# In[17]:


l1[0:2]


# In[18]:


t1=("sudh",345,45+67j,656.78,True)


# In[19]:


type(t1)


# In[20]:


t1[0:2]


# In[21]:


t1[::-1]


# In[22]:


t1[-1]


# In[23]:


t1[-1:-4:-1]


# In[24]:


t1[0::2]


# In[25]:


t1


# In[28]:


l1


# In[29]:


l=[4,5,6,7]


# In[30]:


l1[0]="kumar"


# In[31]:


l1


# In[33]:


l1.extend([1,2,3,4])


# In[34]:


l1


# In[35]:


t1


# In[37]:


t1[0]


# In[38]:


t1[0]="xyz"


# In[39]:


t1


# In[40]:


t2=(4,5,6,7)


# In[41]:


t1+t2


# In[44]:


t1


# In[46]:


l1


# In[49]:


l1.pop(1)


# In[50]:


l1


# In[51]:


t1


# In[52]:


t1.count("sudh")


# In[53]:


t1.index("sudh")


# In[54]:


t1.index(345)


# In[55]:


t1


# In[56]:


t=([1,2,3,4],("pra",56,67.45,4+5j),6,5,6)


# In[57]:


t


# In[58]:


t[0]


# In[59]:


t[0][1]='drt'


# In[60]:


t


# In[61]:


l=list(t)


# In[62]:


l


# In[63]:


type(l)


# In[64]:


l1=[1,2,3,4,5,6,67.87,6+8j]


# In[65]:


l1


# In[66]:


type(l1
    )


# In[67]:


tuple(l1)


# In[68]:


type(l1)


# In[69]:


l1


# In[71]:


type(tuple(l1))


# In[72]:


s={1,2,3,4,4,5,6,4}


# In[73]:


type(s)


# In[83]:


l=[1,2,3,4,5,6,76,5,5,5,5,5,5,2,3,4,5,6,1,2,3]


# In[75]:


s


# In[84]:


l


# In[85]:


set(l)


# In[86]:


s={}


# In[87]:


type(s)


# In[92]:


s


# In[94]:


s2={1,1,1,1,1,2,2,2,2,3,4,54,4,3,3,2,54}


# In[95]:


s2


# In[98]:


l4=list(s2)


# In[99]:


l4


# In[101]:


l4[0]


# In[102]:


s2


# In[103]:


s2.add(3546)


# In[104]:


s2


# In[105]:


s2.add("pras")


# In[106]:


s2


# In[107]:


s2.add[1,2,3,4,56,776,'sudh']


# In[110]:


{(3,4,5,6),(3,4,5,6),3,4,5,6}


# In[109]:


{[2,3,4,5,],3,4,5,3,4,5}


# In[111]:


s.remove(4)


# In[112]:


s2


# In[113]:


s2.remove(4)


# In[114]:


s2


# In[115]:


s2.discard(54)


# In[116]:


s2


# In[117]:


s2.remove(45)


# In[118]:


s2.discard(45)


# In[119]:


s2


# In[120]:


s2.add(45)


# In[121]:


s2


# In[122]:


s2[0]


# In[123]:


l=[1,2,3,4,5]


# In[125]:


l2=tuple(l)


# In[126]:


l2


# In[ ]:





# In[ ]:





# In[ ]:





# In[97]:


s2


# In[127]:


d={}


# In[128]:


type(d)


# In[129]:


d={4:[1,2,3,4,5,798.67,56+7j,"ptds"],6:"hello","table1":"apkakya name"}


# In[130]:


d


# In[131]:


d[0]


# In[132]:


d1={"key1":[1,2,3,4],"key2":"sudth","key1":45}


# In[133]:


d1


# In[135]:


d1['key1']


# In[136]:


d1={"key1":[1,2,3,4],"key2":"tjnkdne",'key3':[1,2,3,4]}


# In[137]:


d1


# In[138]:


d1['key1']


# In[139]:


d1['key3']


# In[142]:


d={"name":"Prashant",'Mobile':'9755442643','mailid':'prashant@gmail.com','key1':[1,2,3,4,5,6],'key2':{1,4,4,4,5,6,7,5,6,},'key3':(56796)}


# In[141]:


d


# In[143]:


d['name']


# In[144]:


type(d['name'])


# In[145]:


d.keys()


# In[146]:


d.values()


# In[147]:


d.items()


# In[148]:


d1={'key1':"prashant",'Key2':[1,2,3,4,5]}


# In[149]:


d1


# In[150]:


d1['key3']={1,2,3,4,5,5,6,6,5,5,6,7,8,9,9,9}


# In[151]:


d1


# In[152]:


del d1['key1']


# In[153]:


d1


# In[154]:


del d1


# In[155]:


d1


# In[156]:


d[(1,2,3,4)]='fjdnf'


# In[157]:


d


# In[158]:


d.get('name')


# In[160]:


d.get('Mobile')


# In[161]:


d.get('key1')


# In[162]:


d1={'key1':"prashnt",'key2':'Singh'}


# In[163]:


d2={'key3':'Beldiha',"key3":668,'key4':7+6j}


# In[164]:


d1.update(d2)


# In[165]:


d1


# In[166]:


d2


# In[167]:


d1+d2


# In[168]:


key=("name","mobile_no",'mailid ')
value="prashant"


# In[170]:


d=d1.fromkeys(key,value)


# In[171]:


d


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




