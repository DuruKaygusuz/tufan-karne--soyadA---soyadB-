from veri import DERS_ADLARI, KREDILER, NOTLAR
import ortalama
import degerlendirme

def main():
    while True:
        print("\n=== KARNE HESAPLAYICI ===")
        # MENU: secenekler buraya
        print("0) Cikis")
        print("1) Basit Ortalama")
        secim = input("> ")
        if secim == "0":
            break
        # MENU: elif'ler buraya
        elif secim == "1":
            print("hooho")
            break
        else:
            print("Gecersiz secim")
if __name__ == "__main__":
    main()



