#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Import pandas library
import pandas as pd


# In[25]:


#Read the csv file
df= pd.read_csv("car-sales-extended-missing-data 1.csv")
df


# In[26]:


#display all the rows and coloumns
#df = pd.set_option("display.max.rows", 1006)
#df= pd.set_option("display.max.columns", 6)


# In[27]:


#display the first five 
df.head(5)


# In[28]:


# Get information about the data set
df.info()


# In[32]:


#Identify which coloumns in the data set have missing values
missing_values = df.isnull()
missing_values


# In[33]:


#Determine the percentage of missing vales
perc_missing = missing_values.mean()*100
print(perc_missing)


# In[ ]:




