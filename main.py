from linked_list import DoubleLinkedList

dll = DoubleLinkedList()

def menu():
    while True:
        print("\n=== PROGRAM MANAJEMEN DATA MAHASISWA ===")
        print("1. Tambah di Awal")
        print("2. Tambah di Akhir")
        print("3. Tambah Urut NIM")
        print("4. Hapus Data by NIM")
        print("5. Cari Data by NIM")
        print("6. Tampilkan Semua Data")
        print("0. Keluar")
        print("=" * 45)

        pilih = input("Pilih menu: ")

        if pilih in ['1', '2', '3']:
            nim =input("Masukkan NIM : ")
            nama = input("Masukkan Nama: ")
            jurusan = input("Masukkan Jurusan: ")
            if pilih == '1':
                dll.tambah_awal(nim, nama, jurusan)
            elif pilih == '2':
                dll.tambah_akhir(nim, nama, jurusan)
            elif pilih == '3':
                dll.tambah_urut_nim(nim, nama, jurusan)

        elif pilih == '4':
            nim = (input("Masukkan NIM yang akan dihapus: "))
            dll.hapus_nim(nim)

        elif pilih == '5':
            nim = (input("Masukkan NIM yang dicari: "))
            hasil = dll.cari_nim(nim)
            if hasil:
                print(f"✅ DITEMUKAN: {hasil.nim} - {hasil.nama} - {hasil.jurusan}")
            else:
                print("❌ Data tidak ditemukan")

        elif pilih == '6':
            dll.tampilkan()

        elif pilih == '0':
            print("👋 Terima kasih!")
            break

        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    menu()