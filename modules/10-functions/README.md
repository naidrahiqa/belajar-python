# Module 10 - Functions (Fungsi)

## 🎯 Tujuan Pembelajaran

- Memahami konsep dan kegunaan fungsi
- Dapat membuat dan memanggil fungsi
- Memahami parameters dan arguments
- Menguasai return values
- Memahami scope (local vs global)
- Mengenal lambda functions
- Memahami *args dan **kwargs

## 📦 Apa itu Fungsi?

**Fungsi** adalah blok kode yang dapat digunakan kembali (reusable) untuk melakukan tugas tertentu.

### Mengapa Menggunakan Fungsi?

1. **Reusability** - Tulis sekali, pakai berkali-kali
2. **Organization** - Kode lebih terstruktur
3. **Modularity** - Pecah program besar jadi bagian kecil
4. **Maintainability** - Mudah diupdate dan debug

```python
# Tanpa fungsi - repetitive
print("Halo, Budi!")
print("Selamat datang!")
print()

print("Halo, Siti!")
print("Selamat datang!")
print()

print("Halo, Andi!")
print("Selamat datang!")
print()

# Dengan fungsi - reusable
def sapa(nama):
    print(f"Halo, {nama}!")
    print("Selamat datang!")
    print()

sapa("Budi")
sapa("Siti")
sapa("Andi")
```

## 🔧 Membuat Fungsi

### Sintaks Dasar

```python
# Sintaks:
# def nama_fungsi(parameters):
#     """Docstring"""
#     kode fungsi
#     return nilai

# Fungsi sederhana
def sapa():
    print("Halo!")

# Memanggil fungsi
sapa()  # Output: Halo!

# Fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

sapa_nama("Budi")  # Output: Halo, Budi!

# Fungsi dengan return value
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print(hasil)  # 8
```

### Docstring

Dokumentasi fungsi dengan triple quotes.

```python
def hitung_luas_persegi(sisi):
    """
    Menghitung luas persegi.
    
    Parameters:
        sisi (float): Panjang sisi persegi
    
    Returns:
        float: Luas persegi
    """
    return sisi ** 2

# Lihat docstring
print(hitung_luas_persegi.__doc__)
help(hitung_luas_persegi)
```

## 📥 Parameters vs Arguments

- **Parameter** - Variabel dalam definisi fungsi
- **Argument** - Nilai yang dikirim saat memanggil fungsi

```python
def greet(nama, umur):  # nama dan umur adalah PARAMETERS
    print(f"Halo {nama}, umur {umur}")

greet("Budi", 25)  # "Budi" dan 25 adalah ARGUMENTS
```

### Positional Arguments

```python
def info(nama, umur, kota):
    print(f"{nama}, {umur} tahun, dari {kota}")

# Urutan harus sesuai
info("Budi", 25, "Jakarta")  # ✅
# info(25, "Budi", "Jakarta")  # ❌ Salah urutan
```

### Keyword Arguments

```python
def info(nama, umur, kota):
    print(f"{nama}, {umur} tahun, dari {kota}")

# Bisa ubah urutan dengan keyword
info(umur=25, nama="Budi", kota="Jakarta")
info(kota="Jakarta", nama="Budi", umur=25)

# Kombinasi positional dan keyword
info("Budi", kota="Jakarta", umur=25)  # ✅
# info(nama="Budi", 25, "Jakarta")  # ❌ Error!
```

### Default Parameters

```python
def sapa(nama, sapaan="Halo"):
    print(f"{sapaan}, {nama}!")

sapa("Budi")  # Halo, Budi!
sapa("Budi", "Hi")  # Hi, Budi!
sapa("Budi", sapaan="Selamat pagi")  # Selamat pagi, Budi!

# Default parameter harus di akhir
def info(nama, umur=20, kota="Jakarta"):  # ✅
    pass

# def info(nama="Unknown", umur, kota):  # ❌ Error!
#     pass
```

## 🔙 Return Values

### Basic Return

```python
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print(hasil)  # 8

# Tanpa return, fungsi return None
def print_nama(nama):
    print(nama)

hasil = print_nama("Budi")
print(hasil)  # None
```

### Multiple Return Values

```python
def hitung_semua(a, b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b
    return tambah, kurang, kali, bagi

# Unpack results
hasil_tambah, hasil_kurang, hasil_kali, hasil_bagi = hitung_semua(10, 2)
print(hasil_tambah)  # 12
print(hasil_kurang)  # 8

# Atau simpan sebagai tuple
hasil = hitung_semua(10, 2)
print(hasil)  # (12, 8, 20, 5.0)
```

### Early Return

```python
def cek_umur(umur):
    if umur < 0:
        return "Umur tidak valid"
    
    if umur < 17:
        return "Anak-anak"
    elif umur < 60:
        return "Dewasa"
    else:
        return "Lansia"

print(cek_umur(25))  # Dewasa
print(cek_umur(-5))  # Umur tidak valid
```

## 🌍 Scope (Local vs Global)

### Local Scope

```python
def function():
    x = 10  # Local variable
    print(x)

function()  # 10
# print(x)  # Error! x tidak ada di luar fungsi
```

### Global Scope

```python
x = 10  # Global variable

def function():
    print(x)  # Bisa akses global variable

function()  # 10
print(x)  # 10
```

### Modifying Global Variable

