import os
import time


def menu_pertemuan_1():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("===========================")
        print(" MENU LATIHAN PERTEMUAN 1  ")
        print("===========================")
        print("1. Membuat Biodata")
        print("2. Pembelian Tiket Pesawat")
        print("0. kembali ke menu utama")
        pilihan_pertemuan_1 = input("Masukkan Pilihan (0-2) : ")

        if pilihan_pertemuan_1 == "1":
            submenu_latihan_1_pertemuan_1()
        elif pilihan_pertemuan_1 == "2":
            submenu_latihan_2_pertemuan_1(jumlah_transaksi) 
        elif pilihan_pertemuan_1 == "0":
            break
        else:
            print("Pilihan Menu tersebut tidak tersedia. Silakan memilih menu yang tersedia angka 0-2.")



def submenu_latihan_1_pertemuan_1():
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
        
        
def submenu_latihan_2_pertemuan_1(jumlah):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("==========================")
        print("  PEMBELIAN TIKET PESAWAT  ")
        print("==========================")

        jumlah += 1

        no_transaksi = f"{jumlah:04d}"

       
        nama_lengkap = input("Nama Lengkap: ")
        no_kontak = input("Nomor Kontak: ")
        alamat_lengkap = input("Alamat Lengkap: ")

        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================")
        print("  SILAHKAN MEMILIH KELAS PENERBANGAN  ")
        print("======================================")
        print("1. Eksklusif")
        print("2. Ekonomi")
        print("======================================")
        pilihan_kelas = input("Masukkan Pilihan Kelas (1-2): ")

        while pilihan_kelas not in ('1', '2'):
            print("Pilihan tidak valid. Silakan masukkan '1' atau '2'.")
            pilihan_kelas = input("Masukkan Pilihan Kelas (1-2): ")

        if pilihan_kelas == '1':
            kelas_penerbangan = "Eksklusif"
            harga_tiket = 500000  
        else:
            kelas_penerbangan = "Ekonomi"
            harga_tiket = 250000  

        os.system('cls' if os.name == 'nt' else 'clear')
        
        tanggal = input("Masukkan Tanggal Pemberangkatan : ")
        bulan = input("Masukkan Bulan Pemberangkatan : ")
        tahun = input("Masukkan Tahun Pemberangkatan : ")
        tgl_pemberangkatan = f"{tanggal}/{bulan}/{tahun}"

        jumlah_beli = int(input("Jumlah Tiket yang Dibeli: "))
        format_harga_tiket = "{:,.0f}".format(harga_tiket)
        
        total_harga = harga_tiket * jumlah_beli
        format_total_harga = "{:,.0f}".format(total_harga)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================")
        print("  INVOICE PEMBELIAN TIKET PESAWAT ANDA  ")
        print("========================================")
        print("Nomor Transaksi:", no_transaksi)
        print("Nama Lengkap:", nama_lengkap)
        print("Nomor Kontak:", no_kontak)
        print("Alamat Lengkap:", alamat_lengkap)
        print("Tanggal Pemberangkatan:", tgl_pemberangkatan)
        print("Kelas Penerbangan:", kelas_penerbangan)
        print("Harga Tiket: Rp.", format_harga_tiket)
        print("Jumlah Tiket:", jumlah_beli)
        print("Total Harga: Rp.", format_total_harga)
        print("========================================")

        ulang = input("Apakah Anda ingin melakukan pembelian lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin melakukan pembelian lagi? (y/n): ")

        if ulang.lower() == 'y':
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

jumlah_transaksi = 0




def menu_pertemuan_2():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("===========================")
        print(" MENU LATIHAN PERTEMUAN 2  ")
        print("===========================")
        print("1. Menghitung luas dan keliling")
        print("2. Menghitung Bangun Ruang")
        print("0. kembali ke menu utama")
        pilihan_menu_2 = input("Masukkan Pilihan (0-2) : ")

        if pilihan_menu_2 == "1":
            submenu_hitung_luas_keliling()
        elif pilihan_menu_2 == "2":
            submenu_hitung_bangun_ruang()
        elif pilihan_menu_2 == "0":
            break
        else:
            print("Pilihan Menu tersebut tidak tersedia. Silakan memilih menu yang tersedia angka 0-2.")

