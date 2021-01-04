#!/usr/bin/env python
# coding: utf-8

# # Mini-Project (Interpreting Relationship between several Social factors and the Infection rate of covid-19)

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


from plotly import __version__
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[3]:


import cufflinks as cf
init_notebook_mode(connected=True)
cf.go_offline()


# ##   Importing Covid-19 dataset (by John Hopkins University)

# In[4]:


covid = pd.read_csv("covid19_Confirmed_dataset.csv")


# In[5]:


covid.tail()


# In[6]:


covid.info(verbose=True)


# In[7]:


covid.drop('Lat',axis=1,inplace = True)
covid.drop('Long',axis=1,inplace = True)
covid


# In[8]:


covid= covid.groupby('Country/Region').sum()


# In[9]:


covid.info()


# In[10]:


covid


# In[11]:


covid.loc[["India","China","US"]].iplot(title="Covid Cases till 30-04-2020 in India, China and US")  #default: line plot


# ### Infection rate

# In[12]:


infection_rate = covid.diff(axis=1)
infection_rate


# In[13]:


max_rate = infection_rate.max(axis=1)
covid['Max_Infection_Rate'] = max_rate
covid


# ### New-dataframe(Corona_Data)

# In[14]:


Corona_Data = max_rate.to_frame().rename(columns={0:'Max Infection Rate'})
Corona_Data


# # Another Dataset ( Worldwide_happiness_report.csv)

# In[15]:


happiness_report = pd.read_csv('worldwide_happiness_report.csv')


# In[16]:


happiness_report.head()


# In[17]:


happiness_report.info()


# In[18]:


happiness_report.drop(['Overall rank','Score','Generosity','Perceptions of corruption'],axis=1,inplace=True)
happiness_report.head()


# In[19]:


sns.heatmap(happiness_report.isnull());


# In[20]:


happiness_report = happiness_report.set_index('Country or region')
happiness_report


# ## Merging Dataframe (happiness_report and Corona_Data)

# In[21]:


data = pd.merge(happiness_report, Corona_Data,right_index=True,left_index=True)
data


# In[22]:


data.info()


# ## Getting correlation between each columns of the dataframe - data

# In[23]:


result = pd.DataFrame.corr(data)
result


# ## Plotting the Relations :

# In[24]:


plt.figure(figsize=(12,8))
sns.set_style("darkgrid")
sns.lineplot(x="GDP per capita", y = "Max Infection Rate", data=result,lw =5).set_title('Relationship between GDP per capita and Max Infection Rate of a country',fontsize=20);


# In[25]:


plt.figure(figsize=(12,8))
sns.lineplot(x="Social support", y = "Max Infection Rate", data=result,lw=5).set_title('Relationship between Social Support and Max Infection Rate of a country',fontsize=20);


# In[26]:


plt.figure(figsize=(12,8))
sns.lineplot(x="Healthy life expectancy", y = "Max Infection Rate", data=result, lw=5).set_title('Relationship between Healthy Life Expectancy and Max Infection Rate of a country',fontsize=20);


# In[27]:


plt.figure(figsize=(12,8))
sns.lineplot(x="Freedom to make life choices", y = "Max Infection Rate", data=result, lw=5).set_title('Relationship between Freedom to make Life Choices and Max Infection Rate of a country',fontsize=20);

