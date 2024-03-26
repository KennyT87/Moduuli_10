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


# Testi
h = Hissi(1, 10)

while True:
    kerros = int(input("Anna haluttu kerros (1-10): "))
    if kerros == 1:
        print(f"Hissi on jo alimmassa kerroksessa.")
        break

    if 2 <= kerros <= 10:
        print(f"Hissi on tulossa.")
        h.siirry_kerrokseen(kerros)
        print(f"Hissi on perillä!")
        break

    else:
        print(f"Talossa ei ole kerrosta {kerros}.")

