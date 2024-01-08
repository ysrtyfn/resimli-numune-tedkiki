from Aletler import Aletler
from Sabitler import Sabitler

from Nokta import Nokta


class NoktaDaire:
    sinif_adi = "NoktaDaire"

    aletler = Aletler()

    cv2 = None
    image = None
    nokta_listesi = []
    nokta_sayisi = 4
    hesap_sonuclari = ()  # (dx, dy, math.hypot(dx, dy))

    def __init__(self, cv2, image):
        print(self.sinif_adi + ": Ölçüm için %d nokta tanımlayınız!" % self.nokta_sayisi)
        print(self.sinif_adi + ": Daire için ilk nokta harici olan diğer noktalar kullanılacaktır.")
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
        nokta = self.nokta_listesi[0]
        self.nokta_listesi.pop(0)
        daire_noktalari = self.nokta_listesi
        daire = self.aletler.define_circle(self.cv2, self.image, daire_noktalari)

        daire_merkez = Nokta(daire.X, daire.Y)

        self.hesap_sonuclari = nokta.distance(daire_merkez) + (daire.R,)
        self.sonuc_goster()

        self.cv2.line(
            self.image, (nokta.X, nokta.Y), (daire.X, daire.Y), Sabitler.cizgi_rengi, Sabitler.cizgi_kalinligi
        )

        self.nokta_listesi.insert(0, nokta)
        return self

    def sonuc_goster(self):
        baslik = "--------- " + self.sinif_adi + " ---------"
        print(baslik)
        print("X: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[0]))
        print("Y: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[1]))
        print("H: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[2]))
        print("R: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[3]))
        print("-" * len(baslik))
        return self
