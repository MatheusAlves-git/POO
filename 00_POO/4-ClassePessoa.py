from datetime import datetime
ano_atual = datetime.now().date()


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhercer(self):
        nova_idade = int(input('Nova idade: '))
        self.crescer(nova_idade)

    def engordar(self):
        pass

    def emagrecer(self):
        pass

    def crescer(self, idade_atual):
        idade_atual = self.envelhercer()
        if self.idade < 21:
            if idade_atual > self.idade:
                self.altura = self.altura + 0.5
            elif idade_atual < self.idade:
                self.altura = self.altura - 0.5
        elif self.idade >= 21:
            print('Altura permanece a mesma!')


individuo = Pessoa(str(input('Nome: ')), int(input('Idade: ')), float(input('Peso: ')), float(input('Altura: ')))
print(individuo.altura)
individuo.envelhercer()
print(individuo.altura)