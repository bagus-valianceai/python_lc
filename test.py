#function ini untuk menghitung volume kubus
def menghitung_volume_kubus(r):
    count_volume = r**3

    return count_volume

#function ini untuk menghitung volume balok
def menghitung_volume_balok(panjang,lebar,tinggi):
    count_volume = panjang*lebar*tinggi

    return count_volume

def main():
    try:
        nama_bangun_ruang = input("Masukan Nama Bangun Ruang: ")

        if nama_bangun_ruang == "kubus":
            r = int(input("Masukan nilai rusuk "))
            print(menghitung_volume_kubus(r))

        elif nama_bangun_ruang == "balok":
            panjang = int(input("Masukan nilai panjang "))
            lebar = int(input("Masukan nilai lebar ")) 
            tinggi = int(input("Masukan nilai tinggi "))
            print(menghitung_volume_balok(panjang, lebar, tinggi))

        else:
            raise Exception
        
    except ValueError:
        print("Nilai bukan tipe data integer")

    except Exception:
        print("Terjadi kesalahan input nama bangun ruang")

    finally:
        print("Sekian dan terima kasih!")

if __name__ == "__main__":
    main()