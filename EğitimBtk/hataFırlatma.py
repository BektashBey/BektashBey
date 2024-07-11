def hataFırlatma(text,renk):
    renkler = ('blue','red','yellow','pink')
    if type(text) is not str:
        raise TypeError('text str tipinde olmalıdır.')
    
    if type(renk) is not str:
        raise TypeError('renk str tipinde olmalıdır')
    
    if renk not in renkler:
        raise ValueError("geçersiz renk!")
    
    
    print(f"{text} {renk} olarak yazıldı.")

try:
    hataFırlatma("merhaba","green")
    hataFırlatma("selam","yellow")
except (TypeError,ValueError) as ex:
    print(ex)

