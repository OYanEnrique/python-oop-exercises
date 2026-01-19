# Fazendo Bolinhos

class Bolo:
	"""
	Classe para representar um bolo com ingredientes básicos.

	Para fazer um bolo, é necessário ter farinha, ovo e leite.
	Se algum desses ingredientes estiver faltando, o bolo não pode ser feito.
	"""
	def __init__(self, nome="", farinha=True, ovo=True, leite=True):
		self.nome = nome
		self.farinha = farinha
		self.ovo = ovo
		self.leite = leite
		
	def __str__(self): 
		return f"Fazendo bolo {self.nome}!" if self.farinha and self.ovo and self.leite else f"Não pode fazer {self.nome}, ingredientes faltando!"
		
	def __getstate__(self):
		return f"Nome: {self.nome}, Farinha: {self.farinha}, Ovo: {self.ovo}, Leite: {self.leite}"
			
bolinho = Bolo("Red Velvet", False, True, True)
print(bolinho)
cupcake = Bolo("Cupcake", True, True, True)
print(cupcake)
print(bolinho.__doc__)
print(cupcake.__getstate__())
