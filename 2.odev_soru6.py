liste = input("Liste toplamı için sayılar giriniz: ").split()
toplam = 0
for sayi in liste:
    toplam += int(sayi)
print("Toplam:", toplam)


