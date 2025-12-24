# Module 05 - Input & Output

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan modul ini, Anda akan:
- Memahami cara menerima input dari user
- Dapat melakukan type conversion pada input
- Menguasai berbagai cara print output
- Memahami formatting output yang rapi
- Dapat membuat program interaktif

## ⌨️ Input - Menerima Data dari User

### Fungsi input()

`input()` adalah fungsi untuk menerima input dari user. Fungsi ini:
- Menampilkan prompt (opsional)
- Menunggu user mengetik
- Return string (SELALU string, apapun yang diketik)

```python
# Basic input
nama = input()  # Tunggu input tanpa prompt
print(nama)

# Input dengan prompt
nama = input("Siapa nama Anda? ")
print(f"Halo, {nama}!")

# Input SELALU return string!
umur = input("Umur: ")
print(type(umur))  # <class 'str'>
```

### Type Conversion pada Input

Karena `input()` selalu return string, kita perlu convert jika butuh tipe lain:

```python
# ❌ SALAH - akan error saat perhitungan
umur = input("Umur: ")
tahun_lahir = 2024 - umur  # TypeError! (str - int)

# ✅ BENAR - convert dulu ke int
umur = int(input("Umur: "))
tahun_lahir = 2024 - umur
print(f"Tahun lahir: {tahun_lahir}")

# Untuk float
tinggi = float(input("Tinggi (cm): "))
print(f"Tinggi: {tinggi} cm")

# Multiple inputs dalam satu baris
data = input("Nama dan umur (pisah spasi): ")
nama, umur = data.split()
umur = int(umur)
print(f"Nama: {nama}, Umur: {umur}")

# Atau lebih efisien:
nama, umur = input("Nama dan umur: ").split()
umur = int(umur)
```

### Error Handling pada Input

```python
# ⚠️ Input non-numerik akan error
try:
    umur = int(input("Umur: "))
    print(f"Umur: {umur}")
except ValueError:
    print("Harap masukkan angka!")

# Loop sampai input valid
while True:
    try:
        umur = int(input("Umur: "))
        break  # Keluar dari loop jika berhasil
    except ValueError:
        print("Input harus angka! Coba lagi.")

print(f"Umur Anda: {umur}")
```

### Input Multi-line

```python
# Input beberapa baris
print("Masukkan alamat (tekan Enter 2x untuk selesai):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
alamat = "\n".join(lines)
print("\nAlamat Anda:")
print(alamat)
```

## 🖨️ Output - Menampilkan Data

### Fungsi print()

`print()` adalah fungsi untuk menampilkan output ke console.

```python
# Basic print
print("Hello, World!")

# Print multiple values
nama = "Budi"
umur = 25
print(nama, umur)  # Output: Budi 25

# Print dengan custom separator
print(nama, umur, sep=" | ")  # Output: Budi | 25
print("A", "B", "C", sep="-")  # Output: A-B-C

# Print tanpa newline
print("Baris 1", end=" ")
print("Baris 2")  # Output: Baris 1 Baris 2

# Loading animation
import time
for i in range(3):
    print("Loading", end="")
    for j in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()  # Newline

# Print ke file (akan dipelajari lebih detail di Module 12)
with open("output.txt", "w") as file:
    print("Hello, File!", file=file)
```

### Formatted Output

#### 1. F-Strings (Recommended ⭐)

