def tam_bolunenler(min, max, bolen):
    sayac = 0
    for i in range(min, max + 1):
        if (i % bolen == 0):
            sayac += 1
    return (sayac)


min = int(input("Minimum pozitif sayi:"))
max = int(input("Maximum pozitif sayi:"))
bolenSayi = int(input("Bölen sayi:"))
print("Toplamda {} sayı bölünür.".format(tam_bolunenler(min, max, bolenSayi)))
