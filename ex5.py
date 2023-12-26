class CompteBancaire:
	def __init__(self, nom, idclient,solde=0):
		self.nom = nom
		self.solde = solde
		self.idclient = idclient

	def depot(self, somme):
		self.solde += somme

	def retrait(self, somme):
		self.solde -= somme

	def __str__(self):
		return f'{self.nom} : {self.solde} €'


banquier = CompteBancaire("Léandre", 47, 600)
banquier.retrait(700)
banquier.depot(205)
print(banquier)