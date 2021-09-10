# 1). Stwórz funkcję nazwaną dodajListy() która zwróci nową listę sumując ze sobą elementy na tych samych indeksach.
# Możesz przypuścić, że jako parametry do funkcji podawane są zawsze listy zawierające tylko liczby.
# Jeżeli listy są różnej długości, funkcja powinna wyświetlić napis ‘Podane listy muszą być tej samej długości’

def dodajListy(A, B):
	C = []
	if len(A) == len(B):
		for x, y in zip(A, B):
			C.append(x + y)
		return C
	if len(A) != len(B):
			return "Podane listy muszą być tej samej długości"


if __name__ == "__main__":
		lista_1 = []
		lista_2 = []
		dl_listy_1 = int(input('Podaj liczbę elementów pierwszej listy: '))
		for item in range(dl_listy_1):
			digit = int(input('Podaj liczbę którą chcesz dodać do listy: '))
			lista_1.append(digit)
		dl_listy_2 = int(input('Podaj liczbę elementów drugiej listy: '))
		for item in range(dl_listy_2):
			digit = int(input('Podaj liczbę którą chcesz dodać do listy: '))
			lista_2.append(digit)
		print('Łączna wartość liczb z listy_1 i listy_2 wynosi: ', dodajListy(lista_1, lista_2))

