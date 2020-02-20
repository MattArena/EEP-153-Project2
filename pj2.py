#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[19]:


data = pd.read_csv("DRI - Complete.csv") 
# Preview the first 5 lines of the loaded data 
data.rename(columns = {'Life Stage\nGroup':'age'}, inplace = True) 
data.head()


# In[102]:


age_range = data['age'].str.split(r'–')
age_range
data['age_range']=age_range
data


# In[98]:


def get_dri(age,condition):
    if condition == 'Infants':
        data_copy = data[data['Infants']==1]
        for x in data_copy.index:
            if int(data_copy['age_range'][index][1])>age:
                return data_copy.loc[index]
    if condition == 'Children':
        data_copy = data[data['Children']==1]
        for x in data_copy.index:
#             print(data_copy['age_range'][0][0])
            if int(data_copy['age_range'][x][1])>age:
                return data_copy.loc[x]
    if condition == 'Males':
        data_copy = data[data['Males']==1]
        for x in data_copy.index:
#             print(data_copy['age_range'][0][0])
            if int(data_copy['age_range'][x][1])>age:
                return data_copy.loc[x]
    if condition == 'Females':
        data_copy = data[data['Females']==1]
        for x in data_copy.index:
#             print(data_copy['age_range'][0][0])
            if int(data_copy['age_range'][x][1])>age:
                return data_copy.loc[x]
    if condition == 'Pregnancy':
        data_copy = data[data['Pregnancy']==1]
        for x in data_copy.index:
#             print(data_copy['age_range'][0][0])
            if int(data_copy['age_range'][x][1])>age:
                return data_copy.loc[x]
    if condition == 'Lactation':
        data_copy = data[data['Lactation']==1]
        for x in data_copy.index:
            if int(data_copy['age_range'][x][1])>age:
                return data_copy.loc[x]
get_dri(45,'Females')


# In[ ]:




