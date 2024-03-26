
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissi_numero, kohde_kerros):
        if hissi_numero < 1 or hissi_numero > len(self.hissit):
            print(f"Talossa ei ole hissiä numero {hissi_numero}.")
        else:
            print(f"Hissi numero {hissi_numero} on tulossa.")
            self.hissit[hissi_numero - 1].siirry_kerrokseen(kohde_kerros)
            print(f"Hissi numero {hissi_numero} on perillä!")

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit ajetaan pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)
        print("Kaikki hissit ovat nyt pohjakerroksessa.")


# Pääohjelma
talo = Talo(1, 10, 3)

while True:
    hissi_numero = int(input("Anna hissin numero (1-3): "))
    kerros = int(input("Anna haluttu kerros (1-10): "))
    if kerros == 1:
        print(f"Hissi on jo alimmassa kerroksessa.")
        break

    if 2 <= kerros <= 10:
        talo.aja_hissia(hissi_numero, kerros)
        break

    else:
        print(f"Talossa ei ole kerrosta {kerros}.")

talo.palohalytys()