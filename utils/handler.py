import json
import os

FILE_PATH = "data/data_resto.json"


def load_data():
    """
    Membaca data dari file JSON
    """
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError("File data_resto.json tidak ditemukan")

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_data(data):
    """
    Menyimpan data ke file JSON
    """
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def reset_data(default_data):
    """
    Reset data ke kondisi awal (opsional, buat testing/demo)
    """
    save_data(default_data)


def update_section(section, value):
    """
    Update bagian tertentu saja (misal stok / antrian)
    """
    data = load_data()
    data[section] = value
    save_data(data)


def get_section(section):
    """
    Ambil bagian tertentu dari JSON
    """
    data = load_data()
    return data.get(section, None)