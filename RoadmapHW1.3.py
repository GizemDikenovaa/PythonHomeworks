vize1 = int(input("vize 1 notu: "))
vize2 = int(input("vize 2 notu: "))
final = int(input("final notu: "))

if ((vize1 >= 0 and vize1 <= 100) and (vize2 >= 0 and vize2 <= 100) and (final >= 0 and final <= 100)):
    vize1 = ((30 * vize1) / 100)
    vize2 = ((30 * vize2) / 100)
    final = ((40 * final) / 100)

    toplam = vize1 + vize2 + final

    if (toplam >= 90):
        print("Harf notunuz: AA'dır.")
    elif (toplam >= 85):
        print("Harf notunuz: BA'dır")
    elif (toplam >= 80):
        print("Harf notunuz: BB'dir")
    elif (toplam >= 75):
        print("Harf notunuz: CB'dir")
    elif (toplam >= 70):
        print("Harf notunuz: CC'dir")
    elif (toplam >= 65):
        print("Harf notunuz: DC'dir")
    elif (toplam >= 60):
        print("Harf notunuz: DD'dir")
    elif (toplam >= 55):
        print("Harf notunuz: FD'dir")
    else:
        print("Harf notunuz: FF'dir")

else:
    print("Geçersiz değer girdiniz. 0 ile 100 arasında bir değer giriniz.")
