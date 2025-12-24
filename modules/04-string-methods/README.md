# Module 04 - String & String Methods

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan modul ini, Anda akan:
- Memahami string secara mendalam
- Menguasai string indexing dan slicing
- Dapat menggunakan berbagai string methods
- Memahami string formatting (f-strings, format(), %)
- Dapat memanipulasi string dengan efisien

## 📝 Apa itu String?

**String** adalah sequence of characters (urutan karakter). Di Python, string adalah **immutable**, artinya tidak bisa diubah setelah dibuat.

```python
# Membuat string
nama = "Python"
pesan = 'Hello, World!'
alamat = """
Jalan Merdeka No. 123
Jakarta Pusat
"""

# String adalah sequence
print(type(nama))  # <class 'str'>
```

## 🔤 Karakteristik String

### 1. Immutable

```python
# String tidak bisa diubah
teks = "Python"

# ❌ Tidak bisa ubah karakter langsung
# teks[0] = "J"  # TypeError!

# ✅ Harus buat string baru
teks = "J" + teks[1:]
print(teks)  # Jython
```

### 2. Ordered (Berurutan)

```python
teks = "Python"
# P = index 0
# y = index 1
# t = index 2
# h = index 3
# o = index 4
# n = index 5
```

### 3. Iterable

```python
# Bisa di-loop
for huruf in "Python":
    print(huruf)
# Output:
# P
# y
# t
# h
# o
# n
```

## 📍 String Indexing

Index dimulai dari 0.

```python
teks = "Python"

# Positive indexing (dari kiri)
print(teks[0])  # P (karakter pertama)
print(teks[1])  # y
print(teks[5])  # n (karakter terakhir)

# Negative indexing (dari kanan)
print(teks[-1])  # n (karakter terakhir)
print(teks[-2])  # o
print(teks[-6])  # P (sama dengan index 0)

# Visual representation:
#  P   y   t   h   o   n
#  0   1   2   3   4   5   (positive index)
# -6  -5  -4  -3  -2  -1   (negative index)
```

## ✂️ String Slicing

Slicing digunakan untuk mengambil sebagian string.

**Sintaks:** `string[start:stop:step]`

- `start` - index awal (inclusive)
- `stop` - index akhir (exclusive - tidak termasuk)
- `step` - langkah/jarak (default: 1)

```python
teks = "Python Programming"

# Basic slicing
print(teks[0:6])    # Python (dari index 0-5)
print(teks[7:18])   # Programming

# Dengan default values
print(teks[:6])     # Python (dari awal sampai index 5)
print(teks[7:])     # Programming (dari index 7 sampai akhir)
print(teks[:])      # Python Programming (copy seluruh string)

# Negative index dalam slicing
print(teks[-11:])   # Programming
print(teks[:-12])   # Python

# Step
print(teks[::2])    # Pto rgamn (setiap 2 karakter)
print(teks[::3])    # Ph ormn (setiap 3 karakter)
print(teks[::-1])   # gnimmargorP nohtyP (reverse!)

# Real-world examples
email = "user@example.com"
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(username)  # user
print(domain)    # example.com

# Extract dari belakang
file = "document.pdf"
extension = file[-3:]
print(extension)  # pdf
```

## 🛠️ String Methods

Python menyediakan banyak built-in methods untuk manipulasi string.

### 1. Case Conversion

```python
teks = "Python Programming"

# upper() - semua huruf besar
print(teks.upper())  # PYTHON PROGRAMMING

# lower() - semua huruf kecil
print(teks.lower())  # python programming

# capitalize() - huruf pertama kapital, sisanya kecil
print(teks.capitalize())  # Python programming

# title() - setiap kata dikapitalkan
print("hello world".title())  # Hello World

# swapcase() - tukar case
print(teks.swapcase())  # pYTHON pROGRAMMING

# casefold() - lebih agresif dari lower() untuk comparison
print("ß".lower())     # ß
print("ß".casefold())  # ss
```

**Kapan digunakan:**
```python
# Case-insensitive comparison
nama_input = "BUDI"
nama_db = "Budi"

if nama_input.lower() == nama_db.lower():
    print("Nama sama")

# Title case untuk nama
nama = input("Nama: ").title()
```

### 2. Checking Methods (return boolean)

