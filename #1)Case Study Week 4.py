#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import numpy, pandas,matplotlib.pyplot ans seaborn for using them appropriately
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_cars= pd.read_csv(r"C:\Users\Tejes\Downloads\cars_data.csv")


# In[8]:


# gives first five rows for all the columns
data_cars.head()


# In[9]:


# using sum function to find if any null value is present. Gives 0= no null values, 1= if null value present
pd.DataFrame(data_cars).isna().sum()


# In[26]:


# Using bar graph to plot Male Vs Female  
plt.figure(figsize=(6,6))
plt.bar(data_cars['Buyer Gender'],height=1, width=0.4)
plt.title('Male Vs Female in Car Sale')
plt.yticks()




# In[13]:


# Using sort_values function to sort on the basis of Sale Price, ascending= false is used for descending order
hc= data_cars. sort_values('Sale Price', ascending=False).head()
hc[['Make','Model','Sale Price']]


# In[12]:


# Using sort function to sort_values function the Sale Price, ascending = True is used for ascending order 
lc= data_cars. sort_values('Resell Price', ascending=True).head()
lc[['Make','Model','Resell Price']]

