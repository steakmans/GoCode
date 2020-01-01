#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(
'''
Enoncé :
    Vous êtes responsables des premiers secours dans une zone maritime.Le temps est ensoleillé et vous pensiez pouvoir vous détendre, vous recevez des appels de bateaux  touristique. Ils sont tous tombés en panne moteur pas loin de la côte. Pas de temps à perdre, vous mobilisez votre bateau de secours pour aller secourir et rapatrier les voyageurs. Il peut embarquer jusqu'a 10 personnes(en plus de l'équipe de secours) et ne peut secourir qu'un seul bateau a la fois.
    
Entrées :
    - Un entier compris entre 1  et 100 representant le nombre de bateaux en panne
    
    -Un entier compris entre 0 et 50 correspondant au nombre de voyageurs a secourir dans chaque bateau.
    
Sortie :
    Le nombre de trajets a effectuer par le bateau de secours.
    
Language utilisé : python
Librairie utilisé : numpy
''')
#Les imports
    
import numpy as np
    
#Les entrées

nb_ships = int(input("Veuillez entrer le nombre de bateau en panne dans la zone : (un entier entre 1 et 100) "))

nb_travelers = int(input("Veuillez entrer le nombre de voyageurs sur chaque bateau : (un entier entre 0 et 50) "))

#On détermine le nombre de trajets(en aller retour) par bateau

nb_travels = nb_travelers / 9

#On l'arrondis au supérieur.

nb_travels = np.trunc(nb_travels) + 1

#Maintenant on détermine le nombre de trajets total (en aller retour)

nb_total_travels = nb_travels * nb_ships

#On l'affiche

print("Il faudra donc ", nb_total_travels, " allers retours pour secourir tous le monde")

#On détermine maintenant le nombre de trajets simple (aller simple + retour simple)

nb_total_travels_simple = nb_total_travels * 2

#On l'affiche

print("Et il faudre donc ", nb_total_travels_simple, " trajets simples pour secourir tous le monde.")