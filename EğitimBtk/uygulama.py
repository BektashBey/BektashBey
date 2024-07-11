benzinFiyat = 41
dizelFiyat = 35
lpgFiyat = 22

toplamYakitÜcreti = 0
ortalamaYakitTüketimi = int(input("100 km deki ortalama yakıt tüketimi: "))
kilometre = int(input("kilometre giriniz: " ))
yakitTipi = input("araç yakit tipi seç: ")

ortalamaYakitTüketimi = kilometre * (ortalamaYakitTüketimi / 100)

if(yakitTipi == "benzin"):
   toplamYakitÜcreti = toplamYakitÜcreti * benzinFiyat

elif(yakitTipi == "dizel"):
    toplamYakitÜcreti = toplamYakitÜcreti * dizelFiyat  

elif(yakitTipi == "lpg"):
    toplamYakitÜcreti = toplamYakitÜcreti * lpgFiyat

else:
    print("hello new car")      

if(toplamYakitÜcreti != 0):
    print(toplamYakitÜcreti)    