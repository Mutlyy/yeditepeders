x=input("Bir sözcük giriniz : ")
ses_hrf="aeıioöuüAEIİOÖUÜ"
sayici=0
for harf in x:
 if x in ses_hrf:
   sayici +=1
print(sayici)