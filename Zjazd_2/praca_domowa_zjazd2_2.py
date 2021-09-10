# Stwórz funkcję nazwaną zbadajTrojkat() która przyjmie jako argumenty długości boków trójkąta.
# Funkcja powinna zwrócić, czy trójkąt jest prostokątny, równoramienny, równoboczny, różnoboczny lub nieprawidłowy
import math
while True:
	def zbadajTrojkat(a, b, c):
			if a + b >= c and b + c >= a and c + a >= b:
				return True
			else:
				return False
	def typ_trojkata(a, b, c):
		if a == b and b == c:
			print('Trójkąt jest równoboczny.')
		elif a == b or b == c or a == c:
			print('Trójkąt jest równoramienny.')
		elif c == math.sqrt(a ** 2 + b ** 2) or b == math.sqrt(a ** 2 + c ** 2) or a == math.sqrt(b ** 2 + c ** 2):
			print('Trójkąt jest prostokątny.')
		else:
			print('Trójkąt jest różnoboczny.')

	bok_a = float(input('Podaj długość boku A: '))
	bok_b = float(input('Podaj długość boku B: '))
	bok_c = float(input('Podaj długość boku C: '))

	if zbadajTrojkat(bok_a, bok_b, bok_c):
		typ_trojkata(bok_a, bok_b, bok_c)
	else:
		print('Z bodanych wartości nie można stworzyć trójkąta.')