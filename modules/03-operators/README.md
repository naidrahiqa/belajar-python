# Module 03 - Operators (Operator)

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan modul ini, Anda akan:
- Memahami berbagai jenis operator di Python
- Dapat menggunakan arithmetic operators
- Menguasai comparison dan logical operators
- Memahami operator precedence (urutan operasi)
- Dapat menggunakan assignment operators dengan efisien

## 🧮 Apa itu Operator?

**Operator** adalah simbol khusus yang digunakan untuk melakukan operasi pada nilai dan variabel.

**Contoh sederhana:**
```python
hasil = 5 + 3  
# '+' adalah operator
# 5 dan 3 adalah operand
# hasil adalah variabel yang menyimpan hasil operasi
```

## 1️⃣ Arithmetic Operators (Operator Aritmatika)

Digunakan untuk operasi matematika.

### Tabel Arithmetic Operators

| Operator | Nama | Contoh | Hasil |
|----------|------|--------|-------|
| `+` | Penjumlahan | `5 + 3` | `8` |
| `-` | Pengurangan | `5 - 3` | `2` |
| `*` | Perkalian | `5 * 3` | `15` |
| `/` | Pembagian | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulus (Sisa bagi) | `5 % 2` | `1` |
| `**` | Pangkat | `5 ** 2` | `25` |

### Penjelasan Detail

#### Penjumlahan (`+`)
```python
# Penjumlahan angka
a = 10 + 5
print(a)  # 15

# Penjumlahan dengan variabel
x = 10
y = 20
total = x + y
print(total)  # 30

# String concatenation (penggabungan string)
nama_depan = "Budi"
nama_belakang = "Santoso"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # Budi Santoso
```

#### Pengurangan (`-`)
```python
# Pengurangan
selisih = 100 - 25
print(selisih)  # 75

# Negative number
suhu = -10  # Minus 10 derajat
print(suhu)  # -10
```

#### Perkalian (`*`)
```python
# Perkalian
luas = 5 * 4
print(luas)  # 20

# String repetition
garis = "-" * 20
print(garis)  # --------------------

seru = "Ya! " * 3
print(seru)  # Ya! Ya! Ya! 
```

#### Pembagian (`/`)
```python
# Pembagian normal - SELALU menghasilkan float
hasil = 10 / 2
print(hasil)  # 5.0 (bukan 5!)

hasil2 = 10 / 3
print(hasil2)  # 3.3333333333333335

# Bahkan jika hasil pembagiannya bulat, tetap float
print(type(10 / 2))  # <class 'float'>
```

#### Floor Division (`//`)
```python
# Pembagian bulat (dibulatkan ke bawah)
hasil = 10 // 3
print(hasil)  # 3 (bukan 3.33...)

hasil2 = 10 // 2
print(hasil2)  # 5

# Dengan bilangan negatif
print(10 // 3)   # 3
print(-10 // 3)  # -4 (dibulatkan ke bawah!)
print(10 // -3)  # -4

# Type: integer
print(type(10 // 3))  # <class 'int'>
```

**Kapan pakai `/` dan `//`?**
- Gunakan `/` untuk pembagian normal (matematika)
- Gunakan `//` ketika Anda butuh hasil integer (misalnya: membagi barang, halaman)

```python
# Contoh: Membagi 25 siswa ke dalam grup beranggotakan 4
siswa = 25
per_grup = 4
jumlah_grup = siswa // per_grup
print(f"Jumlah grup: {jumlah_grup}")  # 6 grup
sisa_siswa = siswa % per_grup
print(f"Sisa siswa: {sisa_siswa}")    # 1 siswa
```

#### Modulus (`%`)
```python
# Modulus = sisa pembagian
print(10 % 3)   # 1 (10 dibagi 3 = 3 sisa 1)
print(15 % 4)   # 3 (15 dibagi 4 = 3 sisa 3)
print(20 % 5)   # 0 (20 dibagi 5 = 4 sisa 0)

# Cek bilangan genap atau ganjil
angka = 7
if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")  # Output ini

# Cek kelipatan
angka = 15
if angka % 5 == 0:
    print("Kelipatan 5")  # Output ini
```

#### Pangkat (`**`)
```python
# Pangkat (Power)
hasil = 2 ** 3  # 2^3 = 2 * 2 * 2
print(hasil)  # 8

hasil2 = 5 ** 2  # 5^2 = 5 * 5
print(hasil2)  # 25

# Akar kuadrat menggunakan pangkat 0.5
akar = 16 ** 0.5
print(akar)  # 4.0

akar2 = 9 ** (1/2)
print(akar2)  # 3.0

# Pangkat negatif
hasil = 2 ** -3  # 1 / (2^3) = 1/8
print(hasil)  # 0.125
```

## 2️⃣ Assignment Operators (Operator Penugasan)

Digunakan untuk assign value ke variabel.

