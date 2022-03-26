#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas  as pd 
import numpy as np
import matplotlib as plt 


# In[27]:


df=pd.DataFrame(np.random.randn(1000),columns=['data'],index=pd.date_range('2022/03/26',periods=1000))


# In[12]:


df


# In[9]:


df=pd.read_csv("https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/master/Iris.csv")


# In[30]:


df=df.drop('Id',axis=1)


# In[31]:


df.plot(figsize=(30,10))


# In[18]:


da=pd.read_csv("https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/master/Iris.csv")


# In[19]:


da


# In[27]:


df=da.drop('Id',axis=1)


# In[ ]:





# In[28]:


df.plot(figsize=(30,10))


# In[29]:


df


# In[36]:


df.iloc[5:11].plot(kind='bar',figsize=(20,10))


# In[38]:


df.iloc[5:6].plot(kind='bar',figsize=(20,10))


# In[ ]:





# In[37]:


df.iloc[5:6]


# In[39]:


df.iloc[5:6].plot(kind='barh',figsize=(20,10))


# In[40]:


df.iloc[5:11].plot(kind='barh',figsize=(20,10))


# In[42]:


df.plot(kind='hist',figsize=(20,10))


# In[44]:


df['SepalLengthCm'].plot(kind='hist',orientation='horizontal')


# In[54]:


df.hist(figsize=(20,10),color='g',alpha=.5)


# In[55]:


df


# In[58]:


df.plot(kind='box',figsize=(20,10),color={'box'})


# In[ ]:





# In[57]:


df.describe()


# In[63]:


df.plot(kind='area',figsize=(20,10),alpha=0.5,stacked=False )


# In[64]:


df.plot(kind='area',figsize=(20,10),alpha=0.5,stacked=True )


# In[ ]:





# In[66]:


df


# In[ ]:





# In[61]:


df.plot(figsize=(20,10))


# In[67]:


df.plot.scatter(x='SepalLengthCm',y='PetalLengthCm')


# In[72]:


df.plot.scatter(x='SepalLengthCm',y='PetalLengthCm',c='SepalWidthCm',s=df['PetalWidthCm']*500)


# In[73]:


df.plot.scatter(x='SepalLengthCm',y='PetalLengthCm',c='SepalWidthCm',s=500)


# In[78]:


df.plot.hexbin(x='SepalLengthCm',y='PetalLengthCm',gridsize=10,)


# In[32]:


df


# In[33]:


df1=df.iloc[0]


# In[84]:


df1


# In[34]:


df2=df.drop(columns='Species').iloc[0]


# In[36]:


df2.plot(kind='pie')


# In[2]:


get_ipython().system('pip install plotly')


# In[37]:


df


# In[12]:


import cufflinks as cf


# In[9]:


pip install cufflinks


# In[28]:


df.iplot()


# In[14]:


import cufflinks as cf
cf.go_offline()


# In[5]:


import pandas  as pd 
import numpy as np
import matplotlib as plt 


# In[17]:


df=pd.read_csv("https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/master/Iris.csv")


# In[16]:


df=df.drop('Id',axis=1)


# In[17]:


df


# In[18]:


df.iplot()


# In[19]:


df.iplot(x='SepalLengthCm',y='PetalLengthCm',mode='markers',kind='scatter')


# In[20]:


df.iplot(kind='scatter',mode='markers',size=3)


# In[45]:


df.iplot(kind='bubble',x='SepalLengthCm', y='PetalLengthCm',size='PetalWidthCm')


# In[21]:


df.scatter_matrix()


# In[47]:


df


# In[24]:


df.iplot(kind='scatter3d',x='SepalLengthCm',y='PetalLengthCm',z='PetalWidthCm')


# In[25]:


df10=df.iloc[0]


# In[31]:


df10.iplot(kind='scatter3d',x='SepalLengthCm',y='PetalLengthCm',size='PetalWidthCm')


# In[ ]:





# In[27]:


df.iplot(kind='bubble3d',x='SepalLengthCm',y='PetalLengthCm',z='PetalWidthCm',size='PetalWidthCm')


# In[3]:


rf=pd.read_excel("D://Ineuron//India Population data set.xlsx")


# In[4]:


rf


# In[22]:


rf.iplot()


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




