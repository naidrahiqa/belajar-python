# Module 02 - Variabel & Tipe Data

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan modul ini, Anda akan:
- Memahami konsep variabel dan cara kerjanya
- Mengerti berbagai tipe data di Python
- Dapat melakukan type conversion
- Memahami dynamic typing di Python
- Mengetahui best practices dalam penamaan variabel

## 📦 Apa itu Variabel?

**Variabel** adalah **wadah** untuk menyimpan data di memori komputer.

### Analogi
Bayangkan variabel seperti **kotak** yang diberi **label**:
- **Label kotak** = nama variabel
- **Isi kotak** = nilai variabel
- **Jenis barang di kotak** = tipe data

```python
# Membuat variabel
nama = "Budi"
# 'nama' adalah label kotak
# "Budi" adalah isi kotak
# String adalah jenis barangnya
```

### Cara Membuat Variabel di Python

```python
# Sintaks dasar: nama_variabel = nilai
umur = 25
nama = "Siti"
tinggi = 165.5
is_student = True
```

**Python adalah dynamically typed** - Anda tidak perlu mendeklarasikan tipe data secara eksplisit!

**Perbandingan dengan bahasa lain:**

Java (statically typed):
```java
String nama = "Siti";  // Harus deklarasi tipe
int umur = 25;
```

Python (dynamically typed):
```python
nama = "Siti"  # Tipe otomatis terdeteksi
umur = 25
```

## 📊 Tipe Data di Python

Python memiliki beberapa tipe data built-in. Mari kita pelajari satu per satu:

### 1. **Integer (int)** - Bilangan Bulat

Integer adalah bilangan bulat (tanpa desimal).

```python
# Contoh integer
umur = 25
tahun = 2024
suhu_celsius = -5
jumlah_siswa = 100

# Integer bisa sangat besar (tidak ada batasan!)
populasi_dunia = 8000000000
jarak_ke_matahari = 149600000  # km

# Underscore untuk readability (Python 3.6+)
satu_juta = 1_000_000  # Lebih mudah dibaca
nasa_budget = 25_200_000_000  # 25.2 miliar

print(satu_juta)  # Output: 1000000
```

**Operasi dengan Integer:**
```python
a = 10
b = 3

print(a + b)   # Penjumlahan: 13
print(a - b)   # Pengurangan: 7
print(a * b)   # Perkalian: 30
print(a / b)   # Pembagian: 3.3333... (hasilnya float!)
print(a // b)  # Floor division: 3 (pembagian bulat)
print(a % b)   # Modulus (sisa bagi): 1
print(a ** b)  # Pangkat (10^3): 1000
```

### 2. **Float** - Bilangan Desimal

Float adalah bilangan yang memiliki titik desimal.

```python
# Contoh float
tinggi = 175.5
berat = 68.7
pi = 3.14159
suhu = -2.5

# Scientific notation
kecepatan_cahaya = 3e8      # 3 x 10^8 = 300000000
massa_elektron = 9.1e-31    # 9.1 x 10^-31

print(kecepatan_cahaya)     # Output: 300000000.0
```

**Operasi dengan Float:**
```python
a = 10.5
b = 2.5

print(a + b)   # 13.0
print(a - b)   # 8.0
print(a * b)   # 26.25
print(a / b)   # 4.2
```

**⚠️ Perhatian: Floating Point Precision**
```python
# Float tidak selalu presisi!
print(0.1 + 0.2)  # Output: 0.30000000000000004 (bukan 0.3!)

# Untuk uang, gunakan decimal module
from decimal import Decimal
harga = Decimal('10.50')  # Lebih akurat untuk kalkulasi uang
```

### 3. **String (str)** - Teks

String adalah urutan karakter (teks).

```python
# String dengan single quotes
nama = 'Budi'

# String dengan double quotes
kota = "Jakarta"

# Keduanya sama saja, pilih salah satu dan konsisten

# Multi-line string dengan triple quotes
alamat = """
Jalan Merdeka No. 123
Jakarta Pusat
DKI Jakarta
"""

# String dengan quotes di dalamnya
kalimat1 = "Dia berkata, 'Halo!'"
kalimat2 = 'Buku favorit saya "Harry Potter"'
```

