from datetime import datetime

print("=== SOAL 2: LOG AKTIVITAS SEDERHANA ===")

# Ambil waktu sekarang dalam format jam:menit
timestamp = datetime.now().strftime("%H:%M")

# Bentuk teks log
baris_log = f"[{timestamp}] Program dijalankan\n"

# Tambahkan ke file log.txt (append mode)
with open("log.txt", "a") as f:
    f.write(baris_log)

print("Log baru ditambahkan ke log.txt:")
print(baris_log)

# (Opsional) tampilkan semua isi log
print("=== ISI log.txt SAAT INI ===")
with open("log.txt", "r") as f:
    print(f.read())
