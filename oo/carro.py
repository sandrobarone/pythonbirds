"""

Criar uma classe carro que deve possuir:
2 atributos compostos por 2 classes.

1) Motor
2) Direcao

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
a) Atributo de dado informando a "velocidade"
b) Metodo "acelerar" que deverá incrementar a velocidadde em 1 unidade.
c) Método "frear" que deverá decrementar a velocidade em 2 unidades.

A direcao terá a responsabilidade de controlar a direcao. Ela oferece os seguintes atributos:
a) Valor de direcao com os seguintes valores possiveis: Norte, Sul, Leste, Oeste.
b) Metodo girar a Direita.
c) Metodo girar a Esquerda.

    N
  O   L
    S

Exemplo:

>>> # Testando motor

>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

>>> # Testando Diirecao

>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'

>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro = acerelar()
>>> carro.calcular_velocidade()
1
>>> carro = acerelar()
>>> carro.calcular_velocidade()
2
>>> carro = frear()
>>> carro.calcular_velocidade()
0

>>> carro.calcular.direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular.direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular.direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular.direcao()
'Oeste'


"""


class Motor():
	def __init__(self):
		self.velocidade = 0

	pass
