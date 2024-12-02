data_mahasiswa = []

def tambah():
    nama = input("Masukkan Nama Mahasiswa: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    data_mahasiswa.append({
        "Nama": nama,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    })
    print("Data berhasil ditambahkan!")

def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    print("\nDaftar Nilai Mahasiswa:")
    print("="*77)
    print(f"| {'Nama':^15} | {'Tugas':^5} | {'UTS':^5} | {'UAS':^5} | {'Akhir':^7} |")
    print("="*77)
    for mahasiswa in data_mahasiswa:
        print(f"| {mahasiswa['Nama']:^15} | {mahasiswa['Tugas']:^5} | {mahasiswa['UTS']:^5} | {mahasiswa['UAS']:^5} | {mahasiswa['Nilai Akhir']:^7.2f} |")
    print("="*77)

def hapus(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa["Nama"].lower() == nama.lower():
            data_mahasiswa.remove(mahasiswa)
            print(f"Data mahasiswa {nama} berhasil dihapus!")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa["Nama"].lower() == nama.lower():
            print("Data ditemukan. Silakan masukkan data baru.")
            mahasiswa["Tugas"] = float(input("Masukkan Nilai Tugas Baru: "))
            mahasiswa["UTS"] = float(input("Masukkan Nilai UTS Baru: "))
            mahasiswa["UAS"] = float(input("Masukkan Nilai UAS Baru: "))
            mahasiswa["Nilai Akhir"] = (mahasiswa["Tugas"] * 0.3) + (mahasiswa["UTS"] * 0.35) + (mahasiswa["UAS"] * 0.35)
            print("Data berhasil diubah!")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

while True:
    print("\nMenu:")
    print("[T]ambah, [L]ihat, [U]bah, [H]apus, [K]eluar")
    pilihan = input("Pilih menu: ").lower()

    if pilihan == "t":
        tambah()
    elif pilihan == "l":
        tampilkan()
    elif pilihan == "u":
        nama = input("Masukkan Nama Mahasiswa yang ingin diubah: ")
        ubah(nama)
    elif pilihan == "h":
        nama = input("Masukkan Nama Mahasiswa yang ingin dihapus: ")
        hapus(nama)
    elif pilihan == "k":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
