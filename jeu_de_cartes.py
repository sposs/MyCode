#!/usr/bin/python
  
import os
from random  import randrange

class Joueur(object) :
	def __init__(self) :
		self.compte = 0
		self.partieGagnee = 0
	def creerJeuDeCartes(self) :
		return self JeuDeCartes()

class JeuDeCartes(object) :
	def __init__(self) : 
		self.listCartes = []
		couleur = ("Pique","Trefle","Coeur","Carreau")
		valeurs = (2,3,4,5,6,7,8,9,10,"valet","dame","roi","as")
		for elt in self.listCartes :
			for val,coul in valeurs,couleur :
				self.listCartes.append((val,coul))
	def nomCartes(self,(val,coul)) :
		return "{0} de {1}".format(val,coul)
	def battre(self) :
		t = len(self.listCartes)
		for elt in range(t)
			c1,c2 = randrange(t), randrange(t)
			self.listCartes[c1], self.listCartes[c2] = self.listCartes[c2], self.listCartes[c1]
	def tirer(self) :
		print "carte tirée = {0} ".format(self.nomCartes(self.listCartes[0]))
		del self.listCartes[0]
