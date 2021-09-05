#sposob z zajec
import random

def rzut_moneta():
    return random.choice([0,1])

def rzut_moneta_n_razy(n):
    current_streak, longest_streak, poprzedni_rzut = 0, 0, 0
    for i in range(n):
        wynik_rzutu = rzut_moneta()
        print(f'Poprzedni rzut: {poprzedni_rzut}')
        print(f'wynik_rzutu: {wynik_rzutu}')
        print(f'Current streak: {current_streak}')
        print(f'Longest streak: {longest_streak}')
        print(10 * '*')
        if wynik_rzutu == 1 and poprzedni_rzut == 1:
            poprzedni_rzut = 1
            current_streak += 1
            longest_streak = max(current_streak, longest_streak)
        elif wynik_rzutu == 1:
            poprzedni_rzut = 1
            current_streak += 1
        else:
            longest_streak = max(current_streak, longest_streak)
            current_streak = 0
            poprzedni_rzut = 0

rzut_moneta_n_razy(10)
        
#sposob po optymalizacji
import random
def rzuc_moneta():
    return random.choice([0,1])
def policz_orly(n):
    current_run, longest_run = 0
    orzel_w_poprzednim_rzucie = None
    for i in range(n):
        #Python traktuje liczbe 1 jako True, liczbe 0 jako False
        wypadl_orzel = rzuc_moneta()
        if wypadl_orzel and (orzel_w_poprzednim_rzucie or orzel_w_poprzednim_rzucie is None):
            # Pytanie: dlaczego jest orzel_w_poprzednim_rzucie is None?
            # Odpowiedz: Bo przed rozpoczeciem rzucania moneta, nie mozemy zdefiniowac czym byl poprzedni rzut.
            # Jest to wspomniany na zajeciach 'warunek startowy'
            current_run += 1
        else:
            longest_run = max(longest_run, current_run)
            current_run = 0
        orzel_w_poprzednim_rzucie = wypadl_orzel
    return longest_run
