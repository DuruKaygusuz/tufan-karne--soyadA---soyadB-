def harf_notu(puan):
    if puan == -1:
        return "GR"
    elif puan >= 90:
        return "AA"
    elif puan >= 85:
        return "BA"
    elif puan >= 80:
        return "BB"
    elif puan >= 75:
        return "CB"
    elif puan >= 70:
        return "CC"
    elif puan >= 60:
        return "DC"
    elif puan >= 50:
        return "DD"
    else:
        return "FF"


def kalan_dersler(notlar, adlar):
    sayac = 0
    for not_degeri, ders_adi in zip(notlar, adlar):
        if not_degeri == -1:
            continue
        if not_degeri < 50:
            print(f"{ders_adi} ({not_degeri})")
            sayac += 1
    return sayac


def basari_durumu(ort):
    if ort >= 85:
        return "Yuksek onur"
    elif ort >= 75:
        return "Onur"
    elif ort >= 50:
        return "Basarili"
    else:
        return "Basarisiz"