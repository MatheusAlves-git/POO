from classe import Caneta

c1 = Caneta('Bic Cristal', 'Azul', 0.5, 80, True)
c1.rabiscar('alguma coisa')
c1.rabiscar('alguma coisa')
c1.parar_rabiscar()
c1.parar_rabiscar()
c1.rabiscar('alguma coisa')

print(f'A cor da caneta é {c1.cor}')
