urunler = [

    { "ürünAdı" : "HP Victus" , "Fiyat" : 32999 } ,   
    { "ürünAdı" : "Lenovo ThinkPad" , "Fiyat" : 25499 },
    { "ürünAdı" : "Apple Macbook" , "Fiyat" : 49999 },
    { "ürünAdı" : "Huawai Matebook" , "Fiyat" : 26999 },
    { "ürünAdı" : "Casper Nirvana" , "Fiyat" : 20000 }     
                 
]

# Aşağıdaki cümleyi her satıra uygulayınız.
#   "HP victus marka ürünün fiyatı 32999 türk lirası."

# for urun in urunler:
#     print(f"{urun['ürünAdı']} marka ürünün fiyatı {urun['Fiyat']} türk lirası.")

# ürünlerin fiyatları toplamı ?

# toplamFiyat = 0

# for urun in urunler:
    
#     toplamFiyat += urun['Fiyat']

# print(toplamFiyat)    

# 25000 ile 40000 arası fiyatları listele.

# for urun in urunler :
#     if urun['Fiyat'] >= 25000 and urun['Fiyat'] <= 40000:
        
#         print(urun)

#kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.

# kelime = str(input("Ürün Seçiniz: "))

# for i in urunler:
#     if (i['ürünAdı'].lower().find(kelime.lower()) > -1 ):
#         print(f"{i['ürünAdı']}")