| Operator | Contoh | Sama dengan | Hasil |
|----------|--------|-------------|-------|
| `=` | `x = 5` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` | `x = 8` |
| `-=` | `x -= 3` | `x = x - 3` | `x = 2` |
| `*=` | `x *= 3` | `x = x * 3` | `x = 15` |
| `/=` | `x /= 3` | `x = x / 3` | `x = 1.666...` |
| `//=` | `x //= 3` | `x = x // 3` | `x = 1` |
| `%=` | `x %= 3` | `x = x % 3` | `x = 2` |
| `**=` | `x **= 3` | `x = x ** 3` | `x = 125` |

### Contoh Penggunaan

```python
# Basic assignment
x = 10
print(x)  # 10

# Addition assignment
x = 5
x += 3    # x = x + 3
print(x)  # 8

# Subtraction assignment
x = 10
x -= 4    # x = x - 4
print(x)  # 6

# Multiplication assignment
x = 5
x *= 2    # x = x * 2
print(x)  # 10

# Division assignment
x = 10
x /= 2    # x = x / 2
print(x)  # 5.0

# Real-world example: Counter
score = 0
print(f"Score: {score}")

# Player mendapat poin
score += 10
print(f"Score: {score}")  # 10

score += 5
print(f"Score: {score}")  # 15

# Player kehilangan poin
score -= 3
print(f"Score: {score}")  # 12
```

## 3️⃣ Comparison Operators (Operator Perbandingan)

Digunakan untuk membandingkan dua nilai. Hasilnya boolean (True/False).

| Operator | Nama | Contoh | Hasil |
|----------|------|--------|-------|
| `==` | Sama dengan | `5 == 5` | `True` |
| `!=` | Tidak sama dengan | `5 != 3` | `True` |
| `>` | Lebih besar | `5 > 3` | `True` |
| `<` | Lebih kecil | `5 < 3` | `False` |
| `>=` | Lebih besar atau sama dengan | `5 >= 5` | `True` |
| `<=` | Lebih kecil atau sama dengan | `3 <= 5` | `True` |

### Contoh Penggunaan

```python
# Equal to (==)
print(5 == 5)      # True
print(5 == 3)      # False
print("abc" == "abc")  # True

# Not equal to (!=)
print(5 != 3)      # True
print(5 != 5)      # False

# Greater than (>)
print(10 > 5)      # True
print(5 > 10)      # False
print(5 > 5)       # False

# Less than (<)
print(3 < 10)      # True
print(10 < 3)      # False

# Greater than or equal to (>=)
print(10 >= 5)     # True
print(5 >= 5)      # True
print(3 >= 5)      # False

# Less than or equal to (<=)
print(3 <= 5)      # True
print(5 <= 5)      # True
print(10 <= 5)     # False

# String comparison (alphabetical)
print("abc" < "xyz")   # True
print("apple" < "banana")  # True
print("Python" == "python")  # False (case-sensitive!)
```

### ⚠️ Perbedaan `=` dan `==`

```python
# = adalah ASSIGNMENT (memberi nilai)
x = 5  # Assign nilai 5 ke x

# == adalah COMPARISON (membandingkan)
print(x == 5)  # True (apakah x sama dengan 5?)

# Kesalahan umum pemula
# if x = 5:  # SALAH! Akan error
if x == 5:   # BENAR!
    print("x adalah 5")
```

### Penggunaan dalam Conditional

```python
# Example 1: Cek umur
umur = 20

if umur >= 18:
    print("Anda sudah dewasa")
else:
    print("Anda masih anak-anak")

# Example 2: Cek nilai
nilai = 85

if nilai >= 90:
    print("Grade: A")
elif nilai >= 80:
    print("Grade: B")
elif nilai >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Example 3: Password check
password = "python123"
input_password = input("Masukkan password: ")

if input_password == password:
    print("Login berhasil!")
else:
    print("Password salah!")
```

## 4️⃣ Logical Operators (Operator Logika)

Digunakan untuk menggabungkan conditional statements.

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `and` | True jika SEMUA kondisi True | `x > 5 and x < 10` |
| `or` | True jika SALAH SATU kondisi True | `x < 5 or x > 10` |
| `not` | Membalik boolean | `not(x > 5)` |

### AND Operator

```python
# AND - semua kondisi harus True
x = 7

# Cek apakah x antara 5 dan 10
if x > 5 and x < 10:
    print("x antara 5 dan 10")  # Output ini

# Truth table untuk AND
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Real-world example
umur = 25
punya_sim = True

if umur >= 17 and punya_sim:
    print("Boleh menyetir")
else:
    print("Tidak boleh menyetir")
```

### OR Operator

```python
# OR - salah satu kondisi True sudah cukup
hari = "Sabtu"

if hari == "Sabtu" or hari == "Minggu":
    print("Akhir pekan!")  # Output ini

# Truth table untuk OR
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Real-world example
cuaca = "hujan"
bawa_payung = True

if cuaca == "hujan" or cuaca == "berawan":
    if bawa_payung:
        print("Aman, bawa payung")
    else:
        print("Sebaiknya bawa payung")
```

### NOT Operator

```python
# NOT - membalik boolean
is_raining = False
is_sunny = not is_raining
print(is_sunny)  # True

# Truth table untuk NOT
print(not True)   # False
print(not False)  # True

# Real-world example
sudah_makan = False

if not sudah_makan:
    print("Waktunya makan!")  # Output ini

# Kombinasi
umur = 15
punya_izin_ortu = False

if not (umur >= 18) and not punya_izin_ortu:
    print("Tidak boleh masuk")
```

