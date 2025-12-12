#6.feladat
#Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot!
#A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a
#felhasználót arról is, hány darab ilyen szám volt.

import random

i = 0
db = 0 

while i < 20:
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
        db += 1
    i +=1

print("3-mal osztható számok száma:", db)
  