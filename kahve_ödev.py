fiyat = {
    "espresso": 2.5,
    "americano": 3.0,
    "latte": 2.5,
    "cappuccino": 3.0,
    "macchiato": 2.5,
    "mocha": 3.5,
    "flat white": 2.5
}
kahve = input("Kahve secimi Espresso, Americano, Latte, Cappuccino, Macchiato, Mocha, Flat White:")
boyut = input("Boyut secimi Medium / Large / XL: ")
tuketim = input("buradamı) yoksa  paketmi : ")
toplam = fiyat.get(kahve, 0)
if boyut == "Large":
    toplam += 1.0
elif boyut == "XL":
    toplam += 1.5
if tuketim == "g":
    toplam += 2
elif tuketim =="p":
    toplam += 1

print("Toplam fiyatınız:",toplam)