```python
teks = "Python123"

# isalpha() - semua huruf?
print("Python".isalpha())    # True
print("Python123".isalpha()) # False

# isdigit() - semua angka?
print("123".isdigit())      # True
print("12.3".isdigit())     # False

# isalnum() - huruf atau angka?
print("Python123".isalnum())  # True
print("Python 123".isalnum()) # False (ada spasi)

# isspace() - semua whitespace?
print("   ".isspace())      # True
print("  a  ".isspace())    # False

# isupper() - semua huruf besar?
print("PYTHON".isupper())   # True
print("Python".isupper())   # False

# islower() - semua huruf kecil?
print("python".islower())   # True
print("Python".islower())   # False

# istitle() - title case?
print("Python Programming".istitle())  # True
print("Python programming".istitle())  # False

# startswith() - dimulai dengan?
print("Python".startswith("Py"))  # True
print("Python".startswith("Ja"))  # False

# endswith() - diakhiri dengan?
print("file.pdf".endswith(".pdf"))  # True
print("file.pdf".endswith(".jpg"))  # False
```

**Real-world usage:**
```python
# Validasi input
umur_input = input("Umur: ")
if umur_input.isdigit():
    umur = int(umur_input)
    print(f"Umur Anda: {umur}")
else:
    print("Input harus angka!")

# Cek file extension
filename = "document.pdf"
if filename.endswith(('.pdf', '.doc', '.docx')):
    print("File dokumen valid")
```

### 3. Find & Replace

```python
teks = "Python is amazing. Python is powerful."

# find() - mencari substring, return index (atau -1 jika tidak ada)
print(teks.find("Python"))     # 0 (index pertama)
print(teks.find("is"))         # 7
print(teks.find("Java"))       # -1 (tidak ada)

# rfind() - find dari kanan
print(teks.rfind("Python"))    # 20 (index Python kedua)

# index() - seperti find(), tapi raise error jika tidak ada
print(teks.index("Python"))    # 0
# print(teks.index("Java"))    # ValueError!

# count() - hitung berapa kali substring muncul
print(teks.count("Python"))    # 2
print(teks.count("is"))        # 2

# replace() - mengganti substring
new_teks = teks.replace("Python", "Java")
print(new_teks)  # Java is amazing. Java is powerful.

# Replace dengan count (max replacement)
teks2 = "ha ha ha ha"
print(teks2.replace("ha", "he", 2))  # he he ha ha
```

### 4. Strip Methods (Hapus Whitespace)

```python
# strip() - hapus whitespace di awal dan akhir
teks = "   Python   "
print(teks.strip())   # "Python"
print(len(teks))      # 13
print(len(teks.strip()))  # 6

# lstrip() - hapus whitespace di kiri
print(teks.lstrip())  # "Python   "

# rstrip() - hapus whitespace di kanan
print(teks.rstrip())  # "   Python"

# Strip karakter tertentu
url = "www.python.org"
print(url.strip('w'))  # .python.org (hapus 'w' di awal/akhir)

website = "https://www.example.com/"
print(website.strip('https://').strip('/'))  # www.example.com
```

**Penggunaan umum:**
```python
# Bersihkan input user
nama = input("Nama: ").strip()  # Hapus spasi berlebih
email = input("Email: ").strip().lower()  # Bersihkan dan lowercase
```

### 5. Split & Join

```python
# split() - memecah string jadi list
kalimat = "Python is amazing"
words = kalimat.split()  # Split by whitespace (default)
print(words)  # ['Python', 'is', 'amazing']

# Split by delimiter tertentu
csv_data = "Budi,25,Jakarta"
data = csv_data.split(',')
print(data)  # ['Budi', '25', 'Jakarta']

# Split dengan max split
teks = "a-b-c-d-e"
print(teks.split('-', 2))  # ['a', 'b', 'c-d-e']

# splitlines() - split by newline
multiline = """Baris 1
Baris 2
Baris 3"""
lines = multiline.splitlines()
print(lines)  # ['Baris 1', 'Baris 2', 'Baris 3']

# join() - gabungkan list jadi string
words = ['Python', 'is', 'amazing']
kalimat = ' '.join(words)
print(kalimat)  # Python is amazing

# Join dengan delimiter lain
data = ['Budi', '25', 'Jakarta']
csv = ','.join(data)
print(csv)  # Budi,25,Jakarta

# Join path
path_parts = ['folder', 'subfolder', 'file.txt']
path = '/'.join(path_parts)
print(path)  # folder/subfolder/file.txt
```

### 6. Alignment & Padding

```python
teks = "Python"

# center() - center align
print(teks.center(20))       # "       Python       "
print(teks.center(20, '*'))  # "*******Python*******"

# ljust() - left justify
print(teks.ljust(20, '-'))   # "Python--------------"

# rjust() - right justify
print(teks.rjust(20, '-'))   # "--------------Python"

# zfill() - pad dengan 0 di kiri (untuk angka)
print("42".zfill(5))         # "00042"
print("-42".zfill(5))        # "-0042"
```