**Operasi String:**
```python
# Concatenation (penggabungan)
nama_depan = "Budi"
nama_belakang = "Santoso"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # Output: Budi Santoso

# Repetition (pengulangan)
garis = "-" * 30
print(garis)  # Output: ------------------------------

# Length (panjang)
nama = "Python"
print(len(nama))  # Output: 6

# Indexing (akses karakter berdasarkan posisi)
# Index dimulai dari 0!
kata = "Python"
print(kata[0])   # P (karakter pertama)
print(kata[1])   # y
print(kata[-1])  # n (karakter terakhir)
print(kata[-2])  # o

# Slicing (mengambil sebagian string)
kata = "Programming"
print(kata[0:4])    # Prog (dari index 0 sampai 3)
print(kata[4:])     # ramming (dari index 4 sampai akhir)
print(kata[:4])     # Prog (dari awal sampai index 3)
print(kata[::2])    # Pormig (setiap 2 karakter)
```

**String Formatting:**
```python
nama = "Budi"
umur = 25

# Method 1: F-string (Python 3.6+, RECOMMENDED)
pesan = f"Nama saya {nama} dan umur saya {umur} tahun"

# Method 2: .format()
pesan = "Nama saya {} dan umur saya {} tahun".format(nama, umur)

# Method 3: % operator (old style, tidak recommended)
pesan = "Nama saya %s dan umur saya %d tahun" % (nama, umur)

print(pesan)  # Nama saya Budi dan umur saya 25 tahun
```

### 4. **Boolean (bool)** - True/False

Boolean hanya memiliki 2 nilai: `True` atau `False`

```python
# Boolean literals
is_student = True
is_graduated = False

# Boolean dari comparison
umur = 20
is_adult = umur >= 18  # True

nilai = 75
lulus = nilai >= 60    # True

# Boolean dari expressions
x = 5
y = 10
hasil = (x < y)        # True
hasil2 = (x == y)      # False
```

**Truthy dan Falsy Values:**

Python mengevaluasi nilai-nilai tertentu sebagai `True` atau `False`:

```python
# Falsy values (dianggap False)
bool(0)          # False - angka 0
bool(0.0)        # False - float 0
bool("")         # False - string kosong
bool([])         # False - list kosong
bool({})         # False - dictionary kosong
bool(None)       # False - None

# Truthy values (dianggap True)
bool(1)          # True - angka selain 0
bool(-5)         # True
bool("hello")    # True - string tidak kosong
bool([1,2,3])    # True - list tidak kosong

# Contoh penggunaan
nama = input("Nama: ")
if nama:  # Akan True jika nama tidak kosong
    print(f"Halo, {nama}!")
else:
    print("Anda tidak memasukkan nama")
```

### 5. **NoneType (None)** - Tidak Ada Nilai

`None` merepresentasikan ketiadaan nilai atau null value.

```python
# Mendeklarasikan variabel tanpa nilai
hasil = None

# Cek apakah variabel None
if hasil is None:
    print("Hasil belum ada")

# Membedakan None dengan False
x = None
y = False

print(x is None)     # True
print(y is None)     # False
print(x == y)        # False
print(bool(x))       # False
print(bool(y))       # False
```

## 🔄 Type Conversion (Konversi Tipe Data)

Kadang kita perlu mengubah satu tipe data ke tipe lainnya.

### int() - Konversi ke Integer

```python
# String to int
angka_str = "123"
angka_int = int(angka_str)
print(angka_int)        # 123
print(type(angka_int))  # <class 'int'>

# Float to int (akan dibulatkan ke bawah)
desimal = 9.7
bulat = int(desimal)
print(bulat)  # 9 (bukan 10!)

# Bool to int
print(int(True))   # 1
print(int(False))  # 0

# ⚠️ Error jika string bukan angka
# angka = int("abc")  # ValueError!
```

### float() - Konversi ke Float

```python
# String to float
harga_str = "99.99"
harga = float(harga_str)
print(harga)  # 99.99

# Int to float
umur = 25
umur_float = float(umur)
print(umur_float)  # 25.0

# Bool to float
print(float(True))   # 1.0
print(float(False))  # 0.0
```

### str() - Konversi ke String

```python
# Int to string
umur = 25
umur_str = str(umur)
print(umur_str)        # "25"
print(type(umur_str))  # <class 'str'>

# Float to string
pi = 3.14
pi_str = str(pi)
print(pi_str)  # "3.14"

# Bool to string
print(str(True))   # "True"
print(str(False))  # "False"

# Mengapa perlu str()?
# Untuk menggabungkan dengan string lain
nama = "Budi"
umur = 25
# pesan = "Nama: " + nama + ", Umur: " + umur  # Error!
pesan = "Nama: " + nama + ", Umur: " + str(umur)  # OK!
# Atau gunakan f-string (lebih mudah!)
pesan = f"Nama: {nama}, Umur: {umur}"  # Otomatis convert!
```

### bool() - Konversi ke Boolean

