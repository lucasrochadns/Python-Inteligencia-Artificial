class Pato:
    def fazer_som(self):
        print("Quack")

class Pessoa:
    def fazer_som(self):
        print("Olá!")
def emitir_som(obj):
    obj.fazer_som()

emitir_som(Pessoa())
emitir_som(Pato())
