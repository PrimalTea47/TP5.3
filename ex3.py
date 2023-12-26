class Chrono:
	def __init__(self, heures:int, minutes:int, secondes:int):
		self.heures = heures
		self.minutes = minutes
		self.secondes = secondes

	def affiche(self):
		return f'Il est {self.heures} heures, {self.minutes} minutes et {self.secondes} secondes.'

	def avance(self, s:int):
		self.secondes += s
		#réorganier les secondes
		while self.secondes >= 60:
			self.secondes -= 60
			self.minutes += 1

		#idem pour les minutes
		while self.minutes >= 60:
			self.minutes -= 60
			self.heures += 1

		#pas d'attribut jour donc on ne réorganise pas les heures


temps = Chrono(3,45,30)
print(temps.affiche())

temps.avance(5000)
print(temps.affiche())