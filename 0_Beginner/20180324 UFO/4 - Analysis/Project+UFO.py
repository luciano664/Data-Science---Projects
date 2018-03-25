
# coding: utf-8

# ## UFO Project

# This project will analyze the occurrences of appearance UFO in USA, the idea is extract valuable information that could help in future analysis.

# In[2]:


#importing libraries
import pandas as pd
import numpy  as np
import datetime


# In[3]:


#reading CSV file
oldCsvFile = 'C:\\Git\\Data_Science_Projects\\0_Beginner\\20180324 UFO\\2 - Updated Data\\ufo.csv'
newCsvFile = 'C:\\Git\\Data_Science_Projects\\0_Beginner\\20180324 UFO\\3 - Upload Data\\ufo.csv'
ufoDataFrame = pd.read_csv(oldCsvFile)


# In[4]:


#figuring out dataframe shape
ufoDataFrame.shape


# In[5]:


#identifying the columns names
ufoDataFrame.columns


# In[6]:


#rename columns removing spaces " "
ufoDataFrame.columns = ['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time']


# In[7]:


#new columns name
ufoDataFrame.columns


# In[8]:


#saving new CSV modified
ufoDataFrame.to_csv(newCsvFile, index=False)


# In[9]:


#verifying index
ufoDataFrame.index


# In[10]:


#analyzing the first rows
ufoDataFrame.head(20)


# In[11]:


#analyzing the last rows
ufoDataFrame.tail(20)


# In[12]:


#verifying original dtypes
ufoDataFrame.dtypes


# In[13]:


#converting Time to DateTime
ufoDataFrame.Time = pd.to_datetime(ufoDataFrame.Time)


# In[14]:


#verifying new dtypes
ufoDataFrame.dtypes


# In[15]:


ufoDataFrame.head()


# In[16]:


#saving new CSV modified
ufoDataFrame.to_csv(newCsvFile, index=False)


# In[17]:


#verifying what kind of value could be ignored
ufoDataFrame.count()


# In[18]:


#removing just only 25 records when city was empty, this 25 records is less than 1% and do not affect the analysis
ufoDataFrame.dropna(subset=['City'],how='any',inplace=True)


# In[19]:


#verifying what kind of value could be ignored
ufoDataFrame.count()


# In[20]:


#saving new CSV modified
ufoDataFrame.to_csv(newCsvFile, index=False)


# # Important points to identify in this file
# <ol>
# <li>Period of information</li>
# <li>Frequency of occurrences, monthly, yearly, by city</li>
# <li>UFO's shape</li>
# <li>Main cities and state with more occurences</li>
# <li>Main time of occurences</li>
# <li>UFO's color</li>
# </ol>

# In[21]:


#listing the first records before sort by
ufoDataFrame.head(5)


# In[22]:


#listing the last records before sort by
ufoDataFrame.tail(5)


# In[23]:


#ordering dataframe by Time in ASCEDING
ufoDataFrame.sort_values(['City'])


# In[24]:


#listing the first records after sort by
ufoDataFrame.head(5)


# In[25]:


#listing the last records after sort by
ufoDataFrame.tail(5)


# In[26]:


#access to the date of the first event
initialDate = ufoDataFrame.Time.min()


# In[27]:


#access to the date of the last event
lastDate = ufoDataFrame.Time.max()


# In[28]:


days = lastDate - initialDate


# In[29]:


qd = abs(days.days)

a=qd/360; 
m=(qd % 360)/ 30;
d=(qd % 360)% 30;
print("%d ano(s) %d mese(s) e %d dia(s) "%(a,m,d))


# # 1-Period of information: 
# We have 18.216 records between 1930 and 2000, it is more than 71 years of data

# In[30]:


#create new column Year
tempList = []
for fYear in ufoDataFrame.Time:
    tempList.append(fYear.year)

ufoDataFrame['Year'] = tempList


# In[31]:


ufoDataFrame.head()


# In[32]:


#create new column Month
tempList = []
for fYear in ufoDataFrame.Time:
    tempList.append(fYear.month)

ufoDataFrame['Month'] = tempList


# In[33]:


ufoDataFrame.head()


# In[34]:


#create new column day
tempList = []
for fYear in ufoDataFrame.Time:
    tempList.append(fYear.day)

ufoDataFrame['Day'] = tempList


# In[35]:


ufoDataFrame.head()


# In[36]:


#create new column hour
tempList = []
for fYear in ufoDataFrame.Time:
    tempList.append(fYear.hour)

ufoDataFrame['Hour'] = tempList


# In[37]:


ufoDataFrame.head()


# In[38]:


#saving new CSV modified
ufoDataFrame.to_csv(newCsvFile, index=False)


# In[39]:


#identify number of occurences yearly
ufoDataFrame.groupby(['Year']).count()['City'].sort_values(ascending=False)


# In[40]:


ufoYear = ufoDataFrame.groupby(['Year']).count()['City'].sort_values(ascending=False)


# # 2 - Frequency of occurrences, yearly, by city and monthly: 
# 

# In[41]:


get_ipython().magic('matplotlib inline')
ufoYear.plot.line().set_title('Appearances per year')


# In[42]:


#identify top 15 cities
ufoCity = ufoDataFrame.groupby(['City']).count()['State'].sort_values(ascending=False)


# In[43]:


ufoCity.head(15)


# In[44]:


ufoCity[0:15].plot.bar().set_title('Top 15 cities')


# In[45]:


#identifies the month with the highest number of apparitions
ufoCity = ufoDataFrame.groupby(['Month']).count()['State'].sort_index()


# In[46]:


ufoCity


# In[47]:


ufoCity.plot.area().set_title('Appearances per month')


# # 3 - UFO's shape
# 

# In[48]:


ufoShape = ufoDataFrame.groupby(['Shape_Reported']).count()['State']


# In[49]:


ufoShape.sort_values(ascending=False).plot.bar().set_title("UFO's shape")


# # 4 - Main cities and state with more occurences

# In[50]:


ufoState = ufoDataFrame.groupby(['State','City']).count()['Year'].sort_values(ascending=False)


# In[51]:


ufoState.head(15)


# In[52]:


ufoState[0:15].plot.bar()


# # 4 - Main time of occurences

# In[55]:


ufoHour = ufoDataFrame.groupby(['Hour']).count()['Year'].sort_index()


# In[56]:


ufoHour


# In[72]:


ufoHour.plot.line().set_title('Most common time for apparitions')


# # 5 - UFO's color

# In[73]:


ufoDataFrame.head()


# In[78]:


ufoColor = ufoDataFrame.groupby(['Colors_Reported']).count()['Year'].sort_values(ascending=False)


# In[83]:


ufoColor[0:15]


# In[84]:


ufoColor[0:15].plot.bar()


# In[89]:


ufoColor = ufoDataFrame.groupby(['Colors_Reported','Shape_Reported']).count()['Year'].sort_values(ascending=False)


# In[94]:


ufoColor[0:15].plot.bar().set_title("UFO's color + shape")

