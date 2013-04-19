#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, sys
import time
import glob
import os.path as path
import getpass
import shutil
import random
import math

username=getpass.getuser()

mypath=os.path.expanduser(os.path.join("~","Dropbox","MacrosDropBox","py","VRD"))
sys.path.append(mypath)

from Fenetre import Fenetre
from Data import Data

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class Controleur(object):

	def __init__(self): 
		self.__projet = ""
		self.__nomboite = ""

		self.__PROJET = 0
		self.__NOM_BOITE = 1
		self.__NUME_BOITE = 2
		self.__GENES = 3
		self.__WELLS = 4		
		self.__CONDS  = 5
		self.__IMAGES = 6

		self.__KEYS = ["Projet", "Nom_Boite", "Num_Boite", "Genes", "Wells", "Condition", "Images"]
		
		self.__dCode = [False,False,False,False,False,False,False]

		self.__dicoDatas = dict()

		self.__dicoEns = dict()

		self.__dicoEnsEnd = dict()
		

	def setData(self, **param) : 
		# tests dict ok...
		#if len(param) <3 : return False
		for v in param.keys() :
			if v in self.__KEYS : continue
			else : return False

		try : param[self.__KEYS[0]]
		except KeyError : return False
		# fin tests -----
		# on rempli un dictionnaire avec les valeur et un code
		for i in range(len(self.__KEYS)) :
			try : param[self.__KEYS[i]]
			except KeyError :
				self.__dCode[i] = False
			else : 
				self.__dicoDatas[i] = param[self.__KEYS[i]]
				self.__dCode[i] = True
		return True

	def __decisionTree(self) :

		# on teste si le projet est toujours le meme :
		if self.__projet != self.__dicoDatas[self.__PROJET] : self.__data = Data(self.__dicoDatas[self.__PROJET])

		#on genere les ensembles par nom de boite si fourni
		if self.__dCode[self.__NOM_BOITE] :

			# les noms de boites et les numeros sont geres par la classe Data :			
			# -1-  l'ensemble pour la valeur fournir a forcement un seul element
			self.__dicoEnsEnd["Nom_Boite"] = set([self.__dicoDatas[self.__NOM_BOITE]])  

			# -2-  on cree l'ensemble des n° de boite:
			templist = self.__data.dicoNumB[self.__dicoDatas[self.__NOM_BOITE]]
			self.__dicoEnsEnd["Num_Boite"] = set(templist)

			# comme on connait la boite on utilise la classe Boite :
			if self.__nomboite!=self.__dicoDatas[self.__NOM_BOITE] : self.__boite = Boite(self.__dicoDatas[self.__NOM_BOITE],  self.__dicoDatas[self.__PROJET])

			# -3-  on cree l'ensemble des genes de la boite:
			self.__dicoEnsEnd["Genes"] = set(self.__boite.genes)

			# -4-  on cree l'ensemble des Wells de la boite:
			values = [v[0] in self.__boite.dicoW.values() if v[1] != "NA"]
			self.__dicoEnsEnd["Wells"] = set(values)

			# -5-  on cree l'ensemble des Conditions de la boite:
			self.__dicoEnsEnd["Condition"] = set(self.__boite.conds)

			# -6-  on cree l'ensemble des images-paths de la boite:
			self.__dicoEnsEnd["Condition"] = set(boite.conds)
			
		return True

if __name__ == "__main__":

	c = Controleur()
	tempdic=dict()
	tempdic["Projet"] = "/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools"
	tempdic["Nom_Boite"] = "20130219_120830_632"
	tempdic["Genes"] = ["123", "456", "789"]
	
	print c.setData(Projet = "/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools", Nom_Boite = "20130219_120830_632", Genes = ["123", "456", "789"], Wells=[1,2,3])
	#print c.setData(Nom_Boite = "20130219_120830_632", Genes = ["123", "456", "789"], Wells=[1,2,3])
	