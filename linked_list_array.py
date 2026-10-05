class Node:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        # TAMBAHAN ARRAY
        self.array_data = [] 

    def tambah_awal(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        
        # Masukkin ke array juga
        self.array_data.append({"nim": nim, "nama": nama, "jurusan": jurusan})
        print(f"[LinkedList & Array] Berhasil tambah {nama} di awal.")

    def tambah_akhir(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        
        self.array_data.append({"nim": nim, "nama": nama, "jurusan": jurusan})
        print(f"[LinkedList & Array] Berhasil tambah {nama} di akhir.")

    def tambah_urut(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if not self.head or nim < self.head.nim:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.nim < nim:
                curr = curr.next
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node

        # TAMBAHAN ARRAY: simpan dan urutkan by NIM
        self.array_data.append({"nim": nim, "nama": nama, "jurusan": jurusan})
        self.array_data = sorted(self.array_data, key=lambda x: x["nim"])
        print(f"[LinkedList & Array] Berhasil tambah {nama} secara urut NIM.")

    def hapus_nim(self, nim):
        if not self.head:
            print("Data masih kosong.")
            return
        curr = self.head
        while curr and curr.nim != nim:
            curr = curr.next
        if not curr:
            print(f"NIM {nim} tidak ditemukan.")
            return
        
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev

        # Hapus dari array juga
        self.array_data = [m for m in self.array_data if m["nim"] != nim]
        print(f"[LinkedList & Array] NIM {nim} berhasil dihapus.")

    def tampil_linkedlist(self):
        print("\n--- Tampil dari DOUBLE LINKED LIST ---")
        if not self.head:
            print("Kosong")
            return
        curr = self.head
        while curr:
            print(f"{curr.nim} | {curr.nama} | {curr.jurusan}")
            curr = curr.next

    def tampil_array(self):
        print("\n--- Tampil dari ARRAY ---")
        if not self.array_data:
            print("Array kosong")
            return
        for m in self.array_data:
            print(f"{m['nim']} | {m['nama']} | {m['jurusan']}")
        print(f"Total di array: {len(self.array_data)} data")

    def cari_di_array(self, nim):
        # Pencarian di array lebih cepat untuk contoh
        for m in self.array_data:
            if m["nim"] == nim:
                print(f"Ditemukan di ARRAY: {m}")
                return m
        print(f"NIM {nim} tidak ada di ARRAY")
        return None

# === PROGRAM UTAMA ===
if __name__ == "__main__":
    dll = DoubleLinkedList()
    
    # Contoh input
    dll.tambah_urut(2301, "rini faku", "Pendidikan Informatika")
    dll.tambah_urut(2305, "livi", "Sistem Informasi")
    dll.tambah_urut(2302, "paman", "Teknik Informasi")

    dll.tampil_linkedlist()
    dll.tampil_array()

    dll.cari_di_array(2302)
    dll.hapus_nim(2305)
    dll.tampil_array()