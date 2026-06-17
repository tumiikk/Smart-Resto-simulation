from modules.graph_delivery import bfs_rute_terdekat
from utils.handler import load_data


def kirim_pesanan(tujuan):
    data = load_data()

    graph = data["peta_delivery_graph"]

    rute = bfs_rute_terdekat(graph, "Restoran", tujuan)

    if not rute:
        return None

    return rute