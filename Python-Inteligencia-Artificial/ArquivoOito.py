from encodings import normalize_encoding


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, sou {self.nome} e tenho {self.idade} anos")

lucas = Pessoa("Lucas", 30)
lucas.apresentar()