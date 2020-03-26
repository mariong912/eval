# controle
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:30:31 2020

@author: Marion

"""


# Question 1 :

def sup21(x):
    """
    >>> sup21(21)
    True
    >>> sup21(2)
    False
    """
    return x>=21


# Question 2 :

def pairs(x):
    """
    >>> pairs([1,2,3])
    [2]
    """
    return [i for i in x if i%2==0]


# Question 3 :

def ajout4(x):
    """
    >>> ajout4([])
    [4]
    >>> ajout4([1,2,4])
    [1, 2, 4, 4]
    >>> l = [1,2,3]
    >>> _ = ajout4(l)
    >>> l
    [1, 2, 3]
    """
    return x+[4]


# Question 4 :
    
def to_strings(x):
    """
    >>> to_strings({1:2})
    ['1:2']
    >>> to_strings({})
    []
    >>> to_strings({1:2,3:4})
    ['1:2', '3:4']
    """
    return [str(i)+":"+str(j) for i,j in zip(x.keys(),x.values())]


# Question 5

def extremites(x):
    """
    >>> extremites(['a', 'b', 'c', 'd', 'e'])
    ['a', 'b', 'd', 'e']
    """
    return x[0:2]+x[-2:]


# Question 6 :

class Mot:
    """
    >>> mot = Mot('Bonjour')
    >>> mot.mot
    'Bonjour'
    >>> mot.comptelettre('o')
    2
    >>> mot.comptelettre('B') == mot.comptelettre('b') == 1
    True
    """
    def __init__(self, mot):
        self.mot = mot

    def comptelettre(self, caract):
        return self.mot.count(caract.lower())+ self.mot.count(caract.upper())
        

# Question 7 : 



def tri_et_inverse(x) :
    """
    >>> maliste = [4,7,6]
    >>> tri_et_inverse(maliste)
    ([4, 6, 7], [6, 7, 4])
    >>> maliste == [4,7,6]
    True
    """
    return (list.sort(x),list.reverse(x))

"""

# Question 8 :

def aller_a_paris(input_call=input):
    saisie = input_call('Question ')
    if saisie not in  ??? # en fonction de saisie on continue a demander ou on renvoie 'Paris'
    valeurs = float(input("Entrez 'paris'"))
        registre_valeurs[saisie] = valeurs.split("Paris")# Au lieu d'utiliser input comme en cours vous appelez input_call
    # par dÃ©faut elle vaut input donc vous pouvez appeller
    # aller_a_paris() pour tester a la main
    while True:
        return 0, 'Nulle Part'
      
 """       
        
        
if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)
        
        

