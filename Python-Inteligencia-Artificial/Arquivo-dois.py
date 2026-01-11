numero = int(input("digite numero"))
if numero % 2 != 0:
    print(numero, "IMPAR")
else:
    print(numero, "PAR")

idade = 50

if idade > 20 and idade < 31:
    print("1", idade)
elif idade > 30 and idade < 60:
    print("2", idade)
else:
    print("teste")

frutas = ["banana","morango","uva"]
frutas.append("pera")

print(frutas)