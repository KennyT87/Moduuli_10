import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        matkan_muutos = self.nykyinen_nopeus * tunnit
        self.kuljettu_matka += matkan_muutos

    def __str__(self):
        return (f"{self.rekisteritunnus}\t"
                f"{self.huippunopeus} km/h\t"
                f"{self.nykyinen_nopeus} km/h\t"
                f"{self.kuljettu_matka} km")


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{self.nimi} - Kilpailun tilanne")
        otsikot = ["Rekisteritunnus", "Huippunopeus", "Tämänhetkinen Nopeus", "Kuljettu Matka"]
        print("\t".join(otsikot))
        for auto in self.autot:
            print(auto)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


# Pääohjelma
kilpailun_nimi = "Suuri romuralli"
kilpailun_pituus = 8000
kilpailun_autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
kilpailu = Kilpailu(kilpailun_nimi, kilpailun_pituus, kilpailun_autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
print(f"Kilpailu kesti yhteensä {tunnit} tuntia.")
