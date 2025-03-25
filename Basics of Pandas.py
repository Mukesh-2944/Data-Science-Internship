#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install pandas


# In[12]:


import pandas


# In[13]:


print(pandas.__version__)


# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("world_happiness_report.csv")


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.head(n=10)


# In[7]:


df.tail()


# In[8]:


df.describe()


# In[9]:


df.shape


# In[10]:


df.info()


# In[11]:


df.columns


# In[12]:


list(df.columns)


# In[13]:


df.isnull()


# In[14]:


df.isnull().sum()


# In[15]:


df.dtypes


# In[16]:


df['Country']


# In[17]:


df[['Country','Unemployment_Rate','Population']]


# In[18]:


df[df.index==0]


# In[50]:


df[df.index.isin(range(50,60))]


# In[53]:


df.iloc[0][1]


# In[56]:


df.iloc[0]


# In[61]:


df.loc[10][10]


# In[60]:


df.loc[2500:2599]


# In[65]:


df.iloc[[10,20,30]]


# In[69]:


df[df['Country']=='India']


# In[70]:


df[df['GDP_per_Capita']>20000]


# In[71]:


df.rename(columns={'GDP_per_Capita':'GDP'},inplace=True)


# In[72]:


df


# In[75]:


df.mode()


# In[76]:


df.dropna()


# In[77]:


df.fillna(0)


# In[82]:


df.drop('Climate_Index',axis=1)


# In[86]:


df['new_column']=df['Public_Trust']+df['Corruption_Perception']
df


# In[89]:


df=df.sort_values(by='Healthy_Life_Expectancy', ascending=True)


# In[100]:


df


# In[111]:


df = df.set_index(["Year","Freedom"])


# In[112]:


df


# In[113]:


df=df.reset_index()


# In[114]:


df


# In[ ]:




