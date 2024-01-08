from Aletler import Aletler

from Nokta import Nokta


class DaireCizgi:
    sinif_adi = "DaireCizgi"

    aletler = Aletler()

    cv2 = None
    image = None
    nokta_listesi = []
    nokta_sayisi = 5
    hesap_sonuclari = ()  # (dx, dy, math.hypot(dx, dy))

    def __init__(self, cv2, image):
        print(self.sinif_adi + ": Ölçüm için %d nokta tanımlayınız!" % self.nokta_sayisi)
        print(self.sinif_adi + ": İlk 3 nokta daire için sonraki 2 nokta ise çizgi için kullanılacaktır.")
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
        daire_noktalari = self.nokta_listesi[0:3]
        cizgi_noktalari = self.nokta_listesi[3:]

        daire = self.aletler.define_circle(self.cv2, self.image, daire_noktalari)
        daire_merkez = Nokta(daire.X, daire.Y)

        nokta_listesi_temp = [daire_merkez] + cizgi_noktalari

        self.hesap_sonuclari = self.aletler.nokta_cizgi_arasi_mesafeyi_hesapla(
            self.cv2, self.image, nokta_listesi_temp
        ) + (daire.R,)
        self.sonuc_goster()

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
