from math import gcd, sqrt
from statistics import mean

# Suma numerelor de la 1 la 100
def _1():
    print(f'1. Suma numerelor de la 1 la 100 este: {sum(range(1,101))}')
# _1()

# Afisarea primelor 20 de numere impare
def _2():
    odd_numbers = []
    i = 1
    while(len(odd_numbers) < 20):
        if i % 2 == 1:
            odd_numbers.append(i)
        i+=1
    print(f'2. Primele 20 numere impare sunt: {odd_numbers}')
# _2()

# Cel mai mare divizor comun pentru 2 numere citite de la tastatura
def _3():
    a = int(input('Dati primul numar: '))
    b = int(input('Dati al doilea numar: '))
    print(f'Cel mai mare divizor comun dintre {a} si {b} este {gcd(a, b)}')
# _3()

# Afisati daca un numar citit de la tastatura este prim
def _4():
    a = int(input('Dati un numar: '))
    if a > 1:
        for i in range(2, (a//2)+1):
            if a % i == 0:
                print(f'{a} nu este un numar prim!')
                break
        else:
            print(f'{a} este un numar prim!')
    else:
        print(f'{a} nu este un numar prim!')
# _4()

# Afisati suma si media unei liste de numere citite de la tastatura
def _5():
    input_list = []
    n = int(input('Dati numarul de elemente: '))
    if n <= 0:
        print('Numar de elemente invalid')
        return
    for i in range(n):
        input_list.append(int(input(f'Introduceti elementul pentru pozitia {i}: ')))
    print(f'Suma listei este {sum(input_list)} si media este {mean(input_list)}!')
# _5()

# Se citesc 3 numere de la tastatura, verificati daca acestea pot reprezenta unghiurile unui triunghi
def _6():
    a = int(input('Dati primul numar: '))
    b = int(input('Dati al doilea numar: '))
    c = int(input('Dati al treilea numar: '))

    print(f'{a}, {b}, {c} {"" if (a + b > c) and (a + c > b) and (b + c > a) else "nu "}pot forma un triunghi!')
# _6()

# Sortati o lista de elemente citite de la tastatura, folosind orice metoda de sortare doriti (nu functia sort)
def _7():
    input_list = []
    n = int(input('Dati numarul de elemente: '))
    if n <= 0:
        print('Numar de elemente invalid')
        return
    for i in range(n):
        input_list.append(int(input(f'Introduceti elementul pentru pozitia {i}: ')))
    
    count = [0] * n
    sorted = [0] * n
    for i in range(n-1):
        for j in range(i+1, n):
            if input_list[i] > input_list[j]:
                count[i]+=1
            else:
                count[j]+=1
    
    for i in range(n):
        sorted[count[i]] = input_list[i]
    print(f'Lista sortata: {sorted}')
# _7()

# Scrieti un program care afiseaza ziua saptamanii pentru un numar citit de la tastatura (de la 1 la 7) unde  1=luni , 7 = duminica
def _8():
    n = int(input('Dati un numar: '))
    if n < 1 or n > 7:
        print('Numar invalid!')
        return
    week_days = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica']
    print(f'Ziua este {week_days[n - 1]}!')
# _8()

# Afisati maximul dintr-un vector de elemente citit de la tastatura
def _9():
    input_list = []
    n = int(input('Dati numarul de elemente: '))
    if n <= 0:
        print('Numar de elemente invalid')
        return
    for i in range(n):
        input_list.append(int(input(f'Introduceti elementul pentru pozitia {i}: ')))
    print(f'Numarul maxim din lista este {max(input_list)}!')
# _9()

# Rezolvati ecuatia de gradul al doilea
def _10():
    a = int(input('Dati a: '))
    b = int(input('Dati b: '))
    c = int(input('Dati c: '))
    
    delta = b**2 - 4 * a * c
    
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f'Solutiile ecuatiei sunt: x1 = {x1}, x2 = {x2}!')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'Solutia ecuatiei este: x = {x}!')
    else:
        print('Ecuatia nu are solutii reale!')
# _10()