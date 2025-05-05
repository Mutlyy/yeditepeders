kap = input("Kap sec (Cup / Cone): ")
if kap == "Cup":
    fiyat = 0.5
elif kap == "Cone":
    fiyat = 0.8
else:
    print("Gecersiz kap!")
    exit()

top = int(input("Kac top? (1-4): "))
fiyat += top * 1.0
flake = input("Flake ister misin? (e/h): ")
if flake == "e":
    fiyat += 0.4
choco = input("Chocolate sprinkle ister misin? (e/h): ")
if choco == "e":
    fiyat += 0.3
straw = input("Strawberry coulis ister misin? (e/h): ")
if straw == "e":
    fiyat += 0.6
print("Toplam fiyat: £", fiyat)