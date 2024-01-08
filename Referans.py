from Sabitler import Sabitler


class Referans:
    sinif_adi = "Referans"

    nokta_listesi = []
    nokta_sayisi = 2

    def __init__(self):
        print(self.sinif_adi + ": Ölçüm için %d nokta tanımlayınız!" % self.nokta_sayisi)
        self.nokta_listesi = []

    def getir_noktalari(self):
        return self.nokta_listesi

    def nokta_ekle(self, nokta):
        if nokta is not None and len(self.nokta_listesi) < self.nokta_sayisi:
            self.nokta_listesi.append(nokta)
            print(self.sinif_adi + ": Nokta eklendi!")
            if len(self.nokta_listesi) == self.nokta_sayisi:
                print(self.sinif_adi + ": Referans tanımlandı!")
                self.hesapla()
            return True
        return False

    def hesapla(self):
        # Hipotenüs kullanılır
        Sabitler.ref_mesafe_px = self.nokta_listesi[0].distance(self.nokta_listesi[1])[2]
        self.sonuc_goster()
        return self

    def sonuc_goster(self):
        print(self.sinif_adi + ": Referans mesafesi pixel: %s" % Sabitler.ref_mesafe_px)
        return self
