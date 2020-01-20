class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, cor):
        self.cor = cor

    def mostrar_cor(self, cor):
        print(cor)


while True:
    obj = Bola(str(input('Cor da Bola: ')), float(input('Circunferência da bola: ')), str(input('Material da Bola: ')))
    trocar = str(input('Deseja trocar a cor da bola? [S / N]: ')).upper()
    print(obj.cor, obj.circunferencia, obj.material)
    if trocar == 'S':
        obj.trocar_cor(str(input('Cor: ')))
    obj.mostrar_cor(f'Nova cor: {obj.cor}')
    continuar = str(input('Deseja continuar? [S / N]: ')).upper()
    if continuar == 'N':
        break
