from datetime import datetime

jumlah = int(input("Masukkan jumlah mahasiswa: "))

with open("nilaimahasiswa.txt", "w") as file:
    for i in range(jumlah):
        nama = input(f"Nama mahasiswa ke-{i+1}: ")
        tugas = float(input(f"Nilai Tugas {nama}: "))
        uts = float(input(f"Nilai UTS {nama}: "))
        uas = float(input(f"Nilai UAS {nama}: "))

        file.write(f"{nama}, {tugas}, {uts}, {uas}\n")

print("\nData berhasil disimpan.\n")
print("Nama                Tugas      UTS        UAS        Rata-rata")
print("-"*60)

with open("nilaimahasiswa.txt", "r") as file:
    for line in file:
        nama, tugas, uts, uas = line.strip().split(",")
        t = float(tugas)
        u1 = float(uts)
        u2 = float(uas)

        rata = (t + u1 + u2) / 3
        print(f"{nama:<20} {t:<10.0f} {u1:<10.0f} {u2:<10.0f} {rata:<10.2f}")

log = datetime.now().strftime("Data disimpan pada tanggal %Y-%m-%d dan jam %H:%M\n")

with open("nilaimahasiswa.txt", "a") as file:
    file.write(log)
