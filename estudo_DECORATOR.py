"""
........................DECORATOR - CONCEITO 1........................
	Utilizado para alterar o comportamento de uma "FUNCAO" sem alterar o codigo da funcao internamente,
facilitando o reuso do codigo.
	Muito utilizado no "Django" para testar login do user.
"""

""" 
	Criando DECORATOR UPPERCASE para alterar todas as FUNCOES (caso haja) e evitar erros.
"""

print("\n........................DECORATOR - CONCEITO 1........................\n")


class uppercase(object):
	def __init__(self, funcao):
		self.funcao = funcao

	def __call__(self, *args):
		self.funcao(args[0].upper())


"""
	Para executar/utilizar o DECORATOR precisamos preceder o nome do DECORATOR pelo caracter "@" no inicio 
	da nossa FUNCAO.
"""


@uppercase
def nome(nome):
	print("Nome: %s\n\n" % nome)


"""O decorator irá substituir esta linha abaixo."""
# print("Nome: %s" % nome.upper())


nome("Sandro")

print("Outro estudo de DECORATOR usando uma FUNCAO de divisao caso haja divisao por ZERO !\n")


def check(func):
	def inside(a, b):
		if b == 0:
			print("Nao posso dividir por ZERO !")
			return
		func(a, b)

	return inside


@check
def div(a, b):
	return a / b


print(div(10, 0))

"""

........................DECORATOR - CONCEITO 2........................

	É uma FUNCAO que tem outra FUNCAO como ARGUMENTO e retorna outra FUNCAO como Valor Retornável.
	É uma FUNCAo de ALTO NIVEL que opera outra FUNCAO.
	É sempre representada atraves da linha "@my_decorator" em cima de uma FUNCAO "def".



Exemplo:
3 funcoes (a, b, c):
Onde a funcao "a" recebe a funcao "b" como parametro para devolver como resposta a funcao "c".
 	
		def funcao_a_decorador(funcao_b):
			def funcao_c_interna():
				# código da funcao c interna
			return funcao_c_interna	
	
"""

print("\n........................DECORATOR - CONCEITO 2........................\n")


def soma():
	print(15 + 20)


def subtracao():
	print(30 - 10)


soma()

subtracao()

"""
Vamos acrescentar funcoes adicionais comuns a todas ou algumas das funcoes acima ("soma" e "subtracao") 
usando "decoradores".

"""

print(
		"\nVamos acrescentar funcoes adicionais comuns a todas ou algumas das funcoes acima (soma e "
		"divisao) usando 'decoradores'.")


def funcao_decoradora(funcao_parametro):
	def funcao_interior(*args, **kwargs):  # "*args" é o mesmo que escrever "num1 + num2 + ..."
		# Acoes adicionais que acrescentam (decoram).
		print("Vamos realizar um cálculo: ")
		funcao_parametro(*args, **kwargs)
		# Acoes adicionais que acrescentam (decoram).
		print("Terminamos o cálculo!")

	return funcao_interior


@funcao_decoradora
def soma(num1, num2, num3):
	print(num1 + num2 + num3)


def subtracao(num1, num2):
	print(num1 - num2)


def multiplicacao(num1, num2):
	print(num1 * num2)


@funcao_decoradora
def divisao(num1, num2):
	print(num1 / num2)


@funcao_decoradora
def potencia(base, exponente):
	print(pow(base, exponente))


soma(7, 5, 8)
subtracao(7, 5)
multiplicacao(7, 5)
divisao(7, 5)
potencia(5, 3)
