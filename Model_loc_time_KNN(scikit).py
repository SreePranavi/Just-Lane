#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


dataset = pd.read_csv(r'C:\Users\sreep\Desktop\projects and hackathons\INTEL_20\data_loc_time.csv')


# In[4]:


#Label encoding alarm type

dataset['alarmType']=dataset['alarmType'].astype('category')
dataset['alarmType_cat']=dataset['alarmType'].cat.codes


# In[5]:


dataset.dtypes


# In[6]:


dataset.head(5)
'''
for i in range(len(dataset['alarmType'])):
    if dataset['alarmType'][i]=='stoppage':
        print(dataset['alarmType_cat'][i])'''


# In[7]:


#Features ClassLabels

#X = dataset.iloc[:,:-2].values
#Y = dataset.iloc[:,:4].values


X = dataset.drop(['alarmType_cat','alarmType'],axis=1)
Y = dataset['alarmType_cat']


# In[8]:


#Train test split

from sklearn.model_selection import train_test_split as tts
X_train, X_test, Y_train, Y_test = tts(X,Y, test_size = 0.10, shuffle=True)

print("Training length:" + repr(len(X_train)))
print("Testing length:" + repr(len(X_test)))
print("Training length:" + repr(len(Y_train)))
print("Testing length:" + repr(len(Y_test)))


# In[9]:


#Feature scaling

from sklearn.preprocessing import RobustScaler as RS
scaler = RS()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[44]:


#Training 

from sklearn.neighbors import KNeighborsClassifier as KNC


classifier = KNC(n_neighbors = 21 )
classifier.fit(X_train,Y_train)



# In[45]:


import pickle 


# In[46]:


#Saving 

filename='model_loc_time_knn.pkl'

pickle.dump(classifier, open(filename, 'wb'))


# In[47]:


#loading the model

filename='model_loc_time_knn.pkl'
model=pickle.load(open(filename, 'rb'))


# In[48]:


#Predictions

Y_pred = model.predict(X_test)


# In[49]:


def res(time,lat,long):
    r=model.predict([[time,lat,long]])
    if r==0:
        print("FCW")
    elif r==1:
        print("HB")
    elif r==2:
        print("HMW")
    elif r==3:
        print("PCW")
    elif r==4:
        print("Stoppage")


res(10,8.180509567,77.418396)


# In[50]:


#Evaluation

from sklearn.metrics import classification_report as cr, confusion_matrix as cm, accuracy_score as acc_s

print("Confusion Matrix : \n", cm(Y_test,Y_pred))
print("\n\nClassification report : \n", cr(Y_test,Y_pred))
print("\n\nAccuracy : ", acc_s(Y_test,Y_pred)*100)


# In[51]:


res(3,8.178689957,77.42429352)


# In[18]:


#Finding suitable k

e=[]

for i in range(1,50):
    knn=KNC(n_neighbors=i)
    knn.fit(X_train,Y_train)
    pred_i=knn.predict(X_test)
    e.append(np.mean(pred_i !=Y_test))
       
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(range(1,50), e,color='red',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=10)
plt.xlabel('k')
plt.ylabel('error')

plt.show()


# In[19]:


#Finding suitable k

e=[]

for i in range(100,150):
    knn=KNC(n_neighbors=i)
    knn.fit(X_train,Y_train)
    pred_i=knn.predict(X_test)
    e.append(np.mean(pred_i !=Y_test))
    
err=np.array(e)
    
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(range(100,150), e,color='red',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=10)
plt.xlabel('k')
plt.ylabel('error')

plt.show()


# In[60]:


#Finding suitable k

e=[]

for i in range(200,250):
    knn=KNC(n_neighbors=i)
    knn.fit(X_train,Y_train)
    pred_i=knn.predict(X_test)
    e.append(np.mean(pred_i !=Y_test))
    
err=np.array(e)
    
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(range(200,250), e,color='red',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=10)
plt.xlabel('k')
plt.ylabel('error')

plt.show()


# In[58]:



print(set(Y_pred))

print(set(Y_test))
print(set(Y_train))


# In[52]:


def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        print (key," : ", value) 
  

  


# In[53]:


CountFrequency(dataset['alarmType_cat']) 


# In[54]:


CountFrequency(dataset['alarmType']) 


# In[55]:


CountFrequency(Y_pred) 


# In[56]:


CountFrequency(Y_test) 


# In[57]:


CountFrequency(Y_train) 


# In[ ]:




