inicio = int(input("Entre com o valor inicial: "))
fim = int(input("Entre com o valor final  : "))
final = fim + 1
num = inicio
fizz = int(input("Entre com o valor do Fizz: "))
buzz = int(input("Entre com o valor de Buzz: "))
print("\nContando FizzBuzz (Fizz = {} e Buzz = {}) no intervalo de {} até {}.\n".format(fizz,
																						buzz, inicio, fim))

for num in range(inicio, final):


	def fizzbuzz(num):
		if (num % fizz == 0) and (num % buzz == 0):
			return "FizzBuzz"
		elif num % fizz == 0:
			return "Fizz"
		elif num % buzz == 0:
			return "Buzz"
		return num


	print(fizzbuzz(num))
