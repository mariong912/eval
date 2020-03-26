# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:14:39 2020

@author: Marion
"""
# A partir de la création d'une fonction qui permet de vréer des polynomes de n'importe quels degrés (simulation)
# On intégre ces valeurs à un dictionnaires à partir des données (résultats de la fontion) de 2 listes
# Ensuite on cherche à regarder les 2 séries pour enfin les représenter graphiquements
"""
def poly(L,val):

    s=0

    for deg,coef in enumerate(L):

        s=s+ coef*val**deg

    return (s)

rep ="non"

while rep!="oui":

    polynome = []

    degre=int(input("Donne le degré : "))

    for i in range(degre+1):

        polynome.append(float(input("donne le coef ")))

    val_x=float(input("Donnez votre valeur "))

    print(" P(x) = ", poly(polynome, val_x))

    rep=input("voulez-vous continuez ? ")

# On cherche à créer 2 listes des résultats des fonctions polunomiales simulées précédemment
    
for i in 5:
    l1=[]
    l1.append(poly(polynome, val_x)) 

for j in 5:
    l2=[]
    l2.append(poly(polynome, val_x)) 
# l1 = [57, 23, 101, 819, 242]
# l2 = [91, 11, 9, 126, 746]

"""

d = {'serie1' : [57, 23, 101, 819, 242],
     'serie2' : [91, 11, 9, 126, 746]}

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.DataFrame(d) 
print(df)

# df['serie']+=10
# df['serie']*=2
print(df)


print("Voici les moyennes par lignes")
seriemoyl=df.mean(1) # calcul de la moyenne par ligne
print(seriemoyl)


print("Voici les moyennes par série(colonnes)")
seriemoyc=df.mean() # calcul de la moyenne par colonne)
print(seriemoyc)


print("Voici les sommes cumulees")
df_cs = df.apply(np.cumsum) # Faire une somme cumulée
print(df_cs)

x = df['serie1']; 
y = df['serie2'] 
xm = sum(df['serie1'])/len(df['serie1'])
ym = sum(df['serie2'])/len(df['serie2'])

# On cherche à representer graphiquement les 2 series du dictionnaires
plt.plot(x) 
plt.plot(y)
# En ajoutant la moyenne de chacune de ces séries qui est calculé au dessus mais également dans la moyenne par serie/colonne
plt.axhline(xm, color="blue")
plt.axhline(ym, color="orange")
plt.show()