```python
nama = "Budi"
umur = 25
tinggi = 175.5

# Basic f-string
print(f"Nama: {nama}, Umur: {umur}")

# Expressions
print(f"Tahun lahir: {2024 - umur}")

# Formatting numbers
pi = 3.14159265359
print(f"Pi: {pi:.2f}")  # 2 decimal places: 3.14
print(f"Pi: {pi:.5f}")  # 5 decimal places: 3.14159

# Percentage
nilai = 0.875
print(f"Nilai: {nilai:.1%}")  # 87.5%

# Thousands separator
harga = 1500000
print(f"Harga: Rp {harga:,}")  # Rp 1,500,000

# Width and alignment
print(f"{'Nama':<15} {'Umur':>5} {'Tinggi':>7}")
print(f"{nama:<15} {umur:>5} {tinggi:>7.1f}")
# Output:
# Nama                 Umur  Tinggi
# Budi                   25    175.5

# Center alignment
judul = "DATA SISWA"
print(f"{judul:^40}")  # Center dalam 40 karakter
print("=" * 40)

# Padding dengan karakter
print(f"{nama:*^20}")  # *******Budi********

# Binary, Octal, Hex
angka = 42
print(f"Decimal: {angka}")       # 42
print(f"Binary: {angka:b}")      # 101010
print(f"Octal: {angka:o}")       # 52
print(f"Hexadecimal: {angka:x}") # 2a
```

#### 2. format() Method

```python
nama = "Budi"
umur = 25

# Positional arguments
print("Nama: {}, Umur: {}".format(nama, umur))

# Index
print("Nama: {0}, Umur: {1}".format(nama, umur))
print("{1} tahun yang lalu, {0} berumur {1} tahun".format(nama, umur-1))

# Named arguments
print("Nama: {name}, Umur: {age}".format(name=nama, age=umur))

# Formatting
pi = 3.14159
print("Pi: {:.3f}".format(pi))  # 3.142
```

#### 3. %-formatting (Old Style)

```python
nama = "Budi"
umur = 25
tinggi = 175.5

print("Nama: %s, Umur: %d, Tinggi: %.1f cm" % (nama, umur, tinggi))
# Output: Nama: Budi, Umur: 25, Tinggi: 175.5 cm

# ⚠️ Tidak disarankan untuk kode baru
```

### Pretty Printing

```python
# Simple table
print("=" * 50)
print(f"{'NO':<5} {'NAMA':<20} {'UMUR':>5} {'KOTA':<15}")
print("=" * 50)
print(f"{1:<5} {'Budi':<20} {25:>5} {'Jakarta':<15}")
print(f"{2:<5} {'Siti':<20} {30:>5} {'Bandung':<15}")
print(f"{3:<5} {'Andi':<20} {22:>5} {'Surabaya':<15}")
print("=" * 50)

# Box drawing
print("╔" + "═" * 48 + "╗")
print("║" + "  DATA SISWA".center(48) + "║")
print("╠" + "═" * 48 + "╣")
print("║ Nama  : Budi".ljust(49) + "║")
print("║ Umur  : 25 tahun".ljust(49) + "║")
print("║ Kelas : 12 IPA 1".ljust(49) + "║")
print("╚" + "═" * 48 + "╝")
```

### Formatted String Literals Advanced

```python
# Date and time formatting
from datetime import datetime
now = datetime.now()

print(f"Sekarang: {now:%Y-%m-%d %H:%M:%S}")
print(f"Tanggal: {now:%d %B %Y}")
print(f"Waktu: {now:%H:%M}")

# Nested formatting
width = 10
precision = 2
value = 3.14159
print(f"{value:{width}.{precision}f}")  # 3.14 (width 10, precision 2)

# Debugging (Python 3.8+)
nama = "Budi"
umur = 25
print(f"{nama=}")   # nama='Budi'
print(f"{umur=}")   # umur=25
print(f"{nama=} {umur=}")  # nama='Budi' umur=25
```

## 🎨 Membuat Output Menarik

### 1. Colors (ANSI Escape Codes)

```python
# ANSI Color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

print(f"{RED}Ini teks merah{RESET}")
print(f"{GREEN}Ini teks hijau{RESET}")
print(f"{YELLOW}Ini teks kuning{RESET}")
print(f"{BLUE}Ini teks biru{RESET}")

# Background colors
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'

print(f"{BG_RED}Background merah{RESET}")
print(f"{BG_GREEN}Background hijau{RESET}")

# Bold, Underline, Italic
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALIC = '\033[3m'

print(f"{BOLD}Teks tebal{RESET}")
print(f"{UNDERLINE}Teks bergaris bawah{RESET}")
print(f"{ITALIC}Teks miring{RESET}")

# Kombinasi
print(f"{BOLD}{RED}Teks merah tebal{RESET}")
```

