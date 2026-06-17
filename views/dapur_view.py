def tampilkan_dapur(daftar_pesanan):
    print("=== DAFTAR PESANAN DI DAPUR ===")

    if not daftar_pesanan:
        print("Belum ada pesanan")
        return

    for i, pesanan in enumerate(daftar_pesanan, start=1):
        print(f"{i}. {pesanan}")