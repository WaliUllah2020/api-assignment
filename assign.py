#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import pandas as pd
responce = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=76b4692e06d117640732aebeefad6f60');
a = responce.json();
# puts data in DataFrame
df2 = pd.DataFrame.from_dict(a);
# data frame contained nested dictionary so we seperated the result columb as a dictionary
df= df2['results'].to_dict();
# I created an other Data frame for our results .
df1 = pd.DataFrame.from_dict(df);
print(df1)


# In[ ]:





# In[ ]:




