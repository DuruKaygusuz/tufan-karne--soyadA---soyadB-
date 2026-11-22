from veri import DERS_ADLARI, KREDILER, NOTLAR
import ortalama
import degerlendirme

def main():
    while True:
        print("\n=== KARNE HESAPLAYICI ===")
        # MENU: secenekler buraya
        print("0) Cikis")
        secim = input("> ")
        if secim == "0":
            break
        # MENU: elif'ler buraya
        else:
            print("Gecersiz secim")
if __name__ == "__main__":
    main()


