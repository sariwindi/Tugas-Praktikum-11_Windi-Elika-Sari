import datetime
import random
import string

# Templat dictionary untuk data buku
buku_template = {
    "judul": "judul",
    "penulis": "penulis",
    "tahun_terbit": 0000,
    "tanggal_pinjam": datetime.datetime(1111, 1, 11),
    "status": "TERSEDIA"
}

# Dictionary utama untuk menyimpan seluruh data buku (Nesting Dictionary)
data_perpustakaan = {}

while True:
    print("\n" + "="*45)
    print(f"{"SISTEM MANAJEMEN PERPUSTAKAAN":^45}")
    print("="*45)

    # Membuat dictionary baru dari templet
    buku = dict.fromkeys(buku_template.keys())

    # input data buku dari pengguna
    buku["judul"] = input("Judul Buku\t\t: ")
    buku["penulis"] = input("Penulis\t\t\t: ")
    buku["tahun_terbit"] = int(input("Tahun Terbit (YYYY)\t: "))

    print("\n--- Tanggal Terakhir Pinjam ---")
    tahun = int(input("Tahun (YYYY)\t\t: "))
    bulan = int(input("Bulan (1-12)\t\t: "))
    tanggal = int(input("Tanggal (1-31)\t\t: "))
    buku["tanggal_pinjam"] = datetime.datetime(tahun, bulan, tanggal)

    status_input = input("Status (TERSEDIA/TIDAK)\t: ").upper()
    buku["status"] = status_input if status_input in ["TERSEDIA", "TIDAK"] else "TERSEDIA"

    # Generate KEY acak sebanyak 6 karakter huruf kapital (Multi-Keys)
    KEY = " ".join((random.choice(string.ascii_uppercase) for i in range(6)))

    #  Memasukkan data buku ke dalam dictionary utama 
    data_perpustakaan.update({KEY: buku})

    # Menampilkan seluruh data buku dalam format tabel rapi
    print("\n" + "="*88)
    print(f"{"KEY":<8} {"JUDUL BUKU":<22} {"PENULIS":<18} {"TAHUN":<6} {"TGL PINJAM":<12} {"STATUS":<18}")
    print("_"*88)

    for key in data_perpustakaan:
         KEY_BUKU = key
         JUDUL = data_perpustakaan[KEY_BUKU]["judul"]
         PENULIS = data_perpustakaan[KEY_BUKU]["penulis"]
         TAHUN = data_perpustakaan[KEY_BUKU]["tahun_terbit"]
         TGL_PINJAM = data_perpustakaan[KEY_BUKU]["tanggal_pinjam"].strftime("%x")
         STATUS = data_perpustakaan[KEY_BUKU]["status"]

         print(f"{KEY_BUKU:<8} {JUDUL:<22} {PENULIS:<18} {TAHUN:<6} {TGL_PINJAM:<12} {STATUS:<18}")

    print("="*88)

    # Konfirmasiu untuk menambah data lagi
    lanjut = input("\nApakah ingin menambah buku lagi? (y/n): ").lower()
    if lanjut == "n":
         break

print("\nProgram selesai. Terima kasih!")

