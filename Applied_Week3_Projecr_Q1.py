#!/usr/bin/env python
# coding: utf-8

# Importing Data from Wiki Link and ignoring Not assigned Borough

# In[80]:


import numpy as np
import pandas as pd

tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M', header=0,
                      keep_default_na=False)

headings = ['Postcode','Borough','Neighbourhood']
for table in tables:
    current_headings = table.columns.values[:3]
    if len(current_headings) != len(headings):
        continue
    if all(current_headings == headings):
        break

#table['Country name'].replace({r'.*!(.*)': r'\1'}, regex=True, inplace=True)
table[headings].to_csv('test.txt', sep=';', header=False, index=False)

df = table[table['Borough']!='Not assigned']


# # Question 1: Import data from Wiki and do some data cleansing

# In[81]:


############################################################################################### Question #1 ###########################################################################

# Merging Duplicated Neighbourhood
df.groupby(['Postcode','Borough'])['Neighbourhood'].apply(' '.join).reset_index()

# Replacing Not Assigned Neighbourhood by Borough
print(df.loc[df['Neighbourhood'] == 'Not assigned']) #M7A Postal Code

#df['Neighbourhood'] = np.where(df['Neighbourhood'] == 'Not assigned', df['Borough'], df['Neighbourhood'])
#df.Neighbourhood[df.Neighbourhood == 'Not assigned'] = df.Borough
df.Neighbourhood.replace('Not assigned',df.Borough,inplace=True)

print(df.loc[df['Postcode'] == 'M7A']) #  M7A  Queen's Park  Queen's Park


# Data Frame Shape

# In[82]:


df.shape #(210,3)
#df.set_index('Postcode',drop = True, inplace=True)
#df.reset_index(drop=True)
df.head()


