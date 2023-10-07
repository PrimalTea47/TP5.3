from math import *
class TriangleRect:
	def __init__(self, cote1,cote2):

		self.cotea = cote1
		self.coteb = cote2
		self.hypotenuse = sqrt(self.cotea**2 + self.coteb**2)

	def hypotenu(self):
		return self.hypotenuse

mon_triangle = TriangleRect(3,4)

# print(mon_triangle.cotea)
# print(mon_triangle.coteb)
# print(mon_triangle.hypotenu())

class Player:
	def __init__(self):
		self.energie = 3
		self.alive = True

	def blessure(self):
		if self.alive:
			self.energie -= 1
			if self.energie == 0:
				self.alive = False
		return self.energie, self.alive

	def soin(self):
		if self.alive:
			self.energie += 1
		return self.energie, self.alive

mario = Player()
# print(mario.blessure())
# print(mario.blessure())
# print(mario.soin())






class Chrono:
	def __init__(self,heures,minutes,secondes):
		self.heures = heures
		self.minutes = minutes
		self.secondes = secondes

	def affiche(self):
		return f"Il est {self.heures} heures, {self.minutes} minutes, {self.secondes} secondes."

	def avance(self,s):
		self.secondes += s
		while self.secondes > 59:
			self.secondes -= 60
			self.minutes += 1
			while self.minutes > 59:
				self.minutes -= 60
				self.heures += 1
		return f'Temps avancé de {s} secondes...'


temps = Chrono(12,59,57)
# print(temps.affiche())
# print(temps.avance(55555))
# print(temps.affiche())











class Satellite:
	def __init__(self, nom, masse, vitesse):
		self.masse = masse
		self.nom = nom
		self.vitesse = vitesse

	def impulsion(self, force, duree):
		self.force = force
		self.duree = duree
		self.vitesse = self.force * self.duree / self.masse
	
	def affiche_vitesse(self):
		return f"Vitesse du satellite {self.nom} = {self.vitesse} m/s"

	def energie(self):
		return (self.masse * self.vitesse**2)/2

s1 = Satellite("Léandre",250,10)
print(s1.impulsion(500,15))
print(s1.affiche_vitesse())
print(s1.energie())