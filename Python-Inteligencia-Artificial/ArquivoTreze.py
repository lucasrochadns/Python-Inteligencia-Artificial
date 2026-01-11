class Veiculo:
    def __init__(self, marca):
        self.marca = marca
    def ligar(self):
        print(f"{self.marca} está ligado")


class Carro(Veiculo):
    def buzinar(self):
        print("BI BI BI !!!")


class CarroEletrico(Carro):
    def __init__(self, marca, bateria):
        super().__init__(marca)
        self.bateria = bateria



carroEletrico = CarroEletrico("TESLA", "ION LITIO")
carroEletrico.buzinar();