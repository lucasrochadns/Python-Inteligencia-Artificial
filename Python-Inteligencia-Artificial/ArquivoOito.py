from encodings import normalize_encoding


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def  apresentar(self):
        print(f"Olá, sou {self.nome} e tenho {self.idade} anos")
    def soma(self, numberOne, numberTwo):
        return numberOne + numberTwo

lucas = Pessoa("Lucas", 30)
lucas.apresentar()
print(lucas.soma(10, 15))