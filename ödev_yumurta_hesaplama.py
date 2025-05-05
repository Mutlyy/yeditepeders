yumurta_sayisi = int(input("Bu sabah kaç yumurta topladığınızı lütfen giriniz: "))
kutu_sayisi_12 = yumurta_sayisi // 12
kalan = yumurta_sayisi % 12
kutu_sayisi_6 = kalan // 6
artan_yumurta = kalan % 6
print("12'lik kutu sayısı:", kutu_sayisi_12)
print("6'lık kutu sayısı:", kutu_sayisi_6)
print("Kahvaltıda kullanılacak yumurta sayısı:", artan_yumurta)
