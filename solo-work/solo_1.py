# zadanie 1.1
hello = "Hello"
student = "Ola"
# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("{} {}".format(hello, student))


# zadanie 1.2
student = input("Wpisz swoje imie")
print(f"Hello {student}")


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
