class Animal:
    def fazer_barulho(self):
        print("Som Generico")

class Cachorro(Animal):
    def fazer_barulho(self):
        print("Au au!!")
class Gato(Animal):
    def fazer_barulho(self):
        print("Miau ")

animais = [Cachorro(), Gato(), Animal()]
for animal in animais:
    animal.fazer_barulho()