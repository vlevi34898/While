#5. Feladat
#Írj egy programot, amely a felhasználótól páros számot kér be.
#Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés
#mindaddig, amíg végül páros számot nem ad meg a felhasználó.

folytatja = True
while folytatja:
    valasz =  int(input("Írj egy páros számot:"))
    if valasz % 2 == 0:
        folytatja = False
print('>> Program vége! <<')      
  
