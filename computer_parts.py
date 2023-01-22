import time
class Bilgisayar():
    def __init__(self, marka, fiyat, bellek = 256, RAM = 6, renk = "Siyah"):
        self.marka=marka
        self.fiyat=fiyat
        self.bellek=bellek
        self.RAM=RAM
        self.renk=renk
    def bellek_attır(self):
        miktar=int(input("Bellek ne kadar artırılacak:"))
        self.bellek+=miktar
        time.sleep(1)
        print("Yeni bellek hazır!")
    def RAM_arttır(self):
        miktar2=int(input("RAM ne kadar artırılacak:"))
        self.RAM+=miktar2
        time.sleep(1)
        print("Yeni RAM hazır!")
    def __str__(self):
        return "Marka: {}\nFiyat: {}\nBellek: {}\nRAM: {}\nRenk: {}" .format(self.marka, self.fiyat, self.bellek, self.RAM, self.renk)
    def __len__(self):
        return int(self.bellek)
    def renk_degistir(self):
        yeni_renk=input("Bilgisayarınızı ne renk istersiniz?:")
        time.sleep(1)
        print("Yeni renk hazır")
        self.renk= yeni_renk

bilgisayar = Bilgisayar("acer",10000)

print("Bilgisayar Özellikleri")
print('''
İşlemler
1-Bilgisayar Özelliklerini Göster
2-Bellek Arttırma
3-RAM Arttırma 
4-Bilgisayarın Rengini Değiştir
5-Çıkmak için '5' e basınız
''')
while True:
    islem= int(input("Yapmak istediğiniz işlemi seçiniz:"))
    if islem==1:
        print(bilgisayar)
    elif islem==2:
        bilgisayar.bellek_attır()
    elif islem==3:
        bilgisayar.RAM_arttır()
    elif islem==4:
        bilgisayar.renk_degistir()
    elif islem==5:
        print("Çıkış Yapılıyor")
        break
    else:
        print("Geçersiz Tuşlama Yaptınız")







