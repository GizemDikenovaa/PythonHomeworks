birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayiOkuma):
    birlerBasamagi = sayi % 10
    onlarBasamagi = sayi // 10
    return onlar[onlarBasamagi] + " " + birler[birlerBasamagi]


def sayiAtama(sayi):
    basamak = 0
    while (sayi > 0):
        basamak += 1
        sayi //= 10
    if (basamak == 2):
        print(okunus(sayi))
    else:
        print("İki basamaklı sayı giriniz.")


sayi = int(input("Sayı:"))
sayiAtama(sayi)
