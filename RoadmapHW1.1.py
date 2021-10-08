def tam_bolunenler(min, max, bolen):
    sayac = 0
    for i in range(min, max):
        if i % bolen == 0:
            sayac += 1

    return sayac


min_sayi = int(input("minimum pozitif sayı:"))
max_sayi = int(input("maximum pozitif sayı:"))
bolen_sayi = int(input("bölünecek sayı:"))

print("Toplam {} sayı bölünmektedir.".format(tam_bolunenler(min_sayi, max_sayi, bolen_sayi)))
