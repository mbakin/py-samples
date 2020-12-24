"""
Traning : Basic guide application on terminal
"""

guide = {
    "karakter1" : {"ev adresi": "100. Yıl Mahallesi 1062 Sokak Vefakar Sitesi C blok D:4",
                   "iş adresi" : "osmangazi mahallesi 21 Sokak no 16",
                   "ev telefonu" : "02163335564",
                   "iş telefonu" : "02134441444",
                   "cep telefonu" : "05556662112"}
}
isimler = guide.keys()


arananKisi = input("Aranan İsim: ")
if arananKisi in isimler:
    flag = True
else:
    flag = False
arananOzellik = input("Aranan Bilgi: ")

if flag:
    print(guide.get(arananKisi, "kişi bulunamadı").get(arananOzellik, "bilgi bulunamadı"))

else:
    print("Aranan Kişi Rehberde Bulunamadı!")
