# controle
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:30:31 2020

@author: Marion

"""


# Question 1 :

def sup21(chiffre):
    chiffre
    if chiffre >= 21 :
            print("True")
    else :
            print("False")
sup21(21)


# Question 2 :

def pairs (liste1):
    for i in len(liste1) :
        i=liste1[i]%2
        if i==0: 
            liste2 += liste1[i]
        else : 
            liste2

pairs([1,2,3])


# Question 3 :


def ajout4(liste):
    liste.append(4)
    print(liste)
    

ajout4([1,2])


# Question 4 :

    
def to_strings(dico):
    l=[]
    for i,j in dico.items():
        l+=[i,':',j]
    print(l)
    
    
to_strings({1:2,3:4})


# Question 5



def extremites(liste1):
    liste1
    liste2 = []
    k= len(liste1)
    j = k-2
    for i in 2 :
        liste2 += liste1[i]
    for j in k : 
        liste2 += liste1[j]
    liste2
    
extremites(['a', 'b', 'c', 'd', 'e'])
        

# Question 6 :



class Mot :
    mot=''
    def comptelettre(self,carat,mot):
        x = mot.upper()
        counter = 0
        for carat1 in x:
            if carat1 == 'carat' :
                counter += + 1
        print(counter)
        # ou 
        # list(mot.split())
        # if 'carat' in len(list):
        #     counter +=1
        

# Question 7 : 



def tri_et_inverse(liste1) :
    liste2 = []
    liste3 = []
    liste2.append(liste1.sort())
    liste3.append(reversed(liste1))
    liste = liste2 + liste3
    liste

tri_et_inverse([4,7,6])



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
      
if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)
        
        

