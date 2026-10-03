class Node:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # 1. Tambah di Awal
    def tambah_awal(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(f"-> Berhasil tambah {nama} di AWAL")

    # 2. Tambah di Akhir
    def tambah_akhir(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
        print(f"-> Berhasil tambah {nama} di AKHIR")

    # 3. Tambah Urut NIM
    def tambah_urut_nim(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if not self.head or nim < self.head.nim:
            self.tambah_awal(nim, nama, jurusan)
            return
        curr = self.head
        while curr.next and curr.next.nim < nim:
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        print(f"-> Berhasil tambah {nama} secara URUT NIM")

    # 4. Hapus berdasarkan NIM
    def hapus_nim(self, nim):
        if not self.head:
            print("Data kosong")
            return
        curr = self.head
        while curr and curr.nim != nim:
            curr = curr.next
        if not curr:
            print(f"NIM {nim} tidak ditemukan")
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        print(f"-> Berhasil hapus NIM {nim}")

    # 5. Cari berdasarkan NIM
    def cari_nim(self, nim):
        curr = self.head
        while curr is not None :
            if curr.nim == nim:
                return curr
            curr = curr.next
        return None

    # 6. Tampilkan semua data
    def tampilkan(self):
        if not self.head:
            print("Belum ada data mahasiswa")
            return
        print("\n=== DAFTAR MAHASISWA ===")
        print(f"{'NIM':<15} | {'Nama':<20} | {'Jurusan':<15}")
        print("-" * 55)
        curr = self.head
        while curr:
            print(f"{curr.nim:<15} | {curr.nama:<20} | {curr.jurusan:<15}")
            curr = curr.next
        print("-" * 55)