def submenu_hitung_luas_keliling():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==============================")
        print("  MENGHITUNG LUAS & KELILING  ")
        print("==============================")
        print("1. Lingkaran")
        print("2. Persegi")
        print("3. Persegi Panjang")
        print("4. Belah Ketupat")
        print("5. Jajar Genjang")
        print("6. Layang-layang")
        print("7. Trapesium")
        print("0. Kembali ke Menu Utama")
        pilihan_submenu = input("Masukkan Pilihan (0-8) : ")

        if pilihan_submenu == "1":
            hitung_luas_keliling_lingkaran()
        elif pilihan_submenu == "2":
            hitung_luas_keliling_persegi()
        elif pilihan_submenu == "3":
            hitung_luas_keliling_persegi_panjang()
        elif pilihan_submenu == "4":
            hitung_luas_keliling_belah_ketupat()
        elif pilihan_submenu == "5":
            hitung_luas_keliling_jajar_genjang()
        elif pilihan_submenu == "6":
            hitung_luas_keliling_layang_layang()
        elif pilihan_submenu == "7":
            hitung_luas_keliling_trapesium()
        elif pilihan_submenu == "0":
            break
        else:
            print("Pilihan Menu tersebut tidak tersedia. Silakan memilih menu yang tersedia angka 0-8.")

