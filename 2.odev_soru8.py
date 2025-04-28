list=[]
for _ in range(5):
  sayi=int(input("Lütfen sayi giriniz :"))
  list.append(sayi)
  
for x in list:
  if (x%2) ==0:
    print(x)