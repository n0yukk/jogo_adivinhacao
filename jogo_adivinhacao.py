import random

numCerto = random.randint(0, 100)
print(numCerto)
numEscolhido = int(input("Adivinhe um numero de 0 a 200:"))


if numEscolhido == numCerto:
	print("Parabens, O numero correto era ", numCerto, " !")

while numEscolhido != numCerto:

	numEscolhido = int(input("Numero errado, tente novamente!"))

	if numEscolhido == numCerto:
		print("Parabens, O numero correto era",numCerto,"!")

