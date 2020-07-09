def teste(v, i):
	valor = v
	incremento = i
	resultado = valor + incremento
	return resultado


""" imprimindo 'a' passando os atributos '(10, 1)' """
a = teste(10, 1)
print("\n")
print(a)

"""
.............CLASSES E METODOS.............
Como se escrreve:
    'def didatica_tech'   # letras minusculas e underline se necessario
    'class DidaticaTech'  # primeira letra maiuscula SEM underline
    uma 'class' pode ter varias 'def'
    'def' dentro de 'class' PRECISA TER A PALAVRA reservada 'self'
"""


class DidaticaTech:
	def incrementa(self, v, i):
		valor = v
		incremento = i
		resultado = valor + incremento
		return resultado


""" instanciando a CLASSE na VARIAVEL 'a' """
a = DidaticaTech()
""" toda FUNCAO dentro de uma CLASSE é chamado de METODO
    chamando o METODO 'incrementa' da CLASSE 'DidaticaTech' """
b = a.incrementa(10, 1)
print("\n")
print(b)

"""
.............PARA ACESSAR A VARIAVEL DENTRO DO METODO DA CLASSE.............
    'self' permite instanciar a variavel dentro do METODO para ser usada fora.
"""


class DidaticaTech:
	def incrementa(self, v, i):
		self.valor = v
		self.incremento = i
		self.resultado = self.valor + self.incremento
		return self.resultado


a = DidaticaTech()
b = a.incrementa(10, 1)
print("\n")
print(b)
print(a.valor)

"""
.............PARA ACESSAR A VARIAVEL DENTRO DO METODO DA CLASSE.............
    '__init__' METODO CONSTRUTOR (funcao dentro da CLASSE) usado para inicializar variaveis.
    '__init__' permite instanciar os valores de 'v' e 'í' direto da CLASSE 'DidaticaTech'.
        a = DidaticaTech(10, 1)

"""


class DidaticaTech:
	def __init__(self, v: int, i: int):
		self.valor = v
		self.incremento = i

	def incrementa(self):
		self.valor = self.valor + self.incremento


a = DidaticaTech(10, 1)
b = a.incrementa()
print('\n.....self.....')
print(a.valor)
b = a.incrementa()
print(a.valor)
b = a.incrementa()
print(a.valor)

"""
.............PARA ACESSAR A VARIAVEL DENTRO DO METODO DA CLASSE com valores
pre-definidos no CONSTRUTOR.............
    '__init__' METODO CONSTRUTOR (funcao dentro da CLASSE) usado para inicializar variaveis.
    '__init__' permite instanciar os valores de 'v' e 'í' direto da CLASSE 'DidaticaTech'.
        a = DidaticaTech()

    Depois de instanciarmos 'a = DidaticaTech()', quando executamos 'a.incrementa(), o que a IDE
    está fazendo é:
        'DidaticaTech().incrementa(a, 10, 1)'
"""


class DidaticaTech:
	def __init__(self, v=10, i=1):
		self.valor = v
		self.incremento = i

	def incrementa(self):
		self.valor = self.valor + self.incremento


a = DidaticaTech()
b = a.incrementa()
print('\n.....self pré definido no CONSTRUTOR.....')
print(a.valor)
b = a.incrementa()
print(a.valor)
b = a.incrementa()
print(a.valor)
b = a.incrementa()
print(a.valor)

"""
.............FUNCAO chama FUNCAO dentro da CLASSE.............
	'__init__' METODO CONSTRUTOR (funcao dentro da CLASSE) usado para inicializar variaveis.
	'__init__' permite instanciar os valores de 'v' e 'í' direto da CLASSE 'DidaticaTech'.
	Exemplo:
		a = DidaticaTech()

	Depois de instanciarmos 'a = DidaticaTech()', quando executamos 'a.incrementa(), o que a IDE
	está fazendo é:
		'DidaticaTech().incrementa(a, 10, 1)'
        
	Uma FUNCAO pode chamar outra FUNCAO dentro da CLASSE.
		Exemplo:
			def incrementa_quadrado(self):
				self.incrementa()
				self.exponencial(2)
"""


