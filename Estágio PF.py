# Resolução do problema 9 do Projeto Euler em Python disponível em: https://projecteuler.net/problem=9

"""Definição de uma classe para nós de uma árvore ternária para analisar todos os ternos pitagóricos possíveis recursivamente."""
class Tree:
	def __init__(self,triplet = [], sons = [None, None, None]):
		self.triplet = triplet
		self.sons = sons

"""Definição de uma função recursiva para, ao mesmo tempo criar e buscar a árvore ternária de ternos pitagóricos."""
def search(branch, deepness):
	if deepness == 0:
		if check(branch):
			return True
		else:
			return False
	else:
		branch.sons = breed(branch.triplet)
		for son in branch.sons:
			if search(son, deepness - 1):
				return True
		return False

"""Definição de uma função para checar se o terno pitagórico do nó possui a característica desejada."""
def check(branch):
	a, b, c = branch.triplet[0][0], branch.triplet[1][0], branch.triplet[2][0]
	num = 1000/(a + b + c)
	if float(num).is_integer():
		aux = sorted((a, b, c))
		print(f"({aux[0]*num}, {aux[1]*num}, {aux[2]*num}) é o terno pitagórico cuja soma é 1000.0. Com isso, seu produto é: {a*b*c*pow(num,3)}")
		return True
	else:
		return False

"""Definição de uma função para criar por multiplicação matricial todos os ternos pitagóricos possíveis."""
def breed(triplet):
	son_A_triplet = [[sum(a*b for a,b in zip(A_row,triplet_col)) for triplet_col in zip(*triplet)] for A_row in A]
	son_A = Tree(son_A_triplet)
	son_B_triplet = [[sum(a*b for a,b in zip(B_row,triplet_col)) for triplet_col in zip(*triplet)] for B_row in B]
	son_B = Tree(son_B_triplet)
	son_C_triplet = [[sum(a*b for a,b in zip(C_row,triplet_col)) for triplet_col in zip(*triplet)] for C_row in C]
	son_C = Tree(son_C_triplet)
	return [son_A, son_B, son_C]

"""Matrizes com a propriedade de gerar cada uma dos três ramos da árvore de ternos pitagóricos."""
A = [[1,-2,2],[2,-1,2],[2,-2,3]]
B = [[1,2,2],[2,1,2],[2,2,3]]
C = [[-1,2,2],[-2,1,2],[-2,2,3]]

deepness = 0

trunk = Tree([[3],[4],[5]])

while True:
	if search(trunk, deepness):
		break
	else:
		# print(deepness)
		deepness += 1

# Referências:
# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
# https://www.geogebra.org/classic
# https://www.programiz.com/python-programming/examples/multiply-matrix
# https://www.w3schools.com/python/python_classes.asp
# https://lucid.app
