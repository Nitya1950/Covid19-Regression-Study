#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('Student_dataset.csv')


# In[3]:


data.shape


# In[6]:


data.head()


# To find is there any null values and to sum up the columns

# In[ ]:


data.isnull().sum()


# In[ ]:


data.dtypes


# TypeCasting the object type into required datatype

# In[7]:


data['Gender']=data['Gender'].astype('category')


# In[ ]:


data.dtypes


# To Count the number of rows in a feature

# In[8]:


data['Age'].value_counts()


# In[9]:


data['On a scale of 1-5 , 1 being the least , how distracted were you by the following? [Social Media]'].describe()


# In[ ]:


sns.histplot(data['percentage_mean'], kde = False, bins = 200)
plt.show()


# In[ ]:


# Binary Features
plt.figure(figsize=(22, 6))
#fig, axs = plt.subplot(ncols=2)

# Item Visibility

sns.histplot(data['Item_Visibility'])
plt.xlabel('Item Visibility')
plt.ylabel('Frequency')


# In[ ]:


# Item Weight

sns.histplot(data['Item_Weight'])
plt.xlabel('Item Weight')
plt.ylabel('Frequency')


# In[ ]:


#Box_Plot
plt.boxplot(data['stud_productive'])
plt.xlabel('stud_productive')
plt.ylabel('Frequency')
plt.show()


# In[ ]:


# Custom function for visualisation of Categorical Variables 
def UVA_category(data, var_group): 
     
  # setting figure_size 
  size = len(var_group) 
  plt.figure(figsize = (7*size,5), dpi = 100) 
 
  # for every variable 
  for j,i in enumerate(var_group): 
    norm_count = data[i].value_counts(normalize = True) 
    n_uni = data[i].nunique() 
 
  #Plotting the variable with every information 
    plt.subplot(1,size,j+1) 
    sns.barplot(norm_count, norm_count.index , order = norm_count.index) 
    plt.xlabel('fraction/percent', fontsize = 10) 
    plt.ylabel('{}'.format(i), fontsize = 10) 
    plt.title('n_uniques = {} \n value counts \n {};'.format(n_uni,norm_count))


# In[ ]:


UVA_category(data, ['stud_productive','most_preffered_days','mode_study'])


# In[ ]:


fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(data['stud_productive'],data['percentage_mean'])
# Show Plot
plt.show()


# In[ ]:


plt.figure(figsize=(22, 6))
sns.boxplot(x="stud_productive", y="percentage_mean", data=data)
plt.show()


# In[ ]:


fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(data['prefday_learning'],data['percentage_mean'])
# Show Plot
plt.show()


# In[ ]:


plt.figure(figsize=(22, 6))
sns.boxplot(x="prefday_learning", y="percentage_mean", data=data)
plt.show()


# In[ ]:


# using a crosstab to analyse the categorical varriables 
pref_comfortable_learning= pd.crosstab(index=data['prefday_learning'],columns=data['mode_study']) 
outlet_establishment_location.plot(kind="bar",figsize=(8,8), stacked=True)


# In[ ]:


plt.figure(figsize=(12, 6)) 
corr = data.apply(lambda x: pd.factorize(x)[0]).corr() 
ax = sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)

