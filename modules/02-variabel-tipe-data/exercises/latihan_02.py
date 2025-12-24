# ============================================
# LATIHAN: Variabel & Tipe Data
# Module 02
# ============================================

"""
INSTRUKSI:
Selesaikan semua latihan di bawah ini.
Jalankan program untuk mengecek hasil Anda.
"""

print("="*60)
print("        LATIHAN MODULE 02: VARIABEL & TIPE DATA")
print("="*60)

# ============================================
# LATIHAN 1: Deklarasi Variabel
# ============================================
print("\n--- LATIHAN 1: Deklarasi Variabel ---")

# TODO: Buat variabel berikut dengan informasi Anda:
# - nama_lengkap (string)
# - umur (integer)
# - tinggi_badan (float, dalam cm)
# - berat_badan (float, dalam kg)
# - kota_asal (string)
# - is_student (boolean)

# Contoh:
# nama_lengkap = "Budi Santoso"
# umur = 20
# (lanjutkan...)

nama_lengkap = "Nama Anda"  # Ganti dengan nama Anda
umur = 0  # Ganti dengan umur Anda
tinggi_badan = 0.0  # Ganti dengan tinggi Anda
berat_badan = 0.0  # Ganti dengan berat Anda
kota_asal = "Kota Anda"  # Ganti dengan kota Anda
is_student = True  # Apakah Anda siswa/mahasiswa?

# Print hasil
print(f"Nama         : {nama_lengkap}")
print(f"Umur         : {umur} tahun")
print(f"Tinggi Badan : {tinggi_badan} cm")
print(f"Berat Badan  : {berat_badan} kg")
print(f"Kota Asal    : {kota_asal}")
print(f"Status       : {'Siswa/Mahasiswa' if is_student else 'Bukan Siswa'}")

# ============================================
# LATIHAN 2: Operasi Matematika
# ============================================
print("\n--- LATIHAN 2: Operasi Matematika ---")

# TODO: Buat variabel a = 15 dan b = 4
# Hitung dan print:
# - Penjumlahan
# - Pengurangan
# - Perkalian
# - Pembagian
# - Floor Division
# - Modulus
# - Pangkat

a = 15
b = 4

# Contoh:
print(f"{a} + {b} = {a + b}")
# TODO: Lanjutkan untuk operasi lainnya...


# ============================================
# LATIHAN 3: String Manipulation
# ============================================
print("\n--- LATIHAN 3: String Manipulation ---")

# TODO: Buat variabel
# - nama_depan = nama depan Anda
# - nama_belakang = nama belakang Anda

nama_depan = "Budi"
nama_belakang = "Santoso"

# TODO: Gabungkan menjadi nama_lengkap
nama_lengkap_gabungan = ""  # LENGKAPI

# TODO: Convert nama_lengkap ke uppercase
nama_uppercase = ""  # LENGKAPI

# TODO: Hitung panjang nama_lengkap
panjang_nama = 0  # LENGKAPI

print(f"Nama Lengkap: {nama_lengkap_gabungan}")
print(f"Uppercase: {nama_uppercase}")
print(f"Panjang: {panjang_nama} karakter")

# ============================================
# LATIHAN 4: Type Conversion
# ============================================
print("\n--- LATIHAN 4: Type Conversion ---")

# Diberikan:
angka_string = "100"
angka_float = 3.14
angka_int = 42

# TODO: Convert angka_string ke integer
converted_int = 0  # LENGKAPI

# TODO: Convert angka_float ke integer
converted_from_float = 0  # LENGKAPI

# TODO: Convert angka_int ke float
converted_to_float = 0.0  # LENGKAPI

# TODO: Convert angka_int ke string
converted_to_string = ""  # LENGKAPI

print(f"'{angka_string}' → {converted_int} (type: {type(converted_int).__name__})")
print(f"{angka_float} → {converted_from_float} (type: {type(converted_from_float).__name__})")
print(f"{angka_int} → {converted_to_float} (type: {type(converted_to_float).__name__})")
print(f"{angka_int} → '{converted_to_string}' (type: {type(converted_to_string).__name__})")

# ============================================
# LATIHAN 5: BMI Calculator
# ============================================
print("\n--- LATIHAN 5: BMI Calculator ---")

# TODO: Gunakan variabel tinggi_badan dan berat_badan dari Latihan 1
# Hitung BMI dengan rumus: BMI = berat / (tinggi_meter^2)
# HINT: tinggi_meter = tinggi_badan / 100

tinggi_meter = 0.0  # LENGKAPI
bmi = 0.0  # LENGKAPI

print(f"Tinggi: {tinggi_badan} cm ({tinggi_meter} m)")
print(f"Berat: {berat_badan} kg")
print(f"BMI: {bmi:.2f}")

# ============================================
# LATIHAN 6: String Formatting
# ============================================
print("\n--- LATIHAN 6: String Formatting ---")

# Diberikan:
nama_produk = "Laptop"
harga = 15500000
stok = 25

# TODO: Buat string dengan format:
# "Produk: [nama_produk], Harga: Rp [harga dengan separator], Stok: [stok] unit"
# Gunakan f-string

pesan = ""  # LENGKAPI

print(pesan)

# ============================================
# LATIHAN 7: Boolean Logic
# ============================================
print("\n--- LATIHAN 7: Boolean Logic ---")

# Diberikan:
nilai_ujian = 85
nilai_tugas = 90
kehadiran = 95  # persentase

# TODO: Buat boolean variable:
# - lulus_ujian: True jika nilai_ujian >= 60
# - lulus_tugas: True jika nilai_tugas >= 60
# - kehadiran_cukup: True jika kehadiran >= 75
# - lulus_semua: True jika SEMUA lulus

lulus_ujian = False  # LENGKAPI
lulus_tugas = False  # LENGKAPI
kehadiran_cukup = False  # LENGKAPI
lulus_semua = False  # LENGKAPI

print(f"Lulus Ujian: {lulus_ujian}")
print(f"Lulus Tugas: {lulus_tugas}")
print(f"Kehadiran Cukup: {kehadiran_cukup}")
print(f"Lulus Semua: {lulus_semua}")

# ============================================
# LATIHAN 8: Swap Values
# ============================================
print("\n--- LATIHAN 8: Swap Values ---")

# Diberikan:
x = 10
y = 20

print(f"Sebelum swap: x={x}, y={y}")

# TODO: Swap nilai x dan y tanpa menggunakan variabel temporary
# HINT: x, y = ???

# TULIS KODE DI SINI

print(f"Setelah swap: x={x}, y={y}")
# Expected output: x=20, y=10

# ============================================
# LATIHAN 9: Challenge - Temperature Converter
# ============================================
print("\n--- LATIHAN 9: Challenge - Temperature Converter ---")

# TODO: Buat program yang:
# 1. Minta input suhu dalam Celsius (gunakan input())
# 2. Convert ke Fahrenheit: F = (C * 9/5) + 32
# 3. Convert ke Kelvin: K = C + 273.15
# 4. Print hasil dengan format yang rapi

# TULIS KODE DI SINI


# ============================================
# LATIHAN 10: Challenge - Shopping Cart
# ============================================
print("\n--- LATIHAN 10: Challenge - Shopping Cart ---")

# TODO: Simulasi shopping cart
# 1. Buat variabel untuk 3 item:
#    - nama_item_1, harga_item_1, quantity_item_1
#    - nama_item_2, harga_item_2, quantity_item_2
#    - nama_item_3, harga_item_3, quantity_item_3
# 2. Hitung subtotal untuk setiap item
# 3. Hitung total keseluruhan
# 4. Jika total > 100000, dapat diskon 10%
# 5. Hitung pajak 10% dari total setelah diskon
# 6. Hitung grand total
# 7. Print invoice yang rapi

# TULIS KODE DI SINI


print("\n" + "="*60)
print("             LATIHAN SELESAI!")
print("="*60)
print("\nSaran:")
print("1. Jalankan program ini dan cek hasilnya")
print("2. Jika ada error, baca error message dengan teliti")
print("3. Jika masih kesulitan, lihat README.md Module 02")
print("4. Coba eksperimen dengan value yang berbeda")
print("="*60)
