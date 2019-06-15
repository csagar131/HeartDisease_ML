#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# In[3]:


df = pd.read_csv('/root/Github/HeartDisease_ML/heart.csv')
df.head()


# # Decision Tree classifier

# In[4]:



features = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
features = features.fillna(features.mean())
features = features.values
label = df[['target']].values

x_train,x_test,y_train,y_test = train_test_split(features,label,test_size=0.2,random_state=4)



# # random forest classifier
# 

# In[5]:


clf = RandomForestClassifier(criterion='entropy',n_estimators=7)


# In[9]:


trained = clf.fit(x_train,y_train)


# In[10]:


predicted = trained.predict(x_test)
predicted


# In[11]:


print("Accuracy from random forest:- ",metrics.accuracy_score(y_test,predicted)*100)


# In[27]:


x_test.shape


# In[32]:


from numpy import array
a = array( [71,0,0,112,149,0,1,125,0,1.6,1,0,2] )
a.reshape(-1,1)
x_test[0].shape


# In[35]:


print("predicted output:-",list(trained.predict([a]))[0])


# In[ ]:




