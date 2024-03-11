import os


def rename_files(folder_path):
    # Mendapatkan daftar file dalam folder
    files = os.listdir(folder_path)

    # Inisialisasi nomor urut
    counter = 51

    # Iterasi melalui setiap file
    for file_name in files:
        # Mendapatkan ekstensi file
        _, file_extension = os.path.splitext(file_name)

        # Membuat nama file baru dengan format yang diinginkan
        new_file_name = f"1207070132_ZIDAN NURYAWAN P_{counter}{file_extension}"

        # Mendapatkan path file lama dan baru
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)

        # Melakukan rename file
        os.rename(old_path, new_path)

        # Increment nomor urut
        counter += 1


# Ganti 'path/to/subfolder' dengan path menuju subfolder yang ingin diubah
folder_path = "D:/KULIAH/TUGAS AKHIR/THE PROJECT/.dataset warga wargi/datawajah_zidan_2/zidan-nuryawan-pratomo"
rename_files(folder_path)
