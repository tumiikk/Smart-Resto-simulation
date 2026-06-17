def tampilkan_stok(stok):
    print("=== STOK BAHAN ===")

    for bahan, jumlah in stok.items():
        print(f"{bahan} : {jumlah}")