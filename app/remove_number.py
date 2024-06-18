import re

# Fungsi untuk menghapus angka menggunakan regex
def remove_numbers(value):
    return re.sub(r'\d+', '', value)