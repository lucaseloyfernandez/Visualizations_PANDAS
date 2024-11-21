#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df1 = pd.read_csv(r"C:\Users\lucas\Desktop\Programacion 2019\Phyton\Merging DataFrames in Pandas\LOTR.csv")
df1


# In[7]:


df2 = pd.read_csv(r"C:\Users\lucas\Desktop\Programacion 2019\Phyton\Merging DataFrames in Pandas\LOTR 2.csv")
df2


# In[9]:


df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName'])


# In[11]:


df1.merge(df2, how = 'outer')


# In[13]:


df1.merge(df2, how = 'left')


# In[15]:


df1.merge(df2, how = 'right')


# In[17]:


df1.merge(df2, how = 'cross')


# In[19]:


df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left',rsuffix = '_Right')


# In[21]:


df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_Left',rsuffix = '_Right', how = 'outer')
df4


# In[23]:


pd.concat([df1,df2], join = 'outer', axis = 1)


# In[27]:





# In[ ]:





# In[ ]:




