
def program():
    x_katsayi = y_katsayi = iki_x_katsayi = iki_y_katsayi = 0
    extra = temp = extra2 = x = y = kontrol = 0
    degisken = degisken2 = ""
    liste = []
    negative1 = negative2 = negative3 = False
    rakamlar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    harfler = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v",
               "y", "w", "x", "z", "q"]

    print("1. denklemi boşluk bırakarak yazınız")
    denklem = input("--> ")
    liste.extend(denklem)

    denklem.replace(" ", "")

    for harf in liste:
        if harf in harfler and kontrol == 0:
            degisken = harf
            kontrol += 1
        elif harf in harfler and kontrol == 1:
            degisken2 = harf
            kontrol += 1

    for i in range(len(liste)):
        if liste[i] in rakamlar and temp == 0:
            if x_katsayi == 0 and temp == 0:
                x_katsayi += int(liste[i])
                continue
            elif x_katsayi > 0 and temp == 0:
                x_katsayi = x_katsayi * 10 + int(liste[i])
                continue

        elif liste[i] == "-" and temp == 0:
            negative1 = True
            continue

        elif liste[i] in harfler and temp == 0:
            temp = 1
            continue
        # -------*******--------

        if liste[i] in rakamlar and temp == 1:
            if y_katsayi == 0:
                y_katsayi += int(liste[i])
                continue
            else:
                y_katsayi = y_katsayi * 10 + int(liste[i])
                continue

        elif liste[i] == "-" and temp == 1:
            negative2 = True
            continue

        elif liste[i] == "=" and temp == 1:
            temp += 1
            continue

        if liste[i] in rakamlar and temp == 2:
            if extra == 0:
                extra += int(liste[i])
                continue
            else:
                extra = extra * 10 + int(liste[i])
        elif liste[i] == "-" and temp == 2:
            negative3 = True
            continue

    if negative1:
        x_katsayi *= -1
        negative1 = False
    if negative2:
        y_katsayi *= -1
        negative2 = False
    if negative3:
        extra *= -1
        negative3 = False


    liste.clear()

    print("2. denklemi giriniz")
    denklem = input("--> ")
    denklem.replace(" ", "")
    liste.extend(denklem)
    temp = 0

    for i in range(len(liste)):
        if liste[i] in rakamlar and temp == 0:
            if iki_x_katsayi == 0 and temp == 0:
                iki_x_katsayi += int(liste[i])
                continue
            elif iki_x_katsayi > 0 and temp == 0:
                iki_x_katsayi = iki_x_katsayi * 10 + int(liste[i])
                continue

        elif liste[i] == "-" and temp == 0:
            negative1 = True
            continue

        elif liste[i] in harfler and temp == 0:
            temp = 1
            continue
        # -------*******--------

        if liste[i] in rakamlar and temp == 1:
            if iki_y_katsayi == 0:
                iki_y_katsayi += int(liste[i])
                continue
            else:
                iki_y_katsayi = iki_y_katsayi * 10 + int(liste[i])
                continue

        elif liste[i] == "-" and temp == 1:
            negative2 = True
            continue

        elif liste[i] == "=" and temp == 1:
            temp += 1
            continue

        if liste[i] in rakamlar and temp == 2:
            if extra2 == 0:
                extra2 += int(liste[i])
                continue
            else:
                extra2 = extra2 * 10 + int(liste[i])
        elif liste[i] == "-" and temp == 2:
            negative3 = True
            continue

    if x_katsayi == 0:
        x_katsayi = 1
    if y_katsayi == 0:
        y_katsayi = 1

    if iki_x_katsayi == 0:
        iki_x_katsayi = 1
    if iki_y_katsayi == 0:
        iki_y_katsayi = 1

    if negative1:
        iki_x_katsayi *= -1
    if negative2:
        iki_y_katsayi *= -1
    if negative3:
        extra2 *= -1

    print("Algılanan: ")
    print("1. yalın denklem --> ", x_katsayi, degisken, y_katsayi, degisken2, " = ", extra)
    print("2. yalın denklem --> ", iki_x_katsayi, degisken, iki_y_katsayi, degisken2, " = ", extra2, "\n")

    temp = y_katsayi
    if y_katsayi > 0:
        if iki_y_katsayi > 0:
            x_katsayi *= iki_y_katsayi * -1
            y_katsayi *= iki_y_katsayi * -1
            extra *= iki_y_katsayi * -1

            iki_x_katsayi *= temp
            iki_y_katsayi *= temp
            extra2 *= temp
        else:
            x_katsayi *= iki_y_katsayi * -1
            y_katsayi *= iki_y_katsayi * -1
            extra *= iki_y_katsayi * -1

            iki_x_katsayi *= temp
            iki_y_katsayi *= temp
            extra2 *= temp
    else:
        if iki_y_katsayi > 0:
            x_katsayi *= iki_y_katsayi
            y_katsayi *= iki_y_katsayi
            extra *= iki_y_katsayi

            iki_x_katsayi *= temp * -1
            iki_y_katsayi *= temp * -1
            extra2 *= temp * -1
        else:
            x_katsayi *= iki_y_katsayi * -1
            y_katsayi *= iki_y_katsayi * -1
            extra *= iki_y_katsayi * -1

            iki_x_katsayi *= temp
            iki_y_katsayi *= temp
            extra2 *= temp

    print("1. denklem:\n", degisken, ": ", x_katsayi, degisken2, ": ", y_katsayi, " = ", extra)
    print("2. denklem:\n", degisken, ": ", iki_x_katsayi, degisken2, ": ", iki_y_katsayi, " = ", extra2)


    carp_x_katsayi = x_katsayi + iki_x_katsayi
    toplam = extra + extra2

    x = toplam / carp_x_katsayi

    temp = x * x_katsayi
    extra -= temp
    y = extra / y_katsayi

    print("Sonuç: ")
    print("\n", degisken, ": ", x, "\n", degisken2, ": ", y, "\n")
    print("Yuvarlanmış hali: ")
    print("\n", degisken, ": ", round(x, 3), "\n", degisken2, ": ", round(y, 3))


program()
