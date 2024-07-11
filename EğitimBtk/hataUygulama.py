# liste = ["1","3","5","20a","abc","60"]

# liste elemanları içindeki sayısal değerleri bulunuz.

# for i in liste :
#     try:
#         sonuc = int(i)
#         print(i)
#     except ValueError:
#         continue

    # kullanıcı q değeri girerse çık inputun sayı olduğundan emin ol aksi halde hata mesajı ver.

# while True:
#     sayi = input("sayı: ")
#     if(sayi == "q"):
#         break

#     try:
#         sonuc = float(sayi)
#         print(f"girilen sayı: {sonuc}")
#         break
#     except ValueError:
#         print("Bir sayı giriniz.")
#         continue

# dict ve key bilgilerini parametre olarak alan get(dict ,key) fonksiyonu hazırlayınız.

# urun = {"urunAdi":"samsung s20", "fiyat":20000}

# def get(liste , key):
#     try:
#         return liste[key]
#     except KeyError:
#         return None
# sonuc = get(urun,"fiyat")
# sonuc = get(urun,"urunAdi")
# sonuc = get(urun,"versiyon")
# print(sonuc)