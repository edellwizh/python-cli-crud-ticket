import random
from datetime import datetime

kode_booking = ""
nama_penumpang = ""
no_hp = ""
kelas_kereta = ""
tanggal_berangkat = ""
total_harga = 0

while True:
    print("=== SELAMAT DATANG ===")
    print("1. Pesan Tiket Baru")
    print("2. Cek Detail Tiket")
    print("3. Reschedule dan Ubah Kelas")
    print("4. Batalkan Tiket")
    print("5. Keluar Program")
    input_pilihan = input("Masukkan Pilihan: ")

    match input_pilihan.strip():
        case "1":
            while True:
                input_nama = input("Nama Penumpang: ")

                check_nama = input_nama.replace(" ", "")
                if len(input_nama) >= 3 and len(input_nama) <= 30 and input_nama.istitle() and len(input_nama.strip().split(" ")) > 1 and check_nama.isalpha():
                    nama_penumpang = input_nama.strip()
                    break
                print("Input tidak valid")

            while True:
                input_hp = input("Nomor Telepon: ")

                if input_hp.isdigit() and input_hp.startswith("08") and 10 <= len(input_hp) <= 13:
                    no_hp = input_hp.strip()
                    break
                print("Input tidak valid")

            while True:
                input_tanggal = input("Tanggal Berangkat (1-31): ")

                if input_tanggal.isdecimal() and 1 <= int(input_tanggal) <= 31:
                    tanggal_berangkat = input_tanggal.strip()

                    break
                print("Input tidak valid")

            while True:
                input_kelas = input("Kelas Kereta (Ekonomi/Bisnis/Eksekutif): ")

                match input_kelas.lower():
                    case "ekonomi":
                        kelas_kereta = "Ekonomi"
                        total_harga = 150000
                        break
                
                    case "bisnis":
                        kelas_kereta = "Bisnis"
                        total_harga = 300000
                        break
                    
                    case "eksekutif":
                        kelas_kereta = "Eksekutif"
                        total_harga = 500000
                        break

                    case _:
                        print("Input tidak valid")

            tahun_sekarang = datetime.now().year 
            kode_booking = "KAI-" + str(tahun_sekarang) + "-" + kelas_kereta[0] + "-" + str(random.randint(100, 999))
            
            print("Data Berhasil di tambahkan")
            input("Tekan Enter untuk lanjut...")

        case "2":
            if kode_booking == "":
                print("Data Kosong")
                input("Tekan Enter untuk lanjut...")
            else:
                print("=== CEK DETAIL TIKET ===")
                print(f"Kode Booking: {kode_booking}")
                print(f"Nama Penumpang: {nama_penumpang}")
                print(f"Kelas Kereta: {kelas_kereta}")
                print(f"Total Harga: Rp {total_harga}")
                bulan_tanggal = datetime.now().strftime("%B %Y")
                print("Tanggal Keberangkatan:", tanggal_berangkat, bulan_tanggal)
                print("Nomor Telepon:", no_hp[:4] + "*" * (len(no_hp) - 6) + no_hp[-2:] )
                input("Tekan Enter untuk lanjut...")

        case "3":
            if kode_booking == "":
                print("Data Kosong")
                input("Tekan Enter untuk lanjut...")
            else:
                print(f"Kode Booking: {kode_booking}")
                print(f"Nama Penumpang: {nama_penumpang}")
                print(f"Kelas Kereta: {kelas_kereta}")
                print(f"Total Harga: Rp {total_harga}")
                bulan_tanggal = datetime.now().strftime("%B %Y")
                print("Tanggal Keberangkatan:", tanggal_berangkat, bulan_tanggal)
                print("Nomor Telepon:", no_hp[:4] + "*" * (len(no_hp) - 6) + no_hp[-2:] )

                print(" ")
                while True:
                    print("[1. Nama Penumpang 2. Kelas Kereta 3. Tanggal Keberangkatan 4. Nomor Telepon  5. Balik ke menu utama]")
                    input_pilihan = input(">> ")

                    match input_pilihan.strip():
                        case "1":
                            while True:
                                input_nama = input("Nama Lengkap: ")

                                check_nama = input_nama.replace(" ", "")
                                if check_nama.isalpha() and 3 <= len(input_nama) <= 30 and input_nama.istitle() and len(input_nama.strip().split(" ")) > 1 and input_nama.istitle:
                                    nama_penumpang = input_nama.strip()
                                    break
                                print("Input tidak valid")

                        case "2":
                            while True:
                                input_kelas = input("Kelas Kereta (Ekonomi/Bisnis/Eksekutif): ")
                                match input_kelas.lower():
                                    case "ekonomi":
                                        kelas_kereta = "Ekonomi"
                                        total_harga = 150000
                                        break
                                    case "bisnis":
                                        kelas_kereta = "Bisnis"
                                        total_harga = 300000
                                        break
                                    case "eksekutif":
                                        kelas_kereta = "Eksekutif"
                                        total_harga = 500000
                                        break
                                    case _:
                                        print("Input tidak valid")

                        case "3":
                            while True:
                                input_tanggal = input("Tanggal Keberangkatan (1-31): ")

                                if 1 <= int(input_tanggal) <= 31 and input_tanggal.isnumeric():
                                    tanggal_berangkat = input_tanggal.strip()
                                    break
                                print("Input tidak valid")


                        case "4":
                            while True:
                                input_hp = input("Nomor Telepon: ")

                                if input_hp.isdigit and input_hp.startswith("08") and 10 <= len(input_hp) <= 13:
                                    no_hp = input_hp.strip()
                                    break
                                print("Input tidak valid")

                            tahun_sekarang = datetime.now().year 
                            kode_booking = "KAI-" + str(tahun_sekarang) + "-" + kelas_kereta[0] + "-" + str(random.randint(100, 999))
                            input("Tekan Enter untuk lanjut...")

                        case "5":
                            break

                        case _:
                            print("Input tidak valid")

        case "4":
            print("=== BATALKAN TIKET ===")
            if kode_booking == "":
                print("Data Kosong")
                input("Tekan Enter untuk lanjut...")
            else:
                print(f"Kode Booking: {kode_booking}")
                print(f"Nama Penumpang: {nama_penumpang}")
                print(f"Kelas Kereta: {kelas_kereta}")
                print(f"Total Harga: Rp {total_harga}")
                bulan_tanggal = datetime.now().strftime("%B %Y")
                print("Tanggal Keberangkatan:", tanggal_berangkat, bulan_tanggal)
                print("Nomor Telepon:", no_hp[:4] + "*" * (len(no_hp) - 6) + no_hp[-2:] )
                konfirmasi = input("Apakah yakin ingin menghapus (y/n): ")

                match konfirmasi.lower():
                    case "y":
                        kode_booking = ""
                        nama_penumpang = ""
                        no_hp = ""
                        kelas_kereta = ""
                        tanggal_berangkat = ""
                        total_harga = 0
                        print("Data berhasil dihapus")
                        print("Terima Kasih")
                        break
                    case "n":
                        print("Data cancel dihapus")
                    case _:
                        print("Input tidak valid")

        case "5":
            print("Terima Kasih")
            break

        case _:
            print("Input tidak valid")