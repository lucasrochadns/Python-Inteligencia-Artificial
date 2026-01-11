frutas = ["Banana", "Pera", "Uva"]
frutas.append("abacate")

for x in frutas:
    print(x)
frutas.remove("Uva")
print(frutas)

pessoa = {"nome": "Lucas", "idade": 30}
pessoa.update({"nome": "Pedro", "idade": 60})

for chave, valor in pessoa.items():
    print(chave, valor)
for texto in pessoa.values():
    print(texto)