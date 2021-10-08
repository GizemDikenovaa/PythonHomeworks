birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus():
    birler_basamagi = sayi % 10
    onlar_basamagi = sayi // 10

    return onlar[onlar_basamagi] + " " + birler[birler_basamagi]


def sayi_atama(sayi):
    basamak = 0
    while sayi > 0:
        basamak += 1
        sayi //= 10
    if basamak == 2:
        print(okunus())
    else:
        print("İki basamaklı sayı girin!")


sayi = int(input("Sayı:"))
sayi_atama(sayi)