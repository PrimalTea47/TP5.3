class Date:
	def __init__(self, jour:int, mois:int, annee:int):
		self.jour = jour
		self.mois = mois
		self.annee = annee
		self.liste_mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

	def __str__(self):
		return f'{self.jour} {liste_mois[self.mois-1]} {self.annee}'

	def __lt__(self, other):
		domicile = f'{self.jour} {self.liste_mois[self.mois-1]} {self.annee}'
		invites = f'{other.jour} {self.liste_mois[other.mois-1]} {other.annee}'
		
		if self.annee < other.annee:
			return f'{domicile} antérieure à {invites}'
		else:
			if self.annee == other.annee and self.mois < other.mois:
				return f'{domicile} antérieure à {invites}'
			else:
				if self.annee == other.annee and self.mois == other.mois and self.jour < other.jour:
					return f'{domicile} antérieure à {invites}'
		
		return f'{domicile} pas antérieure à {invites}'

calendar = Date(17,12,2023)
temps = Date(17,1,2024)
print(temps < calendar)