### 2. Progress Bar Sederhana

```python
import time
import sys

def progress_bar(progress, total):
    percent = 100 * (progress / total)
    bar_length = 50
    filled = int(bar_length * progress / total)
    bar = '█' * filled + '-' * (bar_length - filled)
    sys.stdout.write(f'\r|{bar}| {percent:.1f}%')
    sys.stdout.flush()

# Simulasi
print("Downloading...")
for i in range(101):
    progress_bar(i, 100)
    time.sleep(0.05)
print("\nSelesai!")
```

### 3. Menu Interaktif

```python
def tampilkan_menu():
    print("\n" + "=" * 40)
    print("         MENU UTAMA")
    print("=" * 40)
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("0. Keluar")
    print("=" * 40)

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (0-4): ").strip()
    
    if pilihan == '1':
        print("\n[Tambah Data]")
        # Kode tambah data di sini
    elif pilihan == '2':
        print("\n[Lihat Data]")
        # Kode lihat data di sini
    elif pilihan == '3':
        print("\n[Edit Data]")
        # Kode edit data di sini
    elif pilihan == '4':
        print("\n[Hapus Data]")
        # Kode hapus data di sini
    elif pilihan == '0':
        print("\nTerima kasih! Goodbye!")
        break
    else:
        print("\nPilihan tidak valid!")
```

## 💻 Program Interaktif Complete Example

```python
# Program Kalkulator BMI
def hitung_bmi():
    print("=" * 50)
    print("      KALKULATOR BMI (Body Mass Index)")
    print("=" * 50)
    print()
    
    # Input dengan validasi
    while True:
        try:
            tinggi = float(input("Tinggi badan (cm): "))
            if tinggi <= 0:
                print("Tinggi harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Input harus angka!")
    
    while True:
        try:
            berat = float(input("Berat badan (kg): "))
            if berat <= 0:
                print("Berat harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Input harus angka!")
    
    # Hitung BMI
    tinggi_meter = tinggi / 100
    bmi = berat / (tinggi_meter ** 2)
    
    # Kategori
    if bmi < 18.5:
        kategori = "Underweight (Kurus)"
        warna = '\033[93m'  # Kuning
    elif bmi < 25:
        kategori = "Normal"
        warna = '\033[92m'  # Hijau
    elif bmi < 30:
        kategori = "Overweight (Kelebihan berat badan)"
        warna = '\033[93m'  # Kuning
    else:
        kategori = "Obesitas"
        warna = '\033[91m'  # Merah
    
    RESET = '\033[0m'
    
    # Output
    print("\n" + "=" * 50)
    print("                  HASIL BMI")
    print("=" * 50)
    print(f"Tinggi    : {tinggi} cm")
    print(f"Berat     : {berat} kg")
    print(f"BMI       : {bmi:.2f}")
    print(f"Kategori  : {warna}{kategori}{RESET}")
    print("=" * 50)
    
    # Saran
    print("\nKeterangan:")
    print("  < 18.5  : Underweight")
    print("  18.5-24.9 : Normal")
    print("  25-29.9 : Overweight")
    print("  >= 30   : Obesitas")
    print("=" * 50)

# Jalankan program
if __name__ == "__main__":
    hitung_bmi()
```

## ✅ Checklist Module 05

Pastikan Anda memahami:

- [ ] Cara menggunakan input() untuk menerima input
- [ ] Type conversion pada input (int(), float())
- [ ] Fungsi print() dan parameternya (sep, end)
- [ ] Formatted output dengan f-strings
- [ ] Creating pretty output (tables, menus)
- [ ] Input validation

## 📖 Latihan

Lihat folder `exercises/` untuk latihan praktis!

## ➡️ Selanjutnya

[Module 06 - Control Flow (If-Else)](../06-control-flow/)

---

**Selamat! Anda sudah menyelesaikan Module 05! 🎉**
