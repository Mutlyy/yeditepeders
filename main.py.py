fiyat=float(input("kekin dolar maliyeti: "))
miktar=float(input("kekin miktari: "))

dolar = int(fiyat*miktar)
cent = (fiyat-int(fiyat))//0.01
print (str(dolar)+" Dollar ve " + str(int(cent)) + " Cent")