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
	def __init__(self, *filhos, nome=None, idade=35):
		# "__init__" é um 'construtor' e ele permite criar a funcionalidade inicial que sua
		# classe terá !!!
		self.idade = idade
		self.nome = nome
		self.filhos = list(filhos)

	# "self.nome" é
	# "nome" é

	def cumprimentar(self):  # "self" pode ser qualquer palavra, mas em Python sempre usamos
		# a palavra "self" como parametro.
		return f'Olá {id(self)}'


if __name__ == '__main__':
	# sandro = Pessoa('Ordnas')
	"""O objeto complexo 'sandro' é do tipo 'Pessoa'"""
	sandro = Pessoa(nome='Sandro')
	"""O objeto complexo 'sandro' é passado como um atributo para o objeto 'enoque' """
	enoque = Pessoa(sandro, nome='Enoque')
	"""Abaixo nao é a forma usual de se executar um método ("def")."""
	print(Pessoa.cumprimentar(enoque))  # Esta nao é a forma usual de se executar um método ("def").
	"""A forma usual é:
	Ao chamar um "metodo" a partir do "objeto", nao precisa passá-lo como 1º parametro, o Python 
	passa o objeto "p" como 1º parametro implicitamente!!! """
	print(enoque.cumprimentar())  # Ao chamar um "metodo" a partir do "objeto", nao precisa passá-lo
	# como 1º parametro, o Python passa o objeto "p" como 1º parametro implicitamente!!!
	print(id(enoque))  # Checando o "id"
	# print(sandro.nome)
	# sandro.nome = 'Sandro'
	print('Nome do Pai:\n\t', enoque.nome)
	print('Idade do Pai:\n\t', enoque.idade)
	# print(enoque.filhos)
	for filho in enoque.filhos:
		print('Imprimindo os filhos de Enoque:\n\t', filho.nome)

"""Um atributo especial '__dict__' usado para checar todos os atributos de instancia (todoa aqueles criados 
no '__init__' quanto aqueles criatos dinamicamente"""
print('\t', enoque.__dict__)
print('\t', sandro.__dict__)
"""
Criacao
do
'atributo dinamico' 'sobrenome'"""
enoque.sobrenome = 'Passos'
"""
Deletando
o
'atributo dinamico' 'filhos'"""
del enoque.filhos
print('Criado "atrib dinam" "sobrenome", retirado o "atrib dinam" "filhos" em "enoque":\n\t',
	  enoque.__dict__)
print('\t', sandro.__dict__)