**Penggunaan: Format tabel**
```python
print("Nama".ljust(20), "Umur".rjust(5))
print("Budi".ljust(20), str(25).rjust(5))
print("Siti".ljust(20), str(30).rjust(5))

# Output:
# Nama                  Umur
# Budi                    25
# Siti                    30
```

## 🎨 String Formatting

### 1. F-Strings (Python 3.6+) ⭐ RECOMMENDED

```python
nama = "Budi"
umur = 25
tinggi = 175.5

# Basic f-string
pesan = f"Nama saya {nama}, umur {umur} tahun"
print(pesan)

# Expressions dalam f-string
print(f"Tahun depan umur saya {umur + 1}")
print(f"Tinggi saya {tinggi} cm atau {tinggi/100} meter")

# Method calls dalam f-string
print(f"Nama uppercase: {nama.upper()}")

# Formatting angka
pi = 3.14159265359
print(f"Pi: {pi:.2f}")     # 3.14 (2 desimal)
print(f"Pi: {pi:.4f}")     # 3.1416 (4 desimal)

# Formatting ribuan
harga = 1500000
print(f"Harga: Rp {harga:,}")  # Rp 1,500,000

# Width dan alignment
print(f"{'Nama':<10} {'Umur':>5}")
print(f"{nama:<10} {umur:>5}")
# Nama            Umur
# Budi              25

# Padding dengan karakter tertentu
print(f"{nama:*^20}")  # *******Budi********

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Sekarang: {now:%Y-%m-%d %H:%M:%S}")
```

### 2. format() Method

```python
nama = "Budi"
umur = 25

# Basic format
pesan = "Nama: {}, Umur: {}".format(nama, umur)
print(pesan)

# Dengan index
pesan = "Nama: {0}, Umur: {1}, {0} berumur {1} tahun".format(nama, umur)
print(pesan)

# Dengan named arguments
pesan = "Nama: {name}, Umur: {age}".format(name=nama, age=umur)
print(pesan)

# Formatting
pi = 3.14159
print("Pi: {:.2f}".format(pi))  # Pi: 3.14
```

### 3. % Operator (Old Style)

```python
nama = "Budi"
umur = 25

# %s untuk string
# %d untuk integer
# %f untuk float
pesan = "Nama: %s, Umur: %d" % (nama, umur)
print(pesan)

pi = 3.14159
print("Pi: %.2f" % pi)  # Pi: 3.14

# ⚠️ Tidak disarankan untuk kode baru
# Gunakan f-strings!
```

## 🔧 Escape Characters

```python
# Newline (\n)
print("Baris 1\nBaris 2")
# Output:
# Baris 1
# Baris 2

# Tab (\t)
print("Nama:\tBudi")
print("Umur:\t25")
# Output:
# Nama:	Budi
# Umur:	25

# Backslash (\\)
print("C:\\Users\\Documents")  # C:\Users\Documents

# Quote (\' atau \")
print('Dia berkata, \'Halo!\'')  # Dia berkata, 'Halo!'
print("Buku \"Python\"")         # Buku "Python"

# Unicode (\u)
print("\u2764")  # ❤ (heart symbol)
print("\u03C0")  # π (pi symbol)
```

### Raw Strings

```python
# Raw string - backslash tidak di-escape
path = r"C:\Users\Documents\new_folder"
print(path)  # C:\Users\Documents\new_folder

# Tanpa raw string
path = "C:\\Users\\Documents\\new_folder"  # Harus escape \\
```

## 💡 Best Practices

### 1. Gunakan F-Strings

```python
# ❌ Tidak disarankan
nama = "Budi"
pesan = "Halo, " + nama + "!"

# ✅ Recommended
pesan = f"Halo, {nama}!"
```

### 2. Strip Input User

```python
# ✅ Selalu strip input
nama = input("Nama: ").strip()
email = input("Email: ").strip().lower()
```

### 3. Use String Methods Instead of Regex (Jika Memungkinkan)

```python
# ✅ Simple dan readable
if email.endswith('@gmail.com'):
    print("Gmail user")

# ❌ Overkill untuk kasus sederhana
import re
if re.search(r'@gmail\.com$', email):
    print("Gmail user")
```

## ✅ Checklist Module 04

Pastikan Anda memahami:

- [ ] String indexing dan negative indexing
- [ ] String slicing (start:stop:step)
- [ ] String methods: upper(), lower(), strip(), split(), join()
- [ ] String checking methods: isalpha(), isdigit(), etc.
- [ ] String formatting dengan f-strings
- [ ] Escape characters
- [ ] String immutability

## 📖 Latihan

Lihat folder `exercises/` untuk latihan praktis!

## ➡️ Selanjutnya

[Module 05 - Input & Output](../05-input-output/)

---

**Selamat! Anda sudah menyelesaikan Module 04! 🎉**
