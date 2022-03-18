# Functions

def test_function():
    print("Ez a function meg lett hívva!")


def osszeadas(szam1, szam2):
    eredmeny = szam1 + szam2
    print(str(eredmeny))


test_function()
osszeadas(15, 20)


# Osztályok és Metódusok


class Auto:
    def __init__(self, evjarat, marka, uzemanyag):
        self.evjarat = evjarat
        self.marka = marka
        self.uzemanyag = uzemanyag

    def autokiiras(self):
        print("Az auto evjarata: " + str(self.evjarat) + "\n" +
              "Az auto markaja: " + self.marka + "\n" +
              "Az auto uzemanyaga: " + self.uzemanyag)


auto1 = Auto(2005, "Ford", "dízel")

auto1.autokiiras()

# Adattípusok

lista = list(("alma", "banán", "körte"))
lista_alt = ["alma", "banán", "körte"]

rendezett_veges_lista = tuple(("alma", "banán", "körte"))
rendezett_veges_lista_alt = ("alma", "banán", "körte")

szotar = dict(nev="Dani", kor=21)
szotar_alt = {"nev": "Neve",
              "kor": 21}

terjedelem = range(10)

halmaz = {"alma", "banán", "körte"}
