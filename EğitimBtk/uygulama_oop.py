class BankaHesabı:
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye = 0.0
    
    def get_bakiye(self):
        return self.bakiye
    
    def paraYatırma(self, miktar):
        self.bakiye += miktar  
        return self.bakiye

    def paraCek(self, miktar):
        self.bakiye -= miktar
        return self.bakiye
    
hesap = BankaHesabı("Ozan Gunduz")
print(hesap.paraYatırma(1000))
print(hesap.get_bakiye())
hesap.paraCek(500)
print(hesap.get_bakiye())