class DidaticaTech:
	def __init__(self, v=10, i=1):
		self.valor = v
		self.incremento = i
		self.valor_exponencial = v

	def incrementa(self):
		self.valor = self.valor + self.incremento

	def verifica(self):
		if self.valor > 12:
			print("Ultrapassou 12")
		else:
			print("Nao Ultrapassou 12")

	def exponencial(self, e):  # '(self, e)' indica que o METODO 'exponencial' tem um
		# PARAMETRO/VALOR 'e' que deve ser passado ao ser chamado.
		self.valor_exponencial = self.valor**e

	def incrementa_quadrado(self):
		self.incrementa()
		self.exponencial(2)


a = DidaticaTech()
b = a.incrementa()
print('\n.....self --> FUNCAO chama FUNCAO dentro da CLASSE.....')
print(a.valor)
print(a.verifica())
b = a.incrementa()
print(a.valor)
print(a.verifica())
b = a.incrementa()
print(a.valor)
print(a.verifica())
b = a.incrementa()
print(a.valor)

c = a.exponencial(3)
print(a.valor_exponencial, '= a.valor_exponencial')
c = a.incrementa_quadrado()
print(a.valor, '= a.valor')
print(a.valor_exponencial, '= valor_exponencial\n')

"""
.............HERANÇA.............
	Uma CLASSE criada HERDA tudo de uma classe já existente.
		Exemplo:
			class Calculos(DidaticaTech):
"""

print('.............HERANÇA.............')


class Calculos(DidaticaTech):
	pass


c = Calculos()
c.incrementa()
print(c.valor, '= c.valor')
print(c.valor_exponencial, '= c.valor_exponencial')

"""
.............HERANÇA.............
	Uma CLASSE criada HERDA tudo de uma classe já existente.
		class Calculos(DidaticaTech):
	Herdo uma CLASSE ja existente, para nao ter que fazer novamente e acrescento o que preciso nela.
	Exemplo:
		class Calculos(DidaticaTech):
			def decrementa(self):
				self.valor = self.valor - self.incremento
	
"""


class Calculos(DidaticaTech):
	def decrementa(self):
		self.valor = self.valor - self.incremento


c = Calculos()
c.incrementa()
print(c.valor, '= c.valor')
c.decrementa()
print(c.valor, '= c.valor apos rodar o "c.decrementa"')

"""
.............HERANÇA.............
	Acrescentando atributos ao metodo '__init__' fará com que o metodo '__init__'anterior deixe de existir 
	e passe a ter apenas os atributos do atual criado. Assim alguns metodos HERDADOS podem parar de 
	funcionar.
	Para que eu HERDE tb todo o '__init__' da CLASSE mãe eu uso o comando 'super' e posso alterar o valor 
	dos atributos se quiser.
	Exemplo:
		super().__init__(v=10, i=5)		

"""


class Calculos(DidaticaTech):
	def __init__(self, d=5):
		super().__init__(v=10, i=5)
		self.divisor = d

	def decrementa(self):
		self.valor = self.valor - self.incremento

	def divide(self):
		self.valor = self.valor / self.divisor


c = Calculos()
c.incrementa()
print(c.valor,
	  '= "c.valor" de "c.incrementa()" apos criar outro "__init__" e adicionar a ele o "__init__" da CLASSE '
	  'mãe')
c.decrementa()
print(c.valor,
	  '= "c.valor" de "c.decrementa()" apos criar outro "__init__" e adicionar a ele o "__init__" da CLASSE '
	  'mãe')
c.divide()
print(c.valor,
	  '= "c.valor" de "c.divide()" apos criar outro "__init__" e adicionar a ele o "__init__" da CLASSE mãe')
