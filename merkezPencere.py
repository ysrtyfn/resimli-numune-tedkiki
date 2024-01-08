import tkinter as tk
import cv2
import pyautogui

from Sabitler import Sabitler
from Nokta import Nokta

from Referans import Referans
from NoktaNokta import NoktaNokta
from NoktaDaire import NoktaDaire
from DaireDaire import DaireDaire
from NoktaCizgi import NoktaCizgi
from DaireCizgi import DaireCizgi

sabitler = Sabitler()


class Pencere(tk.Tk):
    vaziyet = Referans()
    ref_vaziyet = vaziyet

    buyutme_kenar_boslugu = int(Sabitler.buyutme_pixel_sayisi / 2)

    def __init__(self):
        super().__init__()
        # self.overrideredirect(True)
        self.protocol("WM_DELETE_WINDOW", self.kapat)

        self.lbl_giris_msj = tk.Label(text="Ölçüm Yöntemini Seçiniz")
        self.lbl_giris_msj.grid(column=0, row=0, columnspan=2)

        self.btn_nkt_nkt = tk.Button(text="Referans Ölçümü", width=15, height=1, command=self.onClickRefOlc)
        self.btn_nkt_nkt.grid(column=0, row=1, columnspan=2)

        self.btn_nkt_nkt = tk.Button(text="Nokta - Nokta", width=15, height=1, command=self.onClickNN)
        self.btn_nkt_nkt.grid(column=0, row=2, columnspan=2)

        self.btn_nkt_dre = tk.Button(text="Nokta - Daire", width=15, height=1, command=self.onClickND)
        self.btn_nkt_dre.grid(column=0, row=3, columnspan=2)

        self.btn_nkt_czg = tk.Button(text="Nokta - Çizgi", width=15, height=1, command=self.onClickNC)
        self.btn_nkt_czg.grid(column=0, row=4, columnspan=2)

        self.btn_dre_dre = tk.Button(text="Daire - Daire", width=15, height=1, command=self.onClickDD)
        self.btn_dre_dre.grid(column=0, row=5, columnspan=2)

        self.btn_dre_czg = tk.Button(text="Daire - Çizgi", width=15, height=1, command=self.onClickDC)
        self.btn_dre_czg.grid(column=0, row=6, columnspan=2)

        self.btn_dre_czg = tk.Button(text="Yenile", width=15, height=1, command=self.onClickYenile)
        self.btn_dre_czg.grid(column=0, row=7, columnspan=2)

        self.lbl_olck_msj = tk.Label(text="Ölçeklendir(Hazır Değil!)")
        self.lbl_olck_msj.grid(column=0, row=8, columnspan=2)

        self.btn_uzaklastir = tk.Button(text="-", width=5, height=1, command=self.onClickUzaklastir)
        self.btn_uzaklastir.grid(column=0, row=9, columnspan=1)
        self.btn_uzaklastir["state"] = "disabled"

        self.btn_yaklastir = tk.Button(text="+", width=5, height=1, command=self.onClickYakinlastir)
        self.btn_yaklastir.grid(column=1, row=9, columnspan=1)
        self.btn_yaklastir["state"] = "disabled"

        self.lbl_giris_msj = tk.Label(text="By RESW")
        self.lbl_giris_msj.grid(column=0, row=10, columnspan=2)

        self.bind("<ButtonPress-1>", self.StartMove)
        self.bind("<ButtonRelease-1>", self.StopMove)
        self.bind("<B1-Motion>", self.OnMotion)

        self.baslat()

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))

    def baslat(self):
        self.image = cv2.imread("resim-2.png", 1)
        self.clone = self.image.copy()

        self.pencere_ismi = "image"
        cv2.namedWindow(self.pencere_ismi)
        cv2.moveWindow(self.pencere_ismi, 400, 150)
        cv2.setMouseCallback(self.pencere_ismi, self.fareTiklamasi)
        self.resmiCiz()

    def resmiCiz(self):
        cv2.imshow(self.pencere_ismi, self.image)

    def buyutulmusResmiCiz(self, x_arg, y_arg):
        if x_arg > self.buyutme_kenar_boslugu:
            x = x_arg - self.buyutme_kenar_boslugu
        else:
            x = self.buyutme_kenar_boslugu

        if y_arg > self.buyutme_kenar_boslugu:
            y = y_arg - self.buyutme_kenar_boslugu
        else:
            y = self.buyutme_kenar_boslugu

        h = Sabitler.buyutme_pixel_sayisi
        w = Sabitler.buyutme_pixel_sayisi

        crop_img = self.image[y : y + h, x : x + w].copy()

        height, width = crop_img.shape[:2]
        crop_img = cv2.resize(
            crop_img,
            (int(Sabitler.buyutme_katsayisi * width), int(Sabitler.buyutme_katsayisi * height)),
            interpolation=cv2.INTER_CUBIC,
        )

        height, width = crop_img.shape[:2]
        cv2.circle(
            crop_img, (int(width / 2), int(height / 2)), Sabitler.isaretci_nokta_capi, Sabitler.isaretci_nokta_rengi, -1
        )
        cv2.imshow("Zoom", crop_img)

    def onClickRefOlc(self):
        print("onClickRefOlc")
        self.vaziyet = Referans()

    def onClickNN(self):
        print("onClickNN")
        self.vaziyet = NoktaNokta(cv2, self.image)

    def onClickND(self):
        print("onClickND")
        self.vaziyet = NoktaDaire(cv2, self.image)

    def onClickDD(self):
        print("onClickDD")
        self.vaziyet = DaireDaire(cv2, self.image)

    def onClickNC(self):
        print("onClickNC")
        self.vaziyet = NoktaCizgi(cv2, self.image)

    def onClickDC(self):
        print("onClickDC")
        self.vaziyet = DaireCizgi(cv2, self.image)

    def onClickYenile(self):
        print("onClickYenile")
        self.image = self.clone.copy()
        self.sifirla()
        ref_sil = pyautogui.confirm(text="Referanslar temizlensin mi?", title="Temizle", buttons=["Temizle", "Kalsın"])
        if ref_sil == "Kalsın":
            ref_noktalari = self.ref_vaziyet.getir_noktalari()
            # print(len(ref_noktalari))
            if len(ref_noktalari) > 0:
                self.isaretciyiCiz(ref_noktalari[0].X, ref_noktalari[0].Y)
                self.isaretciyiCiz(ref_noktalari[1].X, ref_noktalari[1].Y)
        else:
            self.vaziyet = Referans()

        self.resmiCiz()

    def onClickUzaklastir(self):
        print("onClickUzaklastir")
        height, width = self.image.shape[:2]
        self.image = cv2.resize(
            self.image,
            (int(Sabitler.uzaklastirma_katsayisi * width), int(Sabitler.uzaklastirma_katsayisi * height)),
            interpolation=cv2.INTER_CUBIC,
        )
        self.resmiCiz()

    def onClickYakinlastir(self):
        print("onClickYakinlastir")
        height, width = self.image.shape[:2]
        self.image = cv2.resize(
            self.image,
            (int(Sabitler.yakinlastirma_katsayisi * width), int(Sabitler.yakinlastirma_katsayisi * height)),
            interpolation=cv2.INTER_CUBIC,
        )
        self.resmiCiz()

    def fareTiklamasi(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            nokta = Nokta(x, y)
            print("Seçilen Nokta: " + nokta.__str__())

            if self.vaziyet is not None:
                durum = self.vaziyet.nokta_ekle(nokta)

                if durum:
                    self.isaretciyiCiz(x, y)
            else:
                print("Ölçüm yöntemini seçiniz")
            self.resmiCiz()
        self.buyutulmusResmiCiz(x, y)

    def isaretciyiCiz(self, x, y):
        cv2.circle(self.image, (x, y), Sabitler.isaretci_nokta_capi, Sabitler.isaretci_nokta_rengi, -1)
        cv2.line(
            self.image,
            (x, y - Sabitler.isaretci_cizgi_uzunlugu),
            (x, y + Sabitler.isaretci_cizgi_uzunlugu),
            Sabitler.isaretci_cizgi_rengi,
            Sabitler.isaretci_cizgi_kalinligi,
        )
        cv2.line(
            self.image,
            (x - Sabitler.isaretci_cizgi_uzunlugu, y),
            (x + Sabitler.isaretci_cizgi_uzunlugu, y),
            Sabitler.isaretci_cizgi_rengi,
            Sabitler.isaretci_cizgi_kalinligi,
        )

    def sifirla(self):
        self.vaziyet = None

    def kapat(self):
        cv2.destroyAllWindows()
        self.destroy()


pencere = Pencere()
pencere.title("Ölçer")
# pencere.geometry('256x256')

pencere.mainloop()
