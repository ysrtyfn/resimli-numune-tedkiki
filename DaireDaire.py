from Aletler import Aletler
from Sabitler import Sabitler

from Nokta import Nokta


class DaireDaire:
    sinif_adi = "DaireDaire"

    aletler = Aletler()

    cv2 = None
    image = None
    nokta_listesi = []
    nokta_sayisi = 6
    hesap_sonuclari = ()  # (dx, dy, math.hypot(dx, dy))

    def __init__(self, cv2, image):
        print(self.sinif_adi + ": Ölçüm için %d nokta tanımlayınız!" % self.nokta_sayisi)
        print(self.sinif_adi + ": İlk 3 nokta 1. daire için sonraki 3 nokta 2. daire için kullanılacaktır.")
        self.nokta_listesi = []
        self.cv2 = cv2
        self.image = image

    def nokta_ekle(self, nokta):
        if nokta is not None and len(self.nokta_listesi) < self.nokta_sayisi:
            self.nokta_listesi.append(nokta)
            print(self.sinif_adi + ": Nokta eklendi!")
            if len(self.nokta_listesi) == self.nokta_sayisi:
                print(self.sinif_adi + ": Noktalar tanımlandı!")
                self.hesapla()
            return True
        return False

    def hesapla(self):
        daire_1_noktalari = self.nokta_listesi[0:3]
        daire_2_noktalari = self.nokta_listesi[3:]

        daire_1 = self.aletler.define_circle(self.cv2, self.image, daire_1_noktalari)
        daire_2 = self.aletler.define_circle(self.cv2, self.image, daire_2_noktalari)

        daire_1_merkez = Nokta(daire_1.X, daire_1.Y)
        daire_2_merkez = Nokta(daire_2.X, daire_2.Y)

        self.hesap_sonuclari = daire_1_merkez.distance(daire_2_merkez) + (
            daire_1.R,
            daire_2.R,
        )
        self.sonuc_goster()

        self.cv2.line(
            self.image, (daire_1.X, daire_1.Y), (daire_2.X, daire_2.Y), Sabitler.cizgi_rengi, Sabitler.cizgi_kalinligi
        )

        return self

    def sonuc_goster(self):
        baslik = "--------- " + self.sinif_adi + " ---------"
        print(baslik)
        print("X: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[0]))
        print("Y: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[1]))
        print("H: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[2]))
        print("R1: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[3]))
        print("R2: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[4]))
        print("-" * len(baslik))
        return self
