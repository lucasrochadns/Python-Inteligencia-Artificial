
idade = 20
ano = 2026
altura = 1.75
mensagem = "Teste tipos de variaveis"
frutas = ["banana","maça","pera"]
pessoa = {"nome" : "Lucas ", "idade": 20}

for x in frutas:
    print(x)
for i in range(20):
    print(i)
for letra in "lucas":
    print(letra)
for chave in pessoa:
    print(chave)
for chaves in pessoa.values():
    print(chaves)
for chavess, valor in pessoa.items():
    print(chavess, valor)

for i in range(3):
    for j in range(2):
        print(i, j)

quadrados = [x * x for x in range(5)]
print(quadrados)

frutass = ["maçã", "banana", "uva"]

for indice, frut in enumerate(frutass):
    print(indice, frut)



contador = 0

while contador < 5:
    print(contador)
    contador += 1

x = 0

while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

while True:
    comando = input("Digite 'sair' para parar: ")
    if comando == "sair":
        break

