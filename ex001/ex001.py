# Fazendo Bolinhos

class Bolo:
	def __init__(self):
		self.nome ="bolo"
		self.farinha = False
		self.ovo = False
		self.leite = False
		
	def fazerBolo(self):
		return f"Fazendo bolo {self.nome}!" if self.farinha and self.ovo and self.leite else f"Não pode fazer {self.nome}, ingredientes faltando!" 
			
bolinho = Bolo()
bolinho.nome="Red Velvet"
bolinho.farinha = True
bolinho.ovo = True
bolinho.leite = True
print(bolinho.fazerBolo())

cupcake = Bolo()
cupcake.nome = "Cupcake"
print(cupcake.fazerBolo())

