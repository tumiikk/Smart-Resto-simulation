def cek_stok(stok, bahan):
    return stok.get(bahan, 0)


def cek_banyak_bahan(stok, daftar_bahan):
    for bahan, jumlah in daftar_bahan.items():
        if stok.get(bahan, 0) < jumlah:
            return False
    return True


def kurangi_stok(stok, daftar_bahan):
    if cek_banyak_bahan(stok, daftar_bahan):
        for bahan, jumlah in daftar_bahan.items():
            stok[bahan] -= jumlah
        return True
    return False