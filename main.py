def reversed_guess_game():
    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach! Nie oszukuj :)")
    min = 0
    max = 1000
    i = 0
    while i < 10:
        guess = int((max - min) / 2) + min
        print(f'Zgaduję, że Twoja liczba to: {guess}')
        user_answer = input('Napisz, czy liczba jest: za duża, za mała lub trafiłeś:')
        if user_answer == 'trafiłeś':
            print('Wygrałem! Ha Ha Ha :D')
            return
        elif user_answer == 'za duża':
            max = guess
            i += 1
            continue
        elif user_answer == 'za mała':
            min = guess
            i += 1
        else:
            print("Wpisz dokładnie za duża, za mała lub trafiłeś!")
    print('Oszukujesz kłamco!')


reversed_guess_game()
