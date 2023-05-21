# zadanie 1.1
hello = "Hello"
student = "Ola"
# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("{} {}".format(hello, student))


# zadanie 1.2
# student = input("Wpisz swoje imie")
# print(f"Hello {student}")


#zadanie 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print(f"Liczba studentow wynosi: {liczba_studentow}")


#zadanie 1.4
studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for i in studenci:
  print(f"Hello {i}")


#zadanie 1.5
liczba = 3
potega = 4

wynik = liczba ** potega

print("Wynik wynosi: ", wynik)


#zadanie 1.6
# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))


#zadanie 1.7
# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda x: x.split()[0])
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)



#zadanie 1.8
# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda x: x.split()[-1])
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)



#zadanie 1.9
# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
nazwsika_na_N= [1 if student.split()[-1].startswith("N") else 0 for student in studenci ]
liczba_n = sum(nazwsika_na_N)
print("Liczba studentow na N wynosi: ", liczba_n)


#zadanie 1.10
# zadanie 1.10

# zmienne poniezej preprezentuja ulozenie punktow na wykresie,
# do zadania dolaczono takze rysunek pomocniczy
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

def funkcja_liniowa(wykres):
    roznice = [
        [wykres[i+1][1] - wykres[i][1], wykres[i+1][0] - wykres[i][0]]
               for i in range(len(wykres)-1)]
    return all(x == roznice[0] for x in roznice)

wykres_1_funkcja_liniowa = funkcja_liniowa(wykres_1)
wykres_2_funkcja_liniowa = funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = funkcja_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")

# oczekiwany rezultat:
# Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.
