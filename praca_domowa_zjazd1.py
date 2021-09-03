import statistics
while True:
    print('1: Oblicz średnią arytmetyczną')
    print('2: Podnieś do potęgi')
    print('3: Porównaj liczby')
    print('4: Wyjdź')
    decyzja = input('Podaj opcję którą chcesz wybrać: ')

    if decyzja == '1':
        liczba_1 = int(input("Podaj pierwszą liczbę: "))
        liczba_2 = int(input("Podaj drugą liczbę: "))
        liczby = liczba_1, liczba_2
        print('Średnia arytmetyczna liczb wynosi: '+ str((statistics.mean(liczby))))
    if decyzja == '2':
        liczba_1 = int(input("Podaj pierwszą liczbę: "))
        liczba_2 = int(input("Podaj drugą liczbę: "))
        print('Wynik potęgowania to: ' + str((liczba_1 ** liczba_2)))
    elif decyzja == '3':
        liczba_1 = int(input("Podaj pierwszą liczbę: "))
        liczba_2 = int(input("Podaj drugą liczbę: "))
        liczby = liczba_1, liczba_2
    if  liczba_1 > liczba_2:
            print('Większą liczbą jest: ' + str(liczba_1))
    else:
            print('Większą liczbą jest: ' + str(liczba_2))
    if decyzja == '4':
        quit()
