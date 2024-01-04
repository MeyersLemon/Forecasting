"""
Created on Fri Nov  3 10:37:57 2023

@author: KMEYERS
"""

#%%
# Import libraries
import pandas as pd

# Read in your dataframe
df = pd.read_csv(r"C:/Users/kmeyers/OneDrive - Environmental Protection Agency (EPA)/Profile/Documents/ORISE/Forecast/forecast.csv") 

#%%
# Check initial counts of each value in 'class'
df['class'].value_counts()

#%%
"This section determines consecutive weeks of a class"

# Create new column, 'consecutive', that groups 'class' by whether or not (!=) it's the same as value in next row,
# then cumulatively sums those groups and uses transform to add that value to each cell of the group so the new col is same size as the df
df['consecutive'] = df['class'].groupby((df['class'] != df['class'].shift()).cumsum()).transform('size')

print(df.head())

#%%
# Create new dfs that are a subset of df where ex. 'class' == 'FN'
sub = df[df['class'] == 'FN']

print(sub.head())

#%%
# Create two lists: 'leng' is the length of the event, and occ is the number of occurences 
    #occurences will be inflated because of the transform('size), repeating the length of event in every row
occ = list(sub['consecutive'].value_counts())
leng = list(sub['consecutive'].value_counts().index)

#%%
# iterate through length of occ/leng, normalizing occ to size of group (leng), save to new list occ_norm
occ_norm = []
for x,y in zip(occ,leng):
    occ_norm.append(int(x/y))
   
#%%
#create a new df 
leng=pd.Series(leng, name="lenth of FN")
occ_norm=pd.Series(occ_norm, name="occ")

FN=pd.concat([leng, occ_norm], axis=1)

# Print length of FN occurrences
print(FN)

#%%
#Make a barplot to display new data 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

fig, ax = plt.subplots(figsize = (8, 6))
sns.barplot(data = FN, x = leng, y = occ_norm, hue = occ_norm)
ax.bar_label(ax.containers[0])
plt.xlabel('Length of False Negatives (weeks)')

#label the counts on the bar chart
ax.bar_label(ax.containers[0], rotation = 290)

#%%
time = sub['time']
week = sub['week']
cons = sub['consecutive']
occFN = list(sub['class'].value_counts())

fig, ax = plt.subplots(figsize = (8, 6))
sns.scatterplot(data = sub, x = week, y = cons)





