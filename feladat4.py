#4.feladat
#írj egy programot, amely a felhasználó által meghatározott
#alkalommal írja ki a beérkezett szöveget.

szoveg = input("írj egy szöveget: ")

alkalom = int(input("Hányszor írjam ki? "))

i = 0
while i < alkalom:
    print(szoveg)
    i += 1