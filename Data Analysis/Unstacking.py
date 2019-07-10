#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing Libraries
import pandas as pd


# In[3]:


#Importing From The Main 7 Month Data
df=pd.read_csv('43000123633_tickets-June-25-2019-05_11.csv')


# In[4]:


#Extracting Tickets After March 6
df1=df[df['Created time']>='2019-03-06 00:00:00']


# In[5]:


#Extracting Tickets Before June 6
df=df1[df1['Created time']<='2019-06-07 00:00:00']


# In[9]:


#Printing The Default Data
df[['Group','Status']].head(5)


# In[4]:


df.head()


# In[7]:


#Grouping Data according to Group And Status
g1=df1.groupby(['Group','Status']).agg({'Status':'count'})


# In[10]:


#Printing Grouped Data
g1.head(8)


# In[110]:


#Converting Multilevel Index to DataFrame Usng Unstacked Function
g1.unstack()


# In[ ]:


#Saving It In An Excel
pd.to_excel('')