### Kombinasi Logical Operators

```python
# Kombinasi AND dan OR
umur = 25
member = True
belanja = 150000

# Diskon 10% jika:
# - Member DAN belanja >= 100000
# - ATAU belanja >= 200000
if (member and belanja >= 100000) or belanja >= 200000:
    diskon = belanja * 0.1
    total = belanja - diskon
    print(f"Dapat diskon! Total: Rp {total}")
else:
    print(f"Tidak dapat diskon. Total: Rp {belanja}")
```

## 5️⃣ Identity Operators

Membandingkan apakah dua variabel merujuk ke objek yang sama di memori.

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `is` | True jika kedua variabel adalah objek yang sama | `x is y` |
| `is not` | True jika kedua variabel bukan objek yang sama | `x is not y` |

```python
# Identity operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x == y)   # True (nilai sama)
print(x is y)   # False (objek berbeda di memori)
print(x is z)   # True (z merujuk ke objek yang sama dengan x)

# Gunakan 'is' untuk None
nilai = None
if nilai is None:
    print("Nilai adalah None")

# Jangan gunakan 'is' untuk angka atau string (kecuali None dan boolean)
# Gunakan == untuk perbandingan nilai
```

## 6️⃣ Membership Operators

Mengecek apakah nilai ada di dalam sequence (string, list, tuple, dll).

| Operator | Deskripsi | Contoh |
|----------|-----------|--------|
| `in` | True jika nilai ada dalam sequence | `'a' in 'abc'` |
| `not in` | True jika nilai tidak ada dalam sequence | `'x' not in 'abc'` |

```python
# in operator
text = "Python Programming"
print('P' in text)      # True
print('Java' in text)   # False

# Cek substring
print('Pyth' in text)   # True
print('python' in text) # False (case-sensitive!)

# not in operator
print('Java' not in text)  # True

# Real-world example
email = input("Email: ")
if '@' in email and '.' in email:
    print("Email valid")
else:
    print("Email tidak valid")

# List membership (akan dipelajari lebih detail nanti)
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Ada apple!")
```

## 🎯 Operator Precedence (Urutan Operasi)

Ketika ada multiple operators, Python mengikuti urutan tertentu.

### Urutan Precedence (dari tertinggi ke terendah)

1. `()` - Parentheses
2. `**` - Exponentiation
3. `+x`, `-x`, `~x` - Unary plus, minus, bitwise NOT
4. `*`, `/`, `//`, `%` - Multiplication, Division, Floor division, Modulus
5. `+`, `-` - Addition, Subtraction
6. `<`, `<=`, `>`, `>=`, `==`, `!=` - Comparisons
7. `not` - Logical NOT
8. `and` - Logical AND
9. `or` - Logical OR

### Contoh

```python
# Tanpa parentheses
hasil = 2 + 3 * 4
print(hasil)  # 14 (bukan 20!) karena * didahulukan

# Dengan parentheses
hasil = (2 + 3) * 4
print(hasil)  # 20

# Complex expression
hasil = 10 + 5 * 2 - 3
# 10 + (5 * 2) - 3
# 10 + 10 - 3
# 17
print(hasil)  # 17

# Dengan parentheses untuk clarity
hasil = ((10 + 5) * 2) - 3
# (15 * 2) - 3
# 30 - 3
# 27
print(hasil)  # 27

# Best practice: Gunakan parentheses untuk clarity!
# Lebih baik terlalu banyak tanda kurung daripada ambiguous
```

## 💡 Tips & Best Practices

### 1. Gunakan Parentheses untuk Clarity
```python
# ❌ Membingungkan
if x > 5 and y < 10 or z == 0:
    pass

# ✅ Lebih jelas
if (x > 5 and y < 10) or (z == 0):
    pass
```

### 2. Spacing di Sekitar Operators
```python
# ❌ Sulit dibaca
x=5+3*2

# ✅ Mudah dibaca
x = 5 + 3 * 2
```

### 3. Comparison Chaining
```python
# ❌ Panjang
if x > 5 and x < 10:
    pass

# ✅ Lebih pythonic
if 5 < x < 10:
    pass

# Berlaku untuk semua comparison
if 0 <= score <= 100:
    print("Score valid")
```

## ✅ Checklist Module 03

Pastikan Anda memahami:

- [ ] Arithmetic operators (+, -, *, /, //, %, **)
- [ ] Perbedaan `/` dan `//`
- [ ] Assignment operators (=, +=, -=, dll)
- [ ] Comparison operators (==, !=, >, <, >=, <=)
- [ ] Perbedaan `=` dan `==`
- [ ] Logical operators (and, or, not)
- [ ] Operator precedence
- [ ] Membership operators (in, not in)

## 📖 Latihan

Lihat folder `exercises/` untuk latihan praktis!

## ➡️ Selanjutnya

[Module 04 - String & String Methods](../04-string-methods/)

---

**Selamat! Anda sudah menyelesaikan Module 03! 🎉**
