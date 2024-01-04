# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:17:20 2023

@author: KMEYERS
"""

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Read in data
df = pd.read_csv(r"C:/Users/kmeyers/OneDrive - Environmental Protection Agency (EPA)/Profile/Documents/ORISE/Forecast/forecast.csv") 

print(df.head())
#%%
df['class'].value_counts()

#%%
pv = df.groupby(['class', 'week']).size().reset_index().pivot(columns='class', index='week', values=0)
#This gives a stacked bar chart with all data 
#counts.plot(kind='bar', stacked=True)
print(pv.head())
#Reshape the pivot table for easier calculation 
#data_pv = pv.unstack().unstack('class')

pv.plot(legend=True, xlabel="week", ylabel="class")
plt.ylim(top = 2500, bottom = 0)

pv.plot(use_index = True)

TP = data_pv['TP']
FP = data_pv['FP']

plt.stackplot(weeks, TP, FP, data = data_pv, 
              colors =['r', 'c'])
plt.ylabel('counts')


#%%
counts = df.groupby(['class', 'week']).size().reset_index(name = 'counts')
print(counts.head())

sns.set(font_scale = 1.25)
L = sns.lineplot(
    data = counts, 
    x = 'week',  y = 'counts', hue = 'class', 
    palette = "crest" )

#L.set_axis_labels("Week", "Counts", labelpad = 10)
L.legend.set_title("Class")
L.figure.set_size_inches(7, 5)
L.ax.margins(.15)
L.despine(trim=True)

#counts.drop(columns='week').plot(kind='area', stacked=True)

#%%

#%%
# Create new dfs that are a subset of df where ex. 'class' == 'FN'
sub = df[df['class'] == 'FN']
subFP = df[df['class'] == 'FP']
subTN = df[df['class'] == 'TN']
subTP = df[df['class'] == 'TP']

print(sub.head())

#This is the initial way I tried to do this and I feel like im doing it wrong or it's inefficient 
#val = ['TN']
#TN = df[df["class"].isin(val)]
#%%
sub_plot = sub.groupby(['class', 'week']).size().reset_index().pivot(columns='class', index='week', values=0)
print(sub_plot.head())

sub_plot.plot(kind='bar', stacked=True)
plt.xticks(rotation = 300)

sub_plot.plot()
plt.xticks(rotation = 300)

#%%
#create four dfs with the counts of each class sorted by weeks 
FN = sub.groupby(['class', 'week']).size().reset_index().pivot(columns='class', index='week', values=0)
FP = subFP.groupby(['class', 'week']).size().reset_index().pivot(columns='class', index='week', values=0)
TN = subTN.groupby(['class', 'week']).size().reset_index().pivot(columns='class', index='week', values=0)
TP = subTP.groupby(['class', 'week']).size().reset_index().pivot(columns='class', index='week', values=0)

#load created dfs into a list, then merge files using the reduce function
#To keep values that belong to the same date merge it om the 'week'
classes = [FN, FP, TP]
from functools import reduce
classes_merged = reduce(lambda  left,right: pd.merge(left,right,on=['week'], how='outer'), classes)

classes_merged.plot(legend=True, xlabel="week", ylabel="class")
#%%
sub_plot.plot()
FP.plot()
TN.plot()
TP.plot()
plt.xticks(rotation = 300)


#%%
val = ['TN']
TN = df[df["class"].isin(val)]

