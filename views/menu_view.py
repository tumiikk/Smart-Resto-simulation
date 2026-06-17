def tampilkan_menu(node, level=0):
    indent = "  " * level

    # kalau kategori
    if "sub" in node:
        print(f"{indent}{node['nama']}")
        for child in node["sub"]:
            tampilkan_menu(child, level + 1)
    else:
        # kalau menu item
        print(f"{indent}- {node['nama']} (Rp{node['harga']}) [{node['kode']}]")