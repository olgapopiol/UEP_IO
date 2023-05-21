class Student:
    def __init__(self, imie, nazwisko, nr_albumu):
        self.imie_studenta = imie
        self.nazwisko = nazwisko #nazwisko po slef. nie jestem tym samym co parametr nazwisko
        self.numer_albumu = nr_albumu
        self.indeks = []


    def __str__(self):
        return self.imie_studenta + ' ' + self.nazwisko + ' ' + str(self.numer_albumu)
    
    def dodaj_ocene(self, ocena):
        self.indeks.append(ocena)

    def oblicz_srednia_ocen(self):
        if self.indeks:
            srednia = sum(self.indeks) / len(self.indeks)
        else:
            srednia = 0
        print(srednia)



student_olga = Student("Olga", "Popiół", 123123)
student_olga.dodaj_ocene(5.0)
student_olga.dodaj_ocene(4.0)
student_olga.dodaj_ocene(5.0)
student_olga.dodaj_ocene(3.5)
student_olga.oblicz_srednia_ocen()

