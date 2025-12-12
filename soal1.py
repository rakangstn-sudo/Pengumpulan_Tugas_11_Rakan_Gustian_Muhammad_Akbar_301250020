import os

os.system("cls" if os.name == "nt" else "clear")
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
prodi = input("Masukkan Prodi: ")

with open("biodata.txt", "w") as file:
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Prodi: {prodi}\n")

print(f"\nHalo {nama}, biodata kamu sudah disimpan.\n")

with open("biodata.txt", "r") as file:
    print("Isi file biodata:")
    print(file.read())
