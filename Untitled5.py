#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas  as pd 
import numpy as np
import matplotlib as plt
import cufflinks as cf
cf.go_offline()


# In[4]:


df=pd.read_excel("D://Ineuron//India Population data set.xlsx")


# In[5]:


df


# In[17]:


df=df.drop('Area',axis=1)


# In[19]:


df=df.drop('Population Density',axis=1)


# In[27]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[24]:


df.iplot(kind="barh",size=100)


# In[45]:


df.iplot(kind="choropleth",locations="State",z="Population", colorscale="PiYG")


# In[ ]:




