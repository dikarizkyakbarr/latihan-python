import os
import time

def menu_1():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("==========================")
        print("    BIODATA MAHASISWA     ")
        print("==========================")
        nim = input("Masukan Nomor NIM : ")
        nama = input("Masukan Nama : ")
        kelas = input("Masukan Kelas : ")
        telepon = input("Masukan Nomor Telepon : ")
        alamat = input("Masukan Alamat : ")

        konfirmasi = input("Apakah data yang diisi sudah benar? (y/n): ")
        while konfirmasi.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            konfirmasi = input("Apakah data yang diisi sudah benar? (y/n): ")

        if konfirmasi.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("==========================")
            print("   BIODATA MAHASISWA      ")
            print("==========================")
            print("NIM =", nim)
            print("Nama =", nama)
            print("Kelas =", kelas)
            print("Telepon =", telepon)
            print("Alamat =", alamat)
            print("===========================")

            ulang = input("Apakah Anda ingin membuat biodata lagi? (y/n): ")
            while ulang.lower() not in ('y', 'n'):
                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                ulang = input("Apakah Anda ingin membuat biodata lagi? (y/n): ")

            if ulang.lower() == 'y':
                continue 
            elif ulang.lower() == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                break  
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue  

def menu_2():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("==========================")
        print(" MENU LATIHAN MATEMATIKA  ")
        print("==========================")
        print("1. Menghitung luas dan keliling")
        print("2. Latihan Matematika")
        print("0. kembali ke menu utama")
        pilihan_menu_2 = input("Masukkan Pilihan (0-2) : ")

        if pilihan_menu_2 == "1":
            submenu_hitung_luas_keliling()
        elif pilihan_menu_2 == "2":
            # Implement the code for "Latihan Matematika"
            pass
        elif pilihan_menu_2 == "0":
            break
        else:
            print("Pilihan Menu tersebut tidak tersedia. Silakan memilih menu yang tersedia angka 0-2.")

def submenu_hitung_luas_keliling():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========================")
        print("  MENGHITUNG LUAS & KELILING  ")
        print("==========================")
        print("1. Lingkaran")
        print("2. Persegi")
        print("3. Persegi Panjang")
        print("0. Kembali ke Menu Utama")
        pilihan_submenu = input("Masukkan Pilihan (0-3) : ")

        if pilihan_submenu == "1":
            hitung_luas_keliling_lingkaran()
        elif pilihan_submenu == "2":
            hitung_luas_keliling_persegi()
        elif pilihan_submenu == "3":
            hitung_luas_keliling_persegi_panjang()
        elif pilihan_submenu == "0":
            break
        else:
            print("Pilihan Menu tersebut tidak tersedia. Silakan memilih menu yang tersedia angka 0-3.")

def hitung_luas_keliling_lingkaran():
    #hitung lingkaran
    pass

def hitung_luas_keliling_persegi():
    #hitung persegi
    pass

def hitung_luas_keliling_persegi_panjang():
    #hitung persegi panjang
    pass

def hitung_luas_keliling_segitiga():
    #hitung segitiga
    pass

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("==========================")
    print("  Silahkan Memilih Menu   ")
    print("==========================")
    print("1. Membuat Biodata")
    print("2. Latihan Matematika")
    print("0. Keluar")
    pilihan = input("Masukan Pilihan (0-2) : ")
    
    if pilihan == "1":
        menu_1()
    elif pilihan == "2":
        menu_2()
    elif pilihan == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========================")
        print("      Sampai jumpa!       ")
        print("==========================")
        for i in range(5, 0, -1):
            print(f"Keluar program dalam {i} detik ...")
            time.sleep(1)
        break
    else:
        print("Pilihan Menu tersebut tidak tersedia. Silakan memilih menu yang tersedia angka 0-2.")
