class Restauracja:
    def __init__(self, nazwa, miasto, kuchnia, ocena, liczba_osob_ktore_pomiesci):
        self.nazwa = nazwa
        self.miasto = miasto
        self.kuchnia = kuchnia
        self.menu = {}
        self.ocena = ocena
        self.liczba_osob_ktore_pomiesci = liczba_osob_ktore_pomiesci

    def __str__(self):
        return self.nazwa + ' ' + self.miasto + ' ' + self.kuchnia + ' ' + self.wlasciciel + ' ' + str(self.ocena) + ' ' + str(self.liczba_osob_ktore_pomiesci)
    
    def podaj_podstawowe_informacje(self):
        print('Restauracja ' + self.nazwa + ' znajduje się w mieście ' + self.miasto + ' i jej specjalnością jest kuchnia ' + self.kuchnia)

    def dodaj_pozycje_do_menu(self, danie, cena):
        self.menu[danie] = cena

    def wyswietl_menu(self):
        if self.menu:
            for danie, cena in self.menu.items():
                print("{}: {}".format(danie, cena))
        else:
            print("Menu jest puste")

    def czy_restauracja_jest_w_moim_miescie(self, moje_miasto):
        if self.miasto == moje_miasto:
            print("Restauracja znajduje się w Twoim mieście")
        else:
            print("Niestety, restauracja nie znajduje się w Twoim mieście")

    def czy_restaurcja_jest_ok(self):
        if self.ocena < 3.5:
            print("Lepiej poszukaj czegoś innego")
        elif self.ocena < 4.0:
            print("Restauracja nie nalezy do zbyt dobrych")
        elif self.ocena < 4.5:
            print("Restauracja jest ok")
        elif self.ocena < 5.0:
            print("Jest to bardzo dobra restauracja")
        elif self.ocena == 5.0:
            print("Jest to wyśmienita rstauracja")
        
    def czy_restauracja_zmiesci_moja_impreze(self, liczba_uczestnikow_imprezy):
        if self.liczba_osob_ktore_pomiesci >= liczba_uczestnikow_imprezy:
            print("Twoi goście zmieszczą się w tej restauracji")
        else:
            print("Niestety Twoi goście nie zmieszczą się w tej restauracji")


    
restauracja_uGosi = Restauracja("u Gosi", "Poznań", "polska", 4.0, 70)
restauracja_uMarka = Restauracja("u Marka", "Gdynia", "włoska", 4.7, 20)
restauracja_podlukami = Restauracja("pod Łukami", "Warszawa", "amerykańska", 5.0, 100)
restauracja_uGosi.podaj_podstawowe_informacje()

restauracja_uGosi.dodaj_pozycje_do_menu("Pierogi", 18)
restauracja_uGosi.dodaj_pozycje_do_menu("Schabowy", 25)
restauracja_uGosi.dodaj_pozycje_do_menu("Rosół", 12)
restauracja_uGosi.wyswietl_menu()
restauracja_uMarka.wyswietl_menu()

restauracja_podlukami.czy_restauracja_jest_w_moim_miescie("Warszawa")
restauracja_podlukami.czy_restauracja_jest_w_moim_miescie("Poznań")
restauracja_uGosi.czy_restaurcja_jest_ok()
restauracja_podlukami.czy_restaurcja_jest_ok()
restauracja_uMarka.czy_restauracja_zmiesci_moja_impreze(60)
restauracja_podlukami.czy_restauracja_zmiesci_moja_impreze(60)

