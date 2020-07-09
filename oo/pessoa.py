"""
Classe:
	Classes devem comecar com a Letra Maiuscula (camel case : ExemploPessoa)
	É a base da OO.
	É a fôrma (fôrma de gelo) que define como nossos objetos se comportam. As vezes é utilizado
como sinonimo de "tipo".

Funcao:
	Funcoes devem comecar com a letra minuscula (snake_case : exemplo_pessoa)

def: (Metodo)
	É o 1º atributo das Classes
	É uma funcao que pertence a uma classe. Sempre conectada a um objeto.
	Deve sempre declarar o 1º parametro que será o objeto a ser recebido ("self" ou qualquer
outro nome, mas no Python usam a palavra "self")
"""


class Pessoa:
	def __init__(self, nome=None, idade=35):
		# "__init__" é um 'construtor' e ele permite criar a funcionalidade inicial que sua
		# classe terá !!!
		self.idade = idade
		self.nome = nome

	# "self.nome" é
	# "nome" é

	def cumprimentar(self):  # "self" pode ser qualquer palavra, mas em Python sempre usamos
		# a palavra "self" como parametro.
		return f'Olá {id(self)}'


if __name__ == '__main__':
	p = Pessoa('Ordnas')
	"""Abaixo nao é a forma usual de se executar um método ("def")."""
	print(Pessoa.cumprimentar(p))  # Esta nao é a forma usual de se executar um método ("def").
	"""A forma usual é:
	Ao chamar um "metodo" a partir do "objeto", nao precisa passá-lo como 1º parametro, o Python 
	passa o objeto "p" como 1º parametro implicitamente!!! """
	print(p.cumprimentar())  # Ao chamar um "metodo" a partir do "objeto", nao precisa passá-lo
	# como 1º parametro, o Python passa o objeto "p" como 1º parametro implicitamente!!!
	print(id(p))  # Checando o "id"
	print(p.nome)
	p.nome = 'Sandro'
	print(p.nome)
	print(p.idade)
