class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria):
        self.modelo = modelo
        self.gpu_nome = gpu_nome
        self.gpu = self.GPU(gpu_nome, gpu_memoria)

    def mostrar_configuracao(self):
        print(f'Modelo: {self.modelo}')


    class GPU:
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb
        def mostrar_gpu(self):
            print(f'GPU: {self.nome} - {self.memoria_gb}')

pcOne = Computador('Dell Vostro', 'NVIDIA RTX4090', '24GB')
pcOne.mostrar_configuracao()