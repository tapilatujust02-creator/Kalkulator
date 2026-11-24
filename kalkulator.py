def kalkulator_gaji():
    print("==========================================")
    print("        Kalkulator Penghitungan Gaji")
    print("==========================================")
    
    nama = input("Masukkan nama pegawai: ")
    
    try:
        lama_bekerja_str = input("Masukkan lama bekerja (bulan): ")
        lama_bekerja = int(lama_bekerja_str)
        
        gaji_pokok_str = input("Masukkan gaji pokok: ")
        gaji_pokok = float(gaji_pokok_str)
        
        if lama_bekerja >= 24:
            persentase_bonus = 0.25
        elif lama_bekerja >= 12:
            persentase_bonus = 0.15
        elif lama_bekerja >= 0:
            persentase_bonus = 0.0
        else:
            print("Inputan yang Anda masukkan tidak valid.")
            return

        bonus = gaji_pokok * persentase_bonus
        total_gaji = gaji_pokok + bonus
        
        print("\n------------------------------------------")
        print(f"Bonus yang anda dapatkan sebanyak: {bonus}")
        print("------------------------------------------")
        print(f"Total penghitungan gaji anda adalah: {total_gaji}")

    except ValueError:
        print("Inputan yang Anda masukkan tidak valid.")

if __name__ == "__main__":
    kalkulator_gaji()