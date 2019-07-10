#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install fuzzywuzzy[speedup]

import pandas as pd

import numpy as np

import numpy as np


# In[ ]:


source=pd.read_csv('City_harmonization (1).csv')
city_names=pd.read_excel('City TL Mapper.xls')
list_all=pd.read_excel('Town_Codes_2001.xls',skiprows=[0,1,2,3,4])
list_all.columns=['A','city','C','D','E','F','G']
list_all.city[0:100]
ser=city_names['Name of City']
ser


# In[ ]:


ind=0
for x in ser:
  x=str.strip(x).lower()
  ser[ind]=x
  ind=ind+1


# In[ ]:


from fuzzywuzzy import fuzz
s=pd.Series()
index=0
for x in source['src_name']:
  if(pd.isnull(source['trg_name'][index])): 
    x=str.strip(x)
    x=x.lower()
    max=0
    match=""
    for y in list_all['city']:
      y=str(y)
      y=str.strip(y)
      y=y.lower()
      ratio = fuzz.ratio(x,y)
      if(ratio>81):
        if(ratio>max):
          max=ratio
          match=y
    if(max<=81):
      match=np.nan
      data = np.array([x])
      s = pd.Series(data)
      ser=ser.append(s)
    else:
      check=0
      for q in ser:
        if(q==str(match)):
          print('matched')
          check=1
      if(check==0):
        print('in')
        print(str(match))       
        data = np.array([match])
        s = pd.Series(data)
        ser=ser.append(s)
    source['trg_name'][index]=match
    
  index=index+1


# In[ ]:


ser.to_excel("final_Cities.xlsx")


# In[ ]:


index=0
for x in source['trg_name']:
  source['trg_name'][index]=str(str(x).capitalize())
  index=index+1


# In[ ]:


source.to_excel("Updated_City_Harmonization.xlsx")

