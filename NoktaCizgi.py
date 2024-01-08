from Aletler import Aletler


class NoktaCizgi:
    sinif_adi = "NoktaCizgi"

    aletler = Aletler()

    cv2 = None
    image = None
    nokta_listesi = []
    nokta_sayisi = 3
    hesap_sonuclari = ()  # (dx, dy, math.hypot(dx, dy))

    def __init__(self, cv2, image):
        print(self.sinif_adi + ": Ölçüm için %d nokta tanımlayınız!" % self.nokta_sayisi)
        print(self.sinif_adi + ": Çizgi için ilk nokta harici olan diğer noktalar kullanılacaktır.")
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
        self.hesap_sonuclari = self.aletler.nokta_cizgi_arasi_mesafeyi_hesapla(self.cv2, self.image, self.nokta_listesi)
        self.sonuc_goster()

        return self

    def sonuc_goster(self):
        baslik = "--------- " + self.sinif_adi + " ---------"
        print(baslik)
        print("X: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[0]))
        print("Y: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[1]))
        print("H: %s" % self.aletler.px_to_mm(self.hesap_sonuclari[2]))
        print("-" * len(baslik))

        return self