```python
# Int to bool
print(bool(0))      # False
print(bool(1))      # True
print(bool(-5))     # True
print(bool(100))    # True

# String to bool
print(bool(""))     # False (string kosong)
print(bool("abc"))  # True (string ada isi)
print(bool("0"))    # True! (string "0" bukan angka 0)

# None to bool
print(bool(None))   # False
```

## 🏷️ Penamaan Variabel (Naming Conventions)

### Aturan Penamaan Variabel

**Aturan yang HARUS diikuti (akan error jika dilanggar):**

```python
# ✅ VALID
nama = "Budi"
umur = 25
nama_depan = "Budi"
namaDepan = "Budi"  # CamelCase (tapi tidak pythonic)
_private = "data"
nama2 = "Siti"

# ❌ INVALID
# 2nama = "Budi"       # Tidak boleh dimulai dengan angka
# nama-depan = "Budi"  # Tidak boleh pakai dash
# nama depan = "Budi"  # Tidak boleh pakai spasi
# class = "A"          # Tidak boleh gunakan keyword Python
```

**Python Keywords (tidak boleh dipakai sebagai nama variabel):**
```python
# Keywords yang tidak boleh digunakan:
and, as, assert, break, class, continue, def, del, elif, else,
except, False, finally, for, from, global, if, import, in, is,
lambda, None, nonlocal, not, or, pass, raise, return, True, try,
while, with, yield
```

### Konvensi Penamaan (Best Practices)

```python
# ✅ GOOD - snake_case untuk variables
nama_lengkap = "Budi Santoso"
tanggal_lahir = "1999-01-15"
total_harga = 100000

# ✅ GOOD - UPPERCASE untuk constants
PI = 3.14159
MAX_SPEED = 200
DATABASE_URL = "localhost:3306"

# ✅ GOOD - Descriptive names
jumlah_siswa = 30  # Jelas maksudnya
total_harga_setelah_diskon = 85000  # Descriptive

# ❌ BAD - Nama tidak deskriptif
x = 30           # x itu apa?
tmp = 85000      # tmp untuk apa?
a1 = "Budi"      # a1 tidak menjelaskan apa-apa

# ❌ BAD - Terlalu panjang
nama_lengkap_siswa_kelas_12_ipa_1_semester_genap = "Budi"

# ✅ GOOD - Balance
nama_siswa = "Budi"
```

## 🔍 Mengecek Tipe Data

### Fungsi type()

```python
# Mengecek tipe data
nama = "Budi"
umur = 25
tinggi = 175.5
is_student = True

print(type(nama))        # <class 'str'>
print(type(umur))        # <class 'int'>
print(type(tinggi))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# Conditional berdasarkan tipe
nilai = 100
if type(nilai) == int:
    print("Ini adalah integer")
```

### Fungsi isinstance()

```python
# Cara yang lebih pythonic untuk cek tipe
umur = 25

if isinstance(umur, int):
    print("Umur adalah integer")

if isinstance(umur, (int, float)):  # Cek multiple types
    print("Umur adalah angka")
```

## 💡 Konsep Penting

### 1. Dynamic Typing

Python membolehkan variabel mengubah tipe:

```python
x = 5           # x adalah int
print(type(x))  # <class 'int'>

x = "Hello"     # Sekarang x adalah string
print(type(x))  # <class 'str'>

x = True        # Sekarang x adalah boolean
print(type(x))  # <class 'bool'>

# Ini VALID di Python, tapi bisa membingungkan
# Best practice: jangan ubah tipe variabel
```

### 2. Multiple Assignment

```python
# Assign multiple variables sekaligus
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swap values tanpa temporary variable
x = 5
y = 10
x, y = y, x  # Swap!
print(x, y)  # 10 5

# Assign nilai yang sama ke multiple variables
x = y = z = 0
print(x, y, z)  # 0 0 0
```

### 3. Variable Scope (Preview)

```python
# Global variable
nama = "Budi"

def sapa():
    # Local variable
    pesan = "Halo"
    print(f"{pesan}, {nama}!")

sapa()  # Output: Halo, Budi!
# print(pesan)  # Error! pesan tidak exist di luar fungsi
```

## ✅ Checklist Module 02

Pastikan Anda sudah memahami:

- [ ] Cara membuat dan menggunakan variabel
- [ ] Tipe data: int, float, string, bool, None
- [ ] Konversi tipe data (type conversion)
- [ ] Aturan penamaan variabel
- [ ] Cara mengecek tipe data dengan type() dan isinstance()
- [ ] Dynamic typing di Python

## 📖 Latihan

Lihat folder `exercises/` untuk latihan praktis!

## ➡️ Selanjutnya

[Module 03 - Operators (Operator)](../03-operators/)

---

**Selamat! Anda sudah menyelesaikan Module 02! 🎉**
