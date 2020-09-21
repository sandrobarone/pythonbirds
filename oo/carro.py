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

>>> # Testando Direcao

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
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0

>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'


"""


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


"""
Quando há constantes em Python, a convencao da PEP8 diz:
Todos os caracteres em caixa alta (com "underline' se necessario) e os valores nunca devem ser trocados.
Caixa Alta = "CTRL SHIFT U"
"""
NORTE = "Norte"
SUL = "Sul"
LESTE = "Leste"
OESTE = "Oeste"


class Direcao(object):

    rotacao_a_direita_dct = {
        NORTE: LESTE,
        LESTE: SUL,
        SUL: OESTE,
        OESTE: NORTE,
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE,
        OESTE: SUL,
        SUL: LESTE,
        LESTE: NORTE,
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        """
        As linhas abaixo pode ser substituida pela definicao do dicionario acima (rotacao_a_direita_dct)
        mais a unica linha logo abaixo deste comentario.

        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        """
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        # Preciso controlar que a velocidade minima possivel seja ZERO
        self.velocidade = max(0, self.velocidade)
        """
        Assim a velocidade será igual ao valor máximo entre "0" e o valor da velocidade atual "self.velocidade".
        Se por acaso tiver um valor negativo na velocidade atual "self.velocidade", ZERO será maior que 
        este valor e retornará "0".
        Se por acaso tiver um valor positivo na velocidade atual "self.velocidade", ZERO será menor que 
        este valor e retornará "self.velocidade".
        """
