#!/usr/bin/env python
# coding: utf-8

# In[4]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


import statistics


# In[25]:


df1=sns.load_dataset('iris')


# In[9]:


df=sns.load_dataset('tips')


# In[10]:


df


# In[11]:


##mean
np.mean(df['total_bill'])


# In[12]:


##median
np.median(df['total_bill'])


# In[14]:


#mode
statistics.mode(df['total_bill'])


# In[15]:


sns.boxplot(df['total_bill'])


# In[17]:


sns.histplot(df['total_bill'],kde=True)


# In[18]:


sns.countplot(df['day'])


# In[20]:


sns.countplot(df['sex'])


# In[21]:


sns.countplot(df['time'])


# In[22]:


np.percentile(df['total_bill'],[25,75])


# In[23]:


IQR=24.1275-13.3475


# In[24]:


IQR


# In[26]:


df1


# In[30]:



##mean
np.mean(df1['sepal_length'])


# In[31]:


##median
np.median(df1['sepal_length'])


# In[32]:


##mode
#mode
statistics.mode(df1['sepal_length'])


# In[34]:


sns.boxplot(df1['sepal_length'])


# In[35]:


np.percentile(df1['sepal_length'],[25,75])


# In[36]:


IQR=6.4-5.1


# In[37]:


IQR


# In[38]:


###outliers
dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]


# In[61]:


###Zcore, IQR
outliers=[]

def detect_outlier(data):
    threshold=3 ##3 sd
    mean=np.mean(data)
    std=np.std(data)
    
    for i in data:
        z_score=(i-mean)/std
        if np.abs(z_score)>threshold:  #abs mean absoulute
            outliers.append(i)
    return outliers
            


# In[40]:


np.abs(-2.746)


# In[62]:


detect_outlier(dataset)


# In[ ]:


###outliers using IQR steps
1. sort the data
2. calculate Q1 and Q3
3. IQR(Q3-Q1)
4. FIND THE LOWER Fence (Q1-1.5(IQR))
5.FIND THE UPPER FENCE (Q3+1.5(IQR))


# In[47]:


dataset=sorted(dataset)


# In[48]:


dataset


# In[49]:


q1,q3=np.percentile(dataset,[25,75])


# In[50]:


print(q1,q3)


# In[51]:


IQR=q3-q1


# In[52]:


IQR


# In[53]:


##find the lower fence
lower_fence=q1-(1.5*IQR)


# In[54]:


lower_fence


# In[55]:


## higher fence
upper_fence=q3+(1.5*IQR)


# In[56]:


upper_fence


# In[ ]:




