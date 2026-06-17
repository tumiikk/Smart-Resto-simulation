from modules.linkedlist_dapur import Dapur

# dapur dibuat global (biar persist selama program jalan)
dapur = Dapur()


def tambah_ke_dapur(pesanan):
    dapur.tambah_pesanan(pesanan)
    return f"{pesanan} masuk ke dapur"


def pesanan_selesai():
    dapur.hapus_pesanan()
    return "Pesanan selesai"


def lihat_dapur():
    return dapur.get_semua_pesanan()