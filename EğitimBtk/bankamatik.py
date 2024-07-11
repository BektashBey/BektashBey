# bankamatik uygulaması 

hesaplar = [ {
    "ad": "ozan bektas gunduz",
    "hesapNo" : "3535",
    "sifre" : "123",
    "bakiye" : 20000,
    "ekBakiye" : 5000,
    "userName" : "ozangunduz"  
},

{
    "ad": "furkan adın",
    "hesapNo" : "5555",
    "sifre" : "456",
    "bakiye" : 40000,
    "ekBakiye" : 5000,
    "userName" : "furkanaydın"  
}
]



def menu(hesap):
    print("/n")

    print(f"merhaba, {hesap['ad']} ")

    print("1- Bakiye Sorgulama")
    print("2- Para Çekme")
    print("3- Para Yatırma")

    islem = input("Yapmak istediğiniz işlemi seçiniz: ")

    if islem == "1" :
        bakiyeSorgula(hesap)

    elif islem == "2" :
        paraCekme(hesap)

    elif islem == "3" :
        paraYatırma(hesap)

    else :
        print("yanlış seçim")

    menu(hesap)    


def bakiyeSorgula(hesap):
  print(f"Bakiyeniz: {hesap['bakiye']:,.2f} TL")
  print(f"Ek Bakiyeniz: {hesap['ekBakiye']:,.2f} TL")
     




def paraCekme(hesap):
    miktar = float(input("çekmek istediğiniz miktarı giriniz:"))

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar

        print("paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekBakiye"]    

        if toplam >= miktar :
            ekHesapKullanımİzni = input("ek hesap kullanmak ister misiniz? (e/h)")

            if ekHesapKullanımİzni == "e":
                kullanılacakMiktar = hesap["bakiye"] - miktar
                hesap["bakiye"] = 0
                hesap["ekBakiye"] += kullanılacakMiktar
                print("paranızı alabilirsiniz.")

            else:
                print("üzgünüz bakiyeniz yetersiz.")  
              
        else:
                print("üzgünüz bakiyeniz yetersiz.") 



def paraYatırma(hesap):
    yatırılacakMiktar = float(input("yatıracağınız parayı giriniz: "))
    
    
    if not hesap["ekBakiye"] == 5000:
        hesap["ekBakiye"] += yatırılacakMiktar
        if yatırılacakMiktar > 5000:
            kalanmiktar = abs(yatırılacakMiktar - hesap["ekBakiye"] )
            hesap["ekBakiye"] = 5000
            hesap["bakiye"] += kalanmiktar
        else:
            hesap["ekBakiye"] += yatırılacakMiktar      
    else:
         hesap["bakiye"] += yatırılacakMiktar     

     
def login():
    userName = input("userName: ")
    sifre = input("sifre: ")

    isloggedIn = False

    for hesap in hesaplar :
        if hesap["userName"] == userName and hesap ["sifre"] == sifre:
            isloggedIn = True
            menu(hesap)
            break

    if not (isloggedIn) :    
        print("username yada parola yanlış")

login()

 