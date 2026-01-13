produtos = [{"nome": "Teclado", "preco": 150}, {"nome": "Mouse", "preco": 80}]
produtos_ordenados = sorted(produtos, key=lambda p: p["preco"])
print(produtos_ordenados)

