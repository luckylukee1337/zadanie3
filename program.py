import random

def zgadnij_liczbe():
    print("Witaj w grze 'Zgadnij liczbę'!")
    print("Komputer losuje liczbę od 1 do 100. Twoje zadanie to odgadnąć tę liczbę.")
    
    # Losowanie liczby
    liczba_do_odgadniecia = random.randint(1, 100)
    
    # Licznik prób
    proby = 0
    while True:
        try:
            # Gracz wprowadza swoją propozycję
            strzal = int(input("Podaj liczbę: "))
            proby += 1
            
            # Sprawdzanie odpowiedzi
            if strzal < liczba_do_odgadniecia:
                print("Za mało! Spróbuj ponownie.")
            elif strzal > liczba_do_odgadniecia:
                print("Za dużo! Spróbuj ponownie.")
            else:
                print(f"Gratulacje! Odgadłeś liczbę {liczba_do_odgadniecia} w {proby} próbach.")
                break
        except ValueError:
            print("Proszę wprowadzić liczbę całkowitą!")

# Uruchomienie gry
zgadnij_liczbe()
