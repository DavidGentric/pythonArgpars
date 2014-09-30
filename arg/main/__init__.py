#!/usr/bin/python3
#-*-coding: utf-8-*-

import argparse
from locale import str


'''création logger '''
import logging
logging.basicConfig(filename="mon_fichier_de_log.log")





'''Arguments positionnels'''
from argparse import Namespace
parser = argparse.ArgumentParser()


parser.add_argument("duree_playlist", help="duree de la playlist en minutes", type=int)
parser.add_argument("type_playlist", help="Format de sortie de la playlist", choices=["m3u","xspf","pls"])
parser.add_argument("nom_playlist", help="Nom du fichier de la playlist")
parser.add_argument("--g", help="genre de musique voulue '", nargs=2)
parser.add_argument("--ar", help="artiste voulu ", nargs=2)
parser.add_argument("--alb", help="album voulue", nargs=2)
parser.add_argument("--t", help="titre voulue", nargs=2)
parser.add_argument("--marge", help="marge supplementaire a ajoute a la duree", type=int)
parser.add_argument("--sg", help="sous genre possible")
args = parser.parse_args()

'''Fonction qui permet de verifier si l'utilisateur a bien saisie un entier pour une quantite voulue'''
def verificationInt (quantity):
    if quantity >=0 and quantity<=100:
        logging.info("la quantite est bien un entier compris entre 0 et 100")
        try:
            return int(quantity)
            logging.info("la quantite est de "+quantity)
        except ValueError:
            print("Erreur de conversion")
            exit(2)
            logging.error("la quantite n'ai pas convenable elle ne correspond ma a 100<x<0")


'''Fonction qui permet la verification de tout les quantites de chaque arguments saisies'''
def verification ():

    Attributs=('g','ar','sg','alb','t')
    pourcentage=0
    for arg in Attributs:
        Argu=getattr(args, arg)
        if Argu is not None:
            argVerif=verificationInt(Argu[1])
            setattr(args,arg,argVerif)
            pourcentage+=argVerif
            print(pourcentage)
verification()