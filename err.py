
import sys

liste = [ 7, 'Berk', 0 , 3 , "6"]

for x in liste:
    try:
        print("Sayı : " + str(x))
        sonuc = 1/int(x)
        print("Sonuç : " + str(sonuc))

    except:
        print(str(x) + " Hesaplanamadı")
        print("Sistem hatası : " + str(sys.exc_info()[0:1000000000]))
