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
		# self.__dCode liste de tuples, val 1 = present/absent val 2 = liste/valeur unique
		# self.__dCode[0] = projet
		# self.__dCode[1] = nom de boite
		# self.__dCode[2] = numero de boite
		# self.__dCode[3] = Genes
		# self.__dCode[4] = Wells
		# self.__dCode[5] = Images

		self.__PROJET = 0
		self.__NOM_BOITE = 1
		self.__NUME_BOITE = 2
		self.__GENES = 3
		self.__WELLS = 4		
		self.__IMAGES = 5
		self.__CONDS = 6

		self.__KEYS = ["Projet", "Nom_Boite", "Num_Boite", "Genes", "Wells", "Images", "Condition"]
		
		self.__dCode = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

		self.__dicoDatas = dict()

	def setData(self, **param) : 
		# tests dict ok...

		if len(param) <3 : return False
		
		for v in param.keys() :
			if v in self.__KEYS : continue
			else : return False

		try : param[self.__KEYS[0]]
		except KeyError : return False
		
		for i in range(len(self.__KEYS)) :
			try : param[self.__KEYS[i]]
			except KeyError :
				self.__dCode[i] = (0,False)
			else : 
				self.__dicoDatas[i] = param[self.__KEYS[i]]
				isarray = len(param[self.__KEYS[i]]) >1
				self.__dCode[i] = (1,isarray)
		return True

	def __decisionTree(self) :

		if self.__projet != self.__dicoDatas[self.__PROJET] : self.__data = Data(self.__dicoDatas[self.__PROJET])

		if self.__dCode[self.__NOM_BOITE] == 0 :
			if self.__dCode[self.__NUME_BOITE] + self.__dCode[self.__GENES] + self.__dCode[self.__CONDS] + self.__dCode[self._IMAGES]] == 0 : return False
			if self.__dCode[self.__NUME_BOITE]

if __name__ == "__main__":

	c = Controleur()
	tempdic=dict()
	tempdic["Projet"] = "/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools"
	tempdic["Nom_Boite"] = "20130219_120830_632"
	tempdic["Genes"] = ["123", "456", "789"]
	
	#print c.setData(Projet = "/Users/lisalamasse/Dropbox/Macros_Lisa/ProjetVRD_Tools", Nom_Boite = "20130219_120830_632", Genes = ["123", "456", "789"], Wells=[1,2,3])
	print c.setData(Nom_Boite = "20130219_120830_632", Genes = ["123", "456", "789"], Wells=[1,2,3])
	