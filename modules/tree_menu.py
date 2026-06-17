def get_all_menu(node):
    hasil = []

    if "sub" in node:
        for child in node["sub"]:
            hasil.extend(get_all_menu(child))
    else:
        hasil.append({
            "nama": node["nama"],
            "harga": node["harga"],
            "kode": node["kode"]
        })

    return hasil


def cari_menu_by_nama(node, nama):
    if node.get("nama") == nama and "harga" in node:
        return node

    if "sub" in node:
        for child in node["sub"]:
            hasil = cari_menu_by_nama(child, nama)
            if hasil:
                return hasil

    return None


def cari_menu_by_kode(node, kode):
    if node.get("kode") == kode:
        return node

    if "sub" in node:
        for child in node["sub"]:
            hasil = cari_menu_by_kode(child, kode)
            if hasil:
                return hasil
