#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[15]:


af=pd.read_csv(r'C:\Users\Stan\Downloads\alert_data_.csv')

af.replace('null',np.NaN)

af.head(10)


# In[16]:



af['deviceId']=af['deviceId'].astype('category')
af['deviceId_cat']=af['deviceId'].cat.codes

af['alarmType']=af['alarmType'].astype('category')
af['alarmType_cat']=af['alarmType'].cat.codes


# In[17]:


print(set(af["deviceId"]))

print("\n\n")

print("12DF03C6:19636436681228288687  :  3")
print("12DF03C6:19978048393314304687  :  8")
print("12DF03C6:19890203641970688685  :  6")
print("12DF03C6:19317455059550208687  :  0")
print("12DF03C6:19727335125463040688  :  5")
print("12DF03C6:19613968860508160686  :  2")
print("12DF03C6:19523068255842304686  :  1")
print("12DF03C6:19683837391187968688  :  4")
print("12DF03C6:19890368935358464685  :  7")


# In[18]:


#device id density

print("vehicle density")
sns.set(style="darkgrid")
sns.countplot(x="deviceId_cat",data=af)
plt.show()
print("\n")

#alarm type density

print("alarm type density")
sns.countplot(x="alarmType",data=af)
plt.show()
print("\n")

#lat long

print('longitude vs latitude')
plt.scatter(af['longitude'],af['latitude'])
plt.ylabel('latitude')
plt.xlabel('longitude')
plt.show()
print("\n")


# In[19]:


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
  

  


# In[40]:


CountFrequency(af["deviceId"])
print("\n \n Alarmtype vs vehicle id \n")

g = af.groupby(['deviceId','alarmType']).agg('size').reset_index(name='count')

c=pd.DataFrame(g)
print(c)

print("\n \n Alarmtype vs vehicle id \n")

g = af.groupby(['deviceId','alarmType']).agg('size').reset_index(name='count')

c=pd.DataFrame(g)
print(c)
# In[78]:



gr = af.groupby(['deviceId','speed']).agg('size').reset_index(name='count')

cr=pd.DataFrame(gr)
cr.dtypes


# In[82]:



sum=0
s=0
id='12DF03C6:19890203641970688685'
for i in range(len(cr['deviceId'])):
    if(cr['deviceId'][i]==id):
        s=s+1
        sum=sum+cr['speed'][i]


print(sum/s)


# In[88]:


def ind(id):
    for i in range(len(c['deviceId'])):
        if(c['deviceId'][i]==id): 
            return i
        
def res(id):
            i=ind(id)
            #print("Alert summary: \n")
            max=c['count'][i]
            indx=0
            d={}
            sum=0
            s=0
            
            for x in range(len(cr['deviceId'])):
                if(cr['deviceId'][x]==id):
                    s=s+1
                    sum=sum+cr['speed'][x]
            sp_avg=sum/s
            for m in range(i,i+5):
                #print(c['alarmType'][m],c['count'][m])
                d[c['alarmType'][m]]=c['count'][m]
                if(c['count'][m] > max):
                    max=c['count'][m]
                    indx=m
                    
            #print('\nMax occuring alert  :\n ')
            #print(c['alarmType'][indx],max)
            return d, c['alarmType'][indx], max, sp_avg
            
    
res('12DF03C6:19890203641970688685') 


# In[ ]:


import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Vehicle Analysis')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter vehicle id:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

def value ():
    
    x1 = entry1.get()
    a,b,c,d=res(x1)
    
    l=[]
    l.append(b)
    l.append(c)        
    sp= tk.Label(root, text=' ').pack()
    sp= tk.Label(root, text=' ').pack()
    label3 = tk.Label(root, text='Max occuring alert: ').pack()
    label4 = tk.Label(root, text=l).pack()
    sp= tk.Label(root, text=' ').pack()
    label10 = tk.Label(root, text='Average Speed: ').pack()
    label5 = tk.Label(root, text=d).pack()    
        
    sp= tk.Label(root, text=' ').pack()
    label2 = tk.Label(root, text='Alert summary: ').pack()
    label9 = tk.Label(root, text=a).pack()  
  
    
button1 = tk.Button(text='Submit', bg='brown', fg='white',font=('helvetica', 9, 'bold'),command=value).pack()
canvas1.create_window(200, 300, window=button1)

root.mainloop()


# In[ ]:



print("\n \n Alarmtype vs speed \n")
c = pd.pivot_table(af,index=['alarmType','speed'],aggfunc='size')
pd.set_option("display.max_rows",af.shape[0] + 1)
print("\n",c)


# In[ ]:


#alarm type vs speed

print("alarm type vs speed")
plt.scatter(af['alarmType'],af['speed'])
plt.ylabel('speed')
plt.xlabel('alarmType')
plt.show()
print("\n")


# In[ ]:


from pandas.plotting import scatter_matrix
scatter_matrix(af[['deviceId_cat','speed','alarmType_cat','latitude','longitude','recorded_at_time']], figsize=(15,11))


# In[ ]:


plt.show()


# In[ ]:


print("Pearson coeff r")
af.corr(method="pearson")


# In[ ]:


print("Kendall coeff tau")
af.corr(method="kendall")


# In[ ]:


print("spearman coeff p")
af.corr(method="spearman")


# In[ ]:


12DF03C6:19317455059550208687

