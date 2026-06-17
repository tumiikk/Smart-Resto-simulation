from utils.handler import load_data, save_data
from views.menu_view import tampilkan_menu
from views.antrian_view import tampilkan_antrian
from views.stok_view import tampilkan_stok
from views.dapur_view import tampilkan_dapur
from views.delivery_view import tampilkan_rute, tampilkan_graph

from services.pesanan_service import proses_pesanan
from services.dapur_service import tambah_ke_dapur, lihat_dapur, pesanan_selesai
from services.delivery_service import kirim_pesanan

from modules.stack_undo import pop as undo_stack


def menu_utama():
    print("\n=== SMART RESTO SYSTEM ===")
    print("1. Lihat Menu")
    print("2. Lihat Antrian")
    print("3. Pesan Makanan")
    print("4. Undo Pesanan")
    print("5. Lihat Dapur")
    print("6. Selesaikan Pesanan Dapur")
    print("7. Kirim Pesanan (Delivery)")
    print("8. Lihat Stok")
    print("9. Lihat Peta Delivery")
    print("0. Keluar")


def main():
    while True:
        data = load_data()
        menu_utama()
        pilihan = input("Pilih menu: ")

        # 1. TREE → tampilkan menu
        if pilihan == "1":
            tampilkan_menu(data["kategori_menu_tree"])

        # 2. QUEUE → tampilkan antrian
        elif pilihan == "2":
            tampilkan_antrian(data["antrean_pelanggan_queue"])

        # 3. PESAN → dict + queue + stack
        elif pilihan == "3":
            nama_menu = input("Masukkan nama menu: ")
            hasil = proses_pesanan(nama_menu)
            print(hasil)

            # kalau berhasil → masuk dapur
            if "berhasil" in hasil:
                tambah_ke_dapur(nama_menu)

        # 4. STACK → undo
        elif pilihan == "4":
            pesanan_batal = undo_stack(data["riwayat_pesanan_stack"])

            if pesanan_batal:
                print(f"Pesanan dibatalkan: {pesanan_batal}")
                save_data(data)
            else:
                print("Tidak ada pesanan untuk di-undo")

        # 5. LINKED LIST → lihat dapur
        elif pilihan == "5":
            daftar = lihat_dapur()
            tampilkan_dapur(daftar)

        # 6. LINKED LIST → selesai
        elif pilihan == "6":
            print(pesanan_selesai())

        # 7. GRAPH → delivery
        elif pilihan == "7":
            tujuan = input("Masukkan tujuan (contoh: Area_M): ")
            rute = kirim_pesanan(tujuan)
            tampilkan_rute(rute)

        # 8. DICT → stok
        elif pilihan == "8":
            tampilkan_stok(data["stok_bahan_dict"])

        # 9. GRAPH → tampilkan peta
        elif pilihan == "9":
            tampilkan_graph(data["peta_delivery_graph"])

        elif pilihan == "0":
            print("Keluar dari sistem...")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()