from modules.tree_menu import cari_menu_by_nama
from modules.dictionary_stok import kurangi_stok
from modules.queue_antrian import dequeue
from modules.stack_undo import push
from utils.handler import load_data, save_data


# mapping sederhana bahan (biar realistis)
RESEP = {
    "Ayam Goreng": {"Ayam": 1, "Minyak Goreng": 1},
    "Steak Sapi": {"Daging Sapi": 1, "Garam": 1},
    "Kopi Susu": {"Kopi": 1, "Susu": 1, "Gula": 1},
    "Es Teh Manis": {"Teh": 1, "Gula": 1},
    "Jus Jeruk": {"Jeruk": 2},
}


def proses_pesanan(nama_menu):
    data = load_data()

    # ambil pelanggan dari antrian
    pelanggan = dequeue(data["antrean_pelanggan_queue"])
    if not pelanggan:
        return "Tidak ada antrian"

    # cari menu
    menu = cari_menu_by_nama(data["kategori_menu_tree"], nama_menu)
    if not menu:
        return "Menu tidak ditemukan"

    # ambil resep
    bahan = RESEP.get(nama_menu, {})

    # cek & kurangi stok
    if not kurangi_stok(data["stok_bahan_dict"], bahan):
        return "Stok tidak cukup"

    # simpan ke riwayat (stack)
    push(data["riwayat_pesanan_stack"], nama_menu)

    save_data(data)

    return f"Pesanan {nama_menu} untuk {pelanggan} berhasil"