from math import sqrt

class TriangleRect:
	def __init__(self, cote1:int, cote2:int):
		self.cote1 = cote1
		self.cote2 = cote2
		self.hypotenuse = sqrt(cote1**2 + cote2**2)


geometrie = TriangleRect(3,4)

print(geometrie.hypotenuse)