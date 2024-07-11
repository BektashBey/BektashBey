# not uygulaması

# menu
    #1-not gir.
    #2-ortalamaları göster.
    #3-notları kaydet
    #4-çıkış

def notGir():
    ad = input("öğrenci adı:")
    soyad = input("öğrenci soyadı:")
    vize1 = input("öğrenci 1.vizesi:")
    vize2 = input("öğrenci 2.vizesi:")
    final = input("öğrenci finali:")

with open("ogrenci_notları.txt", "a", encoding="utf-8") as file:
    file.write(f"{ad} {soyad}:{vize1},{vize2},{final}\n")


def ortalamaGöster():
    with open("ogrenci_notları.txt","r",encodeing="utf-8") as file:
        for satır in file:
            print(satır)

def notlarıKaydet():
    pass


while True:
    islem = input("1-not gir./n2-ortalamaları göster./n3-notları kaydet/n4-çıkış")

    if islem == "1":
        notGir()
    elif islem == "2":
        ortalamaGöster()
    elif islem == "3":
        notlarıKaydet()
    else:
        break
