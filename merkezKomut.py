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

ref_vaziyet = None
vaziyet = Referans()
ref_vaziyet = vaziyet


def isaretciyiCiz(x, y):
    cv2.circle(image, (x, y), Sabitler.isaretci_nokta_capi, Sabitler.isaretci_nokta_rengi, -1)
    cv2.line(
        image,
        (x, y - Sabitler.isaretci_cizgi_uzunlugu),
        (x, y + Sabitler.isaretci_cizgi_uzunlugu),
        Sabitler.isaretci_cizgi_rengi,
        Sabitler.isaretci_cizgi_kalinligi,
    )
    cv2.line(
        image,
        (x - Sabitler.isaretci_cizgi_uzunlugu, y),
        (x + Sabitler.isaretci_cizgi_uzunlugu, y),
        Sabitler.isaretci_cizgi_rengi,
        Sabitler.isaretci_cizgi_kalinligi,
    )


def fareTiklamasi(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        nokta = Nokta(x, y)

        if vaziyet is not None:
            durum = vaziyet.nokta_ekle(nokta)

            if durum:
                isaretciyiCiz(x, y)
        else:
            print("Ölçüm yöntemini seçiniz")


def sifirla():
    vaziyet = None
    ref_noktalari = ref_vaziyet.getir_noktalari()
    isaretciyiCiz(ref_noktalari[0].X, ref_noktalari[0].Y)
    isaretciyiCiz(ref_noktalari[1].X, ref_noktalari[1].Y)


def sifirla_ref():
    vaziyet = Referans()


image = cv2.imread("resim-2.png", 1)
clone = image.copy()

pencere_ismi = "image"
cv2.namedWindow(pencere_ismi)
cv2.moveWindow(pencere_ismi, 400, 150)
cv2.setMouseCallback(pencere_ismi, fareTiklamasi)

print("Referans noktalarını tanımlayınız")
while True:
    cv2.imshow(pencere_ismi, image)
    key = cv2.waitKey(1) & 0xFF
    # --------------------------------------------------------------------------------------------------
    if key == ord("r"):
        vaziyet = Referans()
    # --------------------------------------------------------------------------------------------------
    elif key == ord("q"):
        vaziyet = NoktaNokta()
    # --------------------------------------------------------------------------------------------------
    if key == ord("w"):
        vaziyet = NoktaDaire(cv2, image)
    # --------------------------------------------------------------------------------------------------
    if key == ord("e"):
        vaziyet = DaireDaire(cv2, image)
    # --------------------------------------------------------------------------------------------------
    if key == ord("a"):
        vaziyet = NoktaCizgi(cv2, image)
    # --------------------------------------------------------------------------------------------------
    if key == ord("s"):
        vaziyet = DaireCizgi(cv2, image)
    # --------------------------------------------------------------------------------------------------
    # if the 'y' key is pressed, reset
    elif key == ord("y"):
        image = clone.copy()
        sifirla()
        print("Ölçüleri temizlendi.")

        ref_sil = pyautogui.confirm(text="Referanslar temizlensin mi?", title="Temizle", buttons=["Temizle", "Kalsın"])

        print("Referanslar temizlensin mi?")
        if ref_sil == "Temizle":
            sifirla_ref()
            print("Referanslar temizlendi.")
    # --------------------------------------------------------------------------------------------------
    # if the 'x' key is pressed, break from the loop
    elif key == ord("x"):
        break

# close all open windows
cv2.destroyAllWindows()
