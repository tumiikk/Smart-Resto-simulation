def tampilkan_antrian(queue):
    print("=== ANTRIAN PELANGGAN ===")

    if not queue:
        print("Antrian kosong")
        return

    for i, nama in enumerate(queue, start=1):
        print(f"{i}. {nama}")