# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro: # Convenção para nomes de classes: PascalCasing
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        self.ligado = True

    def desliga(self):
        self.ligado = False
        self.velocidade = 0

    def acelera(self):
        if self.ligado:
            self.velocidade += 10

    def desacelera(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10

# Crie uma instância da classe carro.
        
meu_carro = Carro('branco','suv')

# Faça o carro "andar" utilizando os métodos da sua classe.

meu_carro.liga()
meu_carro.acelera()

# Verificar velocidade

print(f'A velocidade atual do carro é: {meu_carro.velocidade} Km/h')

# Faça o carro "parar" utilizando os métodos da sua classe.

meu_carro.desacelera()
meu_carro.desliga()

print(f'A velocidade atual do carro é: {meu_carro.velocidade} Km/h')