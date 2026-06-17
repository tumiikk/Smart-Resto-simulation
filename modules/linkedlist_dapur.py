class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Dapur:
    def __init__(self):
        self.head = None

    def tambah_pesanan(self, pesanan):
        node_baru = Node(pesanan)

        if not self.head:
            self.head = node_baru
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node_baru

    def hapus_pesanan(self):
        if self.head:
            self.head = self.head.next

    def get_semua_pesanan(self):
        hasil = []
        temp = self.head

        while temp:
            hasil.append(temp.data)
            temp = temp.next

        return hasil