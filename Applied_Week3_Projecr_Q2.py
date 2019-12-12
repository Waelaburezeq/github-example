# # Question 2 : Merge two datasets

# In[112]:


############################################################################################### Question #2 ###########################################################################
geo_cord = pd.read_csv('https://ibm.box.com/shared/static/9afzr83pps4pwf2smjjcf1y5mvgb18rr.csv')#, index_col = 'Postal Code')

geo_cord.head()

merged_df = pd.merge(df, geo_cord, left_on='Postcode', right_on='Postal Code')
#pd.merge(df_a, df_b, right_index=True, left_index=True)
merged_df.head()


