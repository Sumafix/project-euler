def SumOfMultiplesOf3or5(number):
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])

print("Ten program ma za zadanie policzyć sumę liczb podzielnych przez 3 lub 5 poniżej wskazanej liczby.")

while True:
    try:
        number = int(input("Podaj liczbę całkowitą większą od 0: "))
        if number <= 0:
            print("Nieprawidłowa wartość!")
            continue
        break
    except:
        print("Nieprawidłowa wartość!")

print("Suma liczb podzielnych przez 3 lub 5 poniżej", number, "wynosi:", SumOfMultiplesOf3or5(number))