def hitung_luas_keliling_lingkaran():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=======================================")
        print("  MENGHITUNG LUAS & KELILING LINGKARAN ")
        print("=======================================")
       
        # Input Jari-jari
        jari_jari_input = input("Masukkan jari-jari lingkaran: ")
        if not jari_jari_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        jari_jari = float(jari_jari_input)

        # Rumus luas dan keliling lingkaran
        luas = 3.14 * jari_jari**2
        keliling = 2 * 3.14 * jari_jari

        # Hasil Output
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===============================")
        print("HASIL LUAS & KELILING LINGKARAN")
        print("===============================")
        print(f"Luas : {luas}")
        print(f"Keliling : {keliling}")
        print("===============================")
        ulang = input("Apakah Anda ingin menghitung lingkaran lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung lingkaran lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def hitung_luas_keliling_persegi():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=======================================")
        print("  MENGHITUNG LUAS & KELILING PERSEGI   ")
        print("=======================================")

        # Input panjang sisi
        sisi_input = input("Masukkan panjang sisi persegi: ")
        if not sisi_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi = float(sisi_input)

        # Rumus luas dan keliling persegi
        luas = sisi**2
        keliling = 4 * sisi

        # Hasil Output
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===============================")
        print("HASIL LUAS & KELILING PERSEGI  ")
        print("===============================")
        print(f"Luas : {luas}")
        print(f"Keliling : {keliling}")
        print("===============================")
        ulang = input("Apakah Anda ingin menghitung persegi lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung persegi lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def hitung_luas_keliling_persegi_panjang():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=============================================")
        print("  MENGHITUNG LUAS & KELILING PERSEGI PANJANG ")
        print("=============================================")

        # Input panjang
        panjang_input = input("Masukkan panjang persegi panjang: ")
        if not panjang_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        panjang = float(panjang_input)

        # Input lebar
        lebar_input = input("Masukkan lebar persegi panjang: ")
        if not lebar_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        lebar = float(lebar_input)

        # Rumus luas dan keliling persegi panjang
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        # Hasil Output
        print("=======================================")
        print("HASIL LUAS & KELILING PERSEGI PANJANG  ")
        print("=======================================")
        print(f"Luas : {luas}")
        print(f"Keliling : {keliling}")
        print("=======================================")
        ulang = input("Apakah Anda ingin menghitung persegi panjang lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung persegi panjang lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def hitung_luas_keliling_segitiga():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=============================================")
        print("  MENGHITUNG LUAS & KELILING SEGITIGA        ")
        print("=============================================")

        # Input alas 
        alas_input = input("Masukkan panjang alas segitiga: ")
        if not alas_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        alas = float(alas_input)

        # Input tinggi
        tinggi_input = input("Masukkan tinggi segitiga: ")
        if not tinggi_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        tinggi = float(tinggi_input)

        # Input sisi miring
        sisi_miring_input = input("Masukkan panjang sisi miring segitiga: ")
        if not sisi_miring_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi_miring = float(sisi_miring_input)

        # Rumus luas dan keliling segitiga
        luas = 0.5 * alas * tinggi
        keliling = alas + tinggi + sisi_miring

        # Hasil Output
        print("===================================")
        print("    HASIL LUAS & KELILING SEGITIGA ")
        print("===================================")
        print(f"Luas : {luas}")
        print(f"Keliling : {keliling}")
        print("===================================")
        ulang = input("Apakah Anda ingin menghitung segitiga lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung segitiga lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        
        
def hitung_luas_keliling_belah_ketupat():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=============================================")
        print("   MENGHITUNG LUAS & KELILING BELAH KETUPAT  ")
        print("=============================================")

        # Input diagonal 1
        diagonal1_input = input("Masukkan panjang diagonal 1: ")
        if not diagonal1_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        diagonal1 = float(diagonal1_input)

        # Input diagonal 2
        diagonal2_input = input("Masukkan panjang diagonal 2: ")
        if not diagonal2_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        diagonal2 = float(diagonal2_input)

        # Rumus luas dan keliling belah ketupat
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 4 * diagonal1

        # Hasil Output
        print("========================================")
        print("  HASIL LUAS & KELILING BELAH KETUPAT   ")
        print("========================================")
        print(f"Luas : {luas}")
        print(f"Keliling : {keliling}")
        print("========================================")
        ulang = input("Apakah Anda ingin menghitung belah ketupat lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung belah ketupat lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def hitung_luas_keliling_jajar_genjang():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=============================================")
        print("   MENGHITUNG LUAS & KELILING JAJAR GENJANG  ")
        print("=============================================")

        # Input alas 
        alas_input = input("Masukkan panjang alas: ")
        if not alas_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        alas = float(alas_input)

        # Input tinggi 
        tinggi_input = input("Masukkan tinggi: ")
        if not tinggi_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        tinggi = float(tinggi_input)

        # Input sisi miring 
        sisi_miring_input = input("Masukkan panjang sisi miring: ")
        if not sisi_miring_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi_miring = float(sisi_miring_input)

        # Rumus luas dan keliling jajar genjang
        luas = alas * tinggi
        keliling = 2 * (alas + sisi_miring)

        # Hasil Output
        print("========================================")
        print("  HASIL LUAS & KELILING JAJAR GENJANG   ")
        print("========================================")
        print(f"Luas : {luas}")
        print(f"Keliling : {keliling}")
        print("========================================")
        ulang = input("Apakah Anda ingin menghitung jajar genjang lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung jajar genjang lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def hitung_luas_keliling_layang_layang():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===============================================")
        print("   MENGHITUNG LUAS & KELILING LAYANG-LAYANG    ")
        print("===============================================")

        # Input diagonal 1 
        diagonal1_input = input("Masukkan panjang diagonal 1: ")
        if not diagonal1_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        diagonal1 = float(diagonal1_input)

        # Input diagonal 2 
        diagonal2_input = input("Masukkan panjang diagonal 2: ")
        if not diagonal2_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        diagonal2 = float(diagonal2_input)

        # Input sisi 1 
        sisi1_input = input("Masukkan panjang sisi 1: ")
        if not sisi1_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi1 = float(sisi1_input)

        # Input sisi 2 
        sisi2_input = input("Masukkan panjang sisi 2: ")
        if not sisi2_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi2 = float(sisi2_input)

        # Rumus luas dan keliling layang-layang
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 2 * (sisi1 + sisi2)

        # Hasil Output
        print("===============================================")
        print("   HASIL LUAS & KELILING LAYANG-LAYANG    ")
        print("===============================================")
        print(f"Luas : {luas}")
        print(f"Keliling : {keliling}")
        print("===============================================")
        ulang = input("Apakah Anda ingin menghitung layang-layang lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung layang-layang lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def hitung_luas_keliling_trapesium():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=========================================")
        print("  MENGHITUNG LUAS & KELILING TRAPESIUM   ")
        print("=========================================")

        # Input panjang sisi atas
        sisi_atas_input = input("Masukkan panjang sisi atas: ")
        if not sisi_atas_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi_atas = float(sisi_atas_input)

        # Input panjang sisi bawah
        sisi_bawah_input = input("Masukkan panjang sisi bawah: ")
        if not sisi_bawah_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi_bawah = float(sisi_bawah_input)

        # Input tinggi
        tinggi_input = input("Masukkan tinggi trapesium: ")
        if not tinggi_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        tinggi = float(tinggi_input)

        # Input panjang sisi miring 1
        sisi_miring1_input = input("Masukkan panjang sisi miring 1: ")
        if not sisi_miring1_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi_miring1 = float(sisi_miring1_input)

        # Input panjang sisi miring 2
        sisi_miring2_input = input("Masukkan panjang sisi miring 2: ")
        if not sisi_miring2_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi_miring2 = float(sisi_miring2_input)

        # Rumus luas dan keliling trapesium
        luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
        keliling = sisi_atas + sisi_bawah + sisi_miring1 + sisi_miring2

        # Hasil Output
        print("=========================================")
        print("  HASIL LUAS & KELILING TRAPESIUM   ")
        print("=========================================")
        print(f"Luas : {luas}")
        print(f"Keliling : {keliling}")
        print("=========================================")
        ulang = input("Apakah Anda ingin menghitung trapesium lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung trapesium lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def submenu_hitung_bangun_ruang():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==============================")
        print("  MENGHITUNG BANGUN RUAMG     ")
        print("==============================")
        print("1. Kubus")
        print("2. Balok")
        print("3. Prisma Segitiga")
        print("4. Limas Persegi")
        print("5. Tabung")
        print("6. Kerucut")
        print("7. Bola")
        print("0. Kembali ke Menu Utama")
        pilihan_submenu = input("Masukkan Pilihan (0-8) : ")

        if pilihan_submenu == "1":
            hitung_bangun_ruang_kubus()
        elif pilihan_submenu == "2":
            hitung_bangun_ruang_balok()
        elif pilihan_submenu == "3":
            hitung_bangun_ruang_prisma_segitiga()
        elif pilihan_submenu == "4":
            hitung_bangun_ruang_limas_persegi()
        elif pilihan_submenu == "5":
            hitung_bangun_ruang_tabung()
        elif pilihan_submenu == "6":
            hitung_bangun_ruang_kerucut()
        elif pilihan_submenu == "7":
            hitung_bangun_ruang_bola()
        elif pilihan_submenu == "0":
            break
        else:
            print("Pilihan Menu tersebut tidak tersedia. Silakan memilih menu yang tersedia angka 0-8.")

def hitung_bangun_ruang_kubus():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=================================")
        print("  MENGHITUNG BANGUN RUANG KUBUS  ")
        print("=================================")

        # Input panjang sisi kubus
        sisi_input = input("Masukkan panjang sisi kubus: ")
        if not sisi_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue
        sisi = float(sisi_input)

        # Rumus volume, luas permukaan, dan keliling kubus
        volume = sisi ** 3
        luas_permukaan = 6 * sisi ** 2
        keliling = 12 * sisi

        # Hasil Output
        print("=================================")
        print("   HASIL BANGUN RUANG KUBUS      ")
        print("=================================")
        print(f"Volume kubus: {volume}")
        print(f"Luas permukaan kubus: {luas_permukaan}")
        print(f"Keliling kubus: {keliling}")
        print("=================================")
        ulang = input("Apakah Anda ingin menghitung kubus lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung kubus lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def hitung_bangun_ruang_balok():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=================================")
        print("  MENGHITUNG BANGUN RUANG BALOK  ")
        print("=================================")

        # Input panjang, lebar, dan tinggi balok
        panjang_input = input("Masukkan panjang balok: ")
        lebar_input = input("Masukkan lebar balok: ")
        tinggi_input = input("Masukkan tinggi balok: ")

        if not panjang_input.isdigit() or not lebar_input.isdigit() or not tinggi_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue

        panjang = float(panjang_input)
        lebar = float(lebar_input)
        tinggi = float(tinggi_input)

        # Rumus volume, luas permukaan, dan keliling balok
        volume = panjang * lebar * tinggi
        luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        keliling = 4 * (panjang + lebar + tinggi)

        # Hasil Output
        print("=======================================")
        print("    HASIL BANGUN RUANG RUANG BALOK     ")
        print("=======================================")
        print(f"Volume balok: {volume}")
        print(f"Luas permukaan balok: {luas_permukaan}")
        print(f"Keliling balok: {keliling}")
        print("=================================")
        ulang = input("Apakah Anda ingin menghitung balok lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung balok lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def hitung_bangun_ruang_prisma_segitiga():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===========================================")
        print("  MENGHITUNG BANGUN RUANG PRISMA SEGITIGA  ")
        print("===========================================")

        # Input panjang alas, tinggi alas, tinggi prisma
        alas_input = input("Masukkan panjang alas segitiga: ")
        tinggi_alas_input = input("Masukkan tinggi alas segitiga: ")
        tinggi_prisma_input = input("Masukkan tinggi prisma: ")

        if not alas_input.isdigit() or not tinggi_alas_input.isdigit() or not tinggi_prisma_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue

        alas = float(alas_input)
        tinggi_alas = float(tinggi_alas_input)
        tinggi_prisma = float(tinggi_prisma_input)

        # Rumus volume dan luas permukaan prisma segitiga
        volume = 0.5 * alas * tinggi_alas * tinggi_prisma
        luas_permukaan = alas * tinggi_alas + 3 * (0.5 * alas * tinggi_prisma)

        # Hasil Output
        print("======================================")
        print("  HASIL BANGUN RUANG PRISMA SEGITIGA  ")
        print("======================================")
        print(f"Volume prisma segitiga: {volume}")
        print(f"Luas permukaan prisma segitiga: {luas_permukaan}")
        print("==============================")
        ulang = input("Apakah Anda ingin menghitung prisma segitiga lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung prisma segitiga lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def hitung_bangun_ruang_limas_persegi():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===========================================")
        print("   MENGHITUNG BANGUN RUANG LIMAS PERSEGI   ")
        print("===========================================")

        # Input panjang sisi alas dan tinggi limas
        sisi_alas_input = input("Masukkan panjang sisi alas persegi: ")
        tinggi_limas_input = input("Masukkan tinggi limas: ")

        if not sisi_alas_input.isdigit() or not tinggi_limas_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue

        sisi_alas = float(sisi_alas_input)
        tinggi_limas = float(tinggi_limas_input)

        # Rumus volume dan luas permukaan limas persegi
        volume = (1/3) * sisi_alas**2 * tinggi_limas
        luas_permukaan = sisi_alas**2 + 4 * (0.5 * sisi_alas * tinggi_limas)

        # Hasil Output
        print("======================================")
        print("   HASIL BANGUN RUANG LIMAS PERSEGI   ")
        print("======================================")
        print(f"Volume limas persegi: {volume}")
        print(f"Luas permukaan limas persegi: {luas_permukaan}")
        print("======================================")
        ulang = input("Apakah Anda ingin menghitung limas persegi lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung limas persegi lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def hitung_bangun_ruang_tabung():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================")
        print("   MENGHITUNG RUANG BANGUN TABUNG   ")
        print("====================================")

        # Input jari-jari dan tinggi tabung
        jari_jari_input = input("Masukkan jari-jari tabung: ")
        tinggi_tabung_input = input("Masukkan tinggi tabung: ")

        if not jari_jari_input.isdigit() or not tinggi_tabung_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue

        jari_jari = float(jari_jari_input)
        tinggi_tabung = float(tinggi_tabung_input)

        # Rumus volume dan luas permukaan tabung
        volume = 3.14 * jari_jari**2 * tinggi_tabung
        luas_permukaan = 2 * 3.14 * jari_jari * (jari_jari + tinggi_tabung)

        # Hasil Output
        print("====================================")
        print("   HASIL RUANG BANGUN TABUNG        ")
        print("====================================")
        print(f"Volume tabung: {volume}")
        print(f"Luas permukaan tabung: {luas_permukaan}")
        print("====================================")
        ulang = input("Apakah Anda ingin menghitung tabung lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung tabung lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def hitung_bangun_ruang_kerucut():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=====================================")
        print("   MENGHITUNG BANGUN RUANG KERUCUT   ")
        print("=====================================")

        # Input jari-jari dan tinggi kerucut
        jari_jari_kerucut_input = input("Masukkan jari-jari kerucut: ")
        tinggi_kerucut_input = input("Masukkan tinggi kerucut: ")

        if not jari_jari_kerucut_input.isdigit() or not tinggi_kerucut_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue

        jari_jari_kerucut = float(jari_jari_kerucut_input)
        tinggi_kerucut = float(tinggi_kerucut_input)

        # Rumus volume dan luas permukaan kerucut
        volume_kerucut = (1/3) * 3.14 * jari_jari_kerucut**2 * tinggi_kerucut
        luas_permukaan_kerucut = 3.14 * jari_jari_kerucut * (jari_jari_kerucut + (jari_jari_kerucut**2 + tinggi_kerucut**2)**0.5)

        # Hasil Output
        print("=====================================")
        print("   HASIL BANGUN RUANG KERUCUT   ")
        print("=====================================")
        print(f"Volume kerucut: {volume_kerucut}")
        print(f"Luas permukaan kerucut: {luas_permukaan_kerucut}")
        print("=====================================")
        ulang = input("Apakah Anda ingin menghitung kerucut lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung kerucut lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def hitung_bangun_ruang_bola():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=====================================")
        print("     MENGHITUNG BANGUN RUANG BOLA    ")
        print("=====================================")

        # Input jari-jari bola
        jari_jari_bola_input = input("Masukkan jari-jari bola: ")

        if not jari_jari_bola_input.isdigit():
            print("Masukkan harus berupa angka.")
            continue

        jari_jari_bola = float(jari_jari_bola_input)

       
        volume_bola = (4/3) * 3.14 * jari_jari_bola**3
        luas_permukaan_bola = 4 * 3.14 * jari_jari_bola**2

      
        print("=====================================")
        print("     HASIL BANGUN RUANG BOLA         ")
        print("=====================================")
        print(f"Volume bola: {volume_bola}")
        print(f"Luas permukaan bola: {luas_permukaan_bola}")
        print("=====================================")
        ulang = input("Apakah Anda ingin menghitung bola lagi? (y/n): ")
        while ulang.lower() not in ('y', 'n'):
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
            ulang = input("Apakah Anda ingin menghitung bola lagi? (y/n): ")

        if ulang.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif ulang.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            break



while True:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("==========================")
    print("  Silahkan Memilih Menu   ")
    print("==========================")
    print("1. [TASK] Pertemuan 1")
    print("2. [TASK] Pertemuan 2")
    print("3. [TASK] Pertemuan 3")
    print("0. Keluar")
    print("==========================")
    pilihan = input("Masukan Pilihan (0-3) : ")
    
    if pilihan == "1":
        menu_pertemuan_1()
    elif pilihan == "2":
        menu_pertemuan_2()
    elif pilihan == "3":
        menu_pertemuan_3()
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

