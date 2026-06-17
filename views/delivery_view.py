def tampilkan_graph(graph):
    print("=== PETA DELIVERY ===")

    for node, tetangga in graph.items():
        print(f"{node} -> {', '.join(tetangga)}")


def tampilkan_rute(rute):
    print("=== RUTE PENGIRIMAN ===")

    if not rute:
        print("Rute tidak ditemukan")
        return

    print(" -> ".join(rute))