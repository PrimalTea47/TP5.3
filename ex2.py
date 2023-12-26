class Player:
	def __init__(self):
		self.energie = 3
		self.alive = True


	def blessure(self):
		if self.alive:
			self.energie -= 1
		
		#vérifier si le joueur est mort
		if self.energie == 0:
			self.alive = False

	def soin(self):
		if self.alive:
			self.energie += 1

	def __str__(self):
		status = 'en vie' if self.alive else 'mort'
		return f"Le joueur a {self.energie} point d'énergie et est {status}."

Mario = Player()
print(Mario)
Mario.blessure()
Mario.blessure()
print('2 blessures ==>',Mario)
Mario.soin()
print('1 soin ==>',Mario)
Mario.blessure()
Mario.blessure()
Mario.blessure()
print('3 blessures ==>',Mario)
Mario.soin()
print('1 soin ==>',Mario)