"""

module1 (db) : urunler

module2 (metodlar) : urunEkle() , urunGuncelle() , urunleriGetir()

module3 (app) : 


            yeni ürün ekleme => urunEkle("iphone 15" , 60000)
            ürün günelleme   => urunGuncelle(1 , "iphone 15 pro" , 80000)
            ürünleri listele => urunleriGetir()

"""

from metods import *

urunEkle("iphone 20",90000)
urunEkle("samsung 20",90000)

for i in urunleriGetir():
    print(i["urunAdi"])

urunGuncelleme(1,"iphone 15 pro" , 80000)

for i in urunleriGetir():
    print(i["urunAdi"])
    