class Satellite:
	def __init__(self, nom:str, masse = 100, vitesse = 0):
		self.nom = nom
		self.masse = masse
		self.vitesse = vitesse

	def impulsion(self, force, duree):
		self.vitesse += force * duree / self.masse

	def affiche_vitesse(self):
		print(f'Satellite "{self.nom}" : {self.vitesse} m/s')

	def energie(self):
		cinetique = (self.masse * self.vitesse**2)/2
		return cinetique

s1 = Satellite("Léandre", masse=250, vitesse=10)
s1.impulsion(500,15)
s1.affiche_vitesse()
print(s1.energie())
s1.impulsion(500,15)
s1.affiche_vitesse()
print(s1.energie())