```python
x = 10

def function():
    global x  # Gunakan global keyword
    x = 20

print(x)  # 10
function()
print(x)  # 20 (berubah!)

# ⚠️ Best practice: Hindari global, gunakan return
def function():
    return 20

x = 10
x = function()  # Lebih baik!
print(x)  # 20
```

## ⭐ *args dan **kwargs

### *args - Variable Positional Arguments

```python
def tambah_semua(*angka):
    total = 0
    for num in angka:
        total += num
    return total

print(tambah_semua(1, 2, 3))  # 6
print(tambah_semua(1, 2, 3, 4, 5))  # 15

# *args adalah tuple
def test(*args):
    print(type(args))  # <class 'tuple'>
    print(args)

test(1, 2, 3)  # (1, 2, 3)
```

### **kwargs - Variable Keyword Arguments

```python
def info_siswa(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

info_siswa(nama="Budi", umur=20, kota="Jakarta")
# nama: Budi
# umur: 20
# kota: Jakarta

# **kwargs adalah dictionary
def test(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

test(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
```

### Kombinasi

```python
def fungsi_lengkap(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

fungsi_lengkap(1, 2, 3, 4, 5, nama="Budi", umur=20)
# a = 1
# b = 2
# args = (3, 4, 5)
# kwargs = {'nama': 'Budi', 'umur': 20}

# Urutan parameter harus:
# 1. Positional
# 2. *args
# 3. Keyword
# 4. **kwargs
```

## 🔗 Lambda Functions

Fungsi anonymous (tanpa nama) satu baris.

```python
# Regular function
def kuadrat(x):
    return x ** 2

# Lambda function
kuadrat = lambda x: x ** 2

print(kuadrat(5))  # 25

# Lambda dengan multiple parameters
tambah = lambda a, b: a + b
print(tambah(3, 5))  # 8

# Lambda dalam sorted()
siswa = [
    ("Budi", 85),
    ("Siti", 92),
    ("Andi", 78)
]

# Sort by nilai (index 1)
siswa_sorted = sorted(siswa, key=lambda x: x[1])
print(siswa_sorted)
# [('Andi', 78), ('Budi', 85), ('Siti', 92)]

# Lambda dalam map()
angka = [1, 2, 3, 4, 5]
kuadrat = list(map(lambda x: x**2, angka))
print(kuadrat)  # [1, 4, 9, 16, 25]

# Lambda dalam filter()
genap = list(filter(lambda x: x % 2 == 0, angka))
print(genap)  # [2, 4]
```

## 🎮 Complete Examples

### Example 1: Kalkulator dengan Functions

```python
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi 0"
    return a / b

def kalkulator():
    print("=== KALKULATOR ===")
    
    try:
        a = float(input("Angka pertama: "))
        operator = input("Operator (+,-,*,/): ")
        b = float(input("Angka kedua: "))
        
        if operator == '+':
            hasil = tambah(a, b)
        elif operator == '-':
            hasil = kurang(a, b)
        elif operator == '*':
            hasil = kali(a, b)
        elif operator == '/':
            hasil = bagi(a, b)
        else:
            hasil = "Operator tidak valid"
        
        print(f"\nHasil: {hasil}")
    
    except ValueError:
        print("Input harus angka!")

kalkulator()
```

### Example 2: Validasi dengan Functions

```python
def validasi_email(email):
    """Validasi format email sederhana"""
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    if email.count('@') != 1:
        return False
    return True

def validasi_password(password):
    """
    Validasi password:
    - Minimal 8 karakter
    - Ada huruf besar
    - Ada huruf kecil
    - Ada angka
    """
    if len(password) < 8:
        return False, "Password minimal 8 karakter"
    
    if not any(c.isupper() for c in password):
        return False, "Password harus ada huruf besar"
    
    if not any(c.islower() for c in password):
        return False, "Password harus ada huruf kecil"
    
    if not any(c.isdigit() for c in password):
        return False, "Password harus ada angka"
    
    return True, "Password valid"

# Test
email = input("Email: ")
if validasi_email(email):
    print("✓ Email valid")
else:
    print("✗ Email tidak valid")

password = input("Password: ")
valid, pesan = validasi_password(password)
if valid:
    print(f"✓ {pesan}")
else:
    print(f"✗ {pesan}")
```

## 💡 Best Practices

```python
# ✅ GOOD - Fungsi fokus pada satu tugas
def hitung_luas_persegi(sisi):
    return sisi ** 2

# ❌ BAD - Fungsi terlalu banyak tugas
def hitung_dan_print_dan_simpan(sisi):
    luas = sisi ** 2
    print(luas)
    # save to file
    # send email
    # ...

# ✅ GOOD - Nama deskriptif
def hitung_total_harga(harga, jumlah):
    return harga * jumlah

# ❌ BAD - Nama tidak jelas
def calc(x, y):
    return x * y

# ✅ GOOD - Docstring
def function():
    """Explains what function does"""
    pass

# ✅ GOOD - Return, jangan modify global
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
```

## ✅ Checklist Module 10

- [ ] Dapat membuat dan memanggil fungsi
- [ ] Memahami parameters dan arguments
- [ ] Menguasai return values
- [ ] Memahami local dan global scope
- [ ] Dapat menggunakan *args dan **kwargs
- [ ] Mengenal lambda functions

## ➡️ Selanjutnya
[Module 11 - Modules & Packages](../11-modules-packages/)

---

**Selamat! Anda sudah menyelesaikan Module 10! 🎉**
