# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:14:39 2020

@author: Marion
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

d = {'A' : [14.5, 14., 16., 12.],     
     'B' : [11., 12., 16., 18.]} 
df = pd.DataFrame(d) 
print(df)

# df['A']+=10
# df['B']*=2
print(df)

serie1=df.mean(1) # calcul de la moyenne par ligne
serie2=df.mean() # calcul de la moyenne par colonne)

print(serie1)
print(serie2)

df_cs = df.apply(np.cumsum) # Faire une somme cumulée
print(df_cs)

x = df['A']; 
y = df['B'] 
xm = sum(df['A'])/len(df['A'])
ym = sum(df['B'])/len(df['B'])
print(xm,ym)
plt.plot(x) 
plt.plot(y)

plt.show()