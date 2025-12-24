# ============================================
# CONTOH: Tipe Data dan Variabel
# Module 02 - Variabel & Tipe Data
# ============================================

"""
File ini berisi contoh-contoh penggunaan variabel
dan berbagai tipe data di Python.
"""

# ==========================================
# 1. INTEGER (Bilangan Bulat)
# ==========================================

print("="*50)
print("1. INTEGER EXAMPLES")
print("="*50)

umur = 25
tahun = 2024
jumlah_siswa = 100

print(f"Umur: {umur}")
print(f"Tahun: {tahun}")
print(f"Jumlah siswa: {jumlah_siswa}")

# Integer bisa sangat besar
populasi_indonesia = 270_000_000  # Underscore untuk readability
print(f"Populasi Indonesia: {populasi_indonesia:,}")

# Operasi integer
a = 10
b = 3
print(f"\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")  # Float result
print(f"{a} // {b} = {a // b}")  # Integer division
print(f"{a} % {b} = {a % b}")  # Modulus
print(f"{a} ** {b} = {a ** b}")  # Power

# ==========================================
# 2. FLOAT (Bilangan Desimal)
# ==========================================

print("\n" + "="*50)
print("2. FLOAT EXAMPLES")
print("="*50)

tinggi = 175.5
berat = 68.7
pi = 3.14159
suhu = -2.5

print(f"Tinggi: {tinggi} cm")
print(f"Berat: {berat} kg")
print(f"Pi: {pi}")
print(f"Suhu: {suhu}°C")

# Scientific notation
kecepatan_cahaya = 3e8  # 3 x 10^8
print(f"Kecepatan cahaya: {kecepatan_cahaya} m/s")

# Float precision issue
print(f"\n0.1 + 0.2 = {0.1 + 0.2}")  # 0.30000000000000004
print("(Ini adalah keterbatasan floating point!)")

# ==========================================
# 3. STRING (Teks)
# ==========================================

print("\n" + "="*50)
print("3. STRING EXAMPLES")
print("="*50)

nama = "Budi Santoso"
kota = 'Jakarta'
alamat = """
Jalan Merdeka No. 123
Jakarta Pusat, 10110
"""

print(f"Nama: {nama}")
print(f"Kota: {kota}")
print(f"Alamat: {alamat}")

# String operations
nama_depan = "Budi"
nama_belakang = "Santoso"
nama_lengkap = nama_depan + " " + nama_belakang
print(f"Nama lengkap: {nama_lengkap}")

# String repetition
garis = "-" * 40
print(garis)

# String methods
print(f"Uppercase: {nama.upper()}")
print(f"Lowercase: {nama.lower()}")
print(f"Length: {len(nama)} karakter")

# ==========================================
# 4. BOOLEAN (True/False)
# ==========================================

print("\n" + "="*50)
print("4. BOOLEAN EXAMPLES")
print("="*50)

is_student = True
is_graduated = False
is_adult = umur >= 18

print(f"Apakah siswa? {is_student}")
print(f"Sudah lulus? {is_graduated}")
print(f"Sudah dewasa? {is_adult}")

# Boolean operations
print(f"\nTrue and True = {True and True}")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# ==========================================
# 5. NONE TYPE
# ==========================================

print("\n" + "="*50)
print("5. NONE TYPE EXAMPLE")
print("="*50)

hasil = None
print(f"Hasil: {hasil}")
print(f"Type: {type(hasil)}")

if hasil is None:
    print("Hasil belum ada")

# ==========================================
# 6. TYPE CONVERSION
# ==========================================

print("\n" + "="*50)
print("6. TYPE CONVERSION EXAMPLES")
print("="*50)

# String to int
angka_str = "123"
angka_int = int(angka_str)
print(f"'{angka_str}' (string) → {angka_int} (int)")

# Int to float
umur_int = 25
umur_float = float(umur_int)
print(f"{umur_int} (int) → {umur_float} (float)")

# Float to int
pi_float = 3.14
pi_int = int(pi_float)
print(f"{pi_float} (float) → {pi_int} (int)")

# Int to string
angka = 100
angka_str = str(angka)
print(f"{angka} (int) → '{angka_str}' (string)")

# Bool to int
print(f"int(True) = {int(True)}")
print(f"int(False) = {int(False)}")

# ==========================================
# 7. TYPE CHECKING
# ==========================================

print("\n" + "="*50)
print("7. TYPE CHECKING")
print("="*50)

variables = [
    ("nama", nama),
    ("umur", umur),
    ("tinggi", tinggi),
    ("is_student", is_student),
    ("hasil", hasil)
]

for var_name, var_value in variables:
    print(f"{var_name:15} = {str(var_value):15} | Type: {type(var_value).__name__}")

# ==========================================
# 8. MULTIPLE ASSIGNMENT
# ==========================================

print("\n" + "="*50)
print("8. MULTIPLE ASSIGNMENT")
print("="*50)

# Assign multiple variables
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Swap values
x, y = y, x
print(f"After swap: x={x}, y={y}")

# Same value to multiple variables
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

print("\n" + "="*50)
print("PROGRAM SELESAI")
print("="*50)
