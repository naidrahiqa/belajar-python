# Module 07 - Loops (Perulangan)

## 🎯 Tujuan Pembelajaran

- Memahami konsep perulangan (loops)
- Menguasai for loop dan while loop
- Dapat menggunakan range() function
- Memahami break, continue, dan else dalam loops
- Dapat membuat nested loops
- Memahami list comprehension (preview)

## 🔄 Apa itu Loop?

**Loop** adalah struktur yang mengulang eksekusi kode berkali-kali.

```python
# Tanpa loop - repetitive!
print("Baris 1")
print("Baris 2")
print("Baris 3")
print("Baris 4")
print("Baris 5")

# Dengan loop - efisien!
for i in range(1, 6):
    print(f"Baris {i}")
```

## 🔁 For Loop

Loop yang mengiterasi sequence (list, string, range, dll).

### Sintaks Dasar

```python
# Sintaks:
# for item in sequence:
#     kode yang diulang

# Loop through list
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(item)

# Output:
# apel
# jeruk
# mangga

# Loop through string
for huruf in "Python":
    print(huruf)
# P y t h o n
```

### range() Function

`range()` menghasilkan sequence of numbers.

```python
# range(stop) - dari 0 sampai stop-1
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# range(start, stop) - dari start sampai stop-1
for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8

# Range dengan step negatif (mundur)
for i in range(10, 0, -1):
    print(i)
# Output: 10 9 8 7 6 5 4 3 2 1

# Range tidak menghasilkan list langsung (efisien memory)
print(type(range(5)))  # <class 'range'>
print(list(range(5)))  # [0, 1, 2, 3, 4]
```

### enumerate() - Loop dengan Index

```python
# Dapatkan index dan value sekaligus
buah = ["apel", "jeruk", "mangga"]

# Cara biasa
for i in range(len(buah)):
    print(f"{i}: {buah[i]}")

# Cara pythonic dengan enumerate
for index, item in buah:
    print(f"{index}: {item}")

# Output:
# 0: apel
# 1: jeruk
# 2: mangga

# enumerate dengan custom start
for index, item in enumerate(buah, start=1):
    print(f"{index}. {item}")
# 1. apel
# 2. jeruk
# 3. mangga
```

### Loop through Dictionary

```python
siswa = {
    "nama": "Budi",
    "umur": 20,
    "kota": "Jakarta"
}

# Loop through keys
for key in siswa:
    print(key)
# nama umur kota

# Loop through values
for value in siswa.values():
    print(value)
# Budi 20 Jakarta

# Loop through key-value pairs
for key, value in siswa.items():
    print(f"{key}: {value}")
# nama: Budi
# umur: 20
# kota: Jakarta
```

## ⚡ While Loop

Loop yang berjalan selama kondisi True.

### Sintaks Dasar

```python
# Sintaks:
# while kondisi:
#     kode yang diulang

# Hitung mundur
counter = 5
while counter > 0:
    print(counter)
    counter -= 1
# Output: 5 4 3 2 1

# While True (infinite loop) dengan break
while True:
    password = input("Password: ")
    if password == "python123":
        print("Login berhasil!")
        break
    else:
        print("Password salah, coba lagi")
```

### Perbedaan For vs While

```python
# FOR - Ketika tahu berapa kali loop
for i in range(10):
    print(i)

# WHILE - Ketika tidak tahu berapa kali loop
password_benar = "python123"
while True:
    password = input("Password: ")
    if password == password_benar:
        break

# FOR - Iterasi sequence
buah = ["apel", "jeruk"]
for item in buah:
    print(item)

# WHILE - Based on condition
saldo = 100000
while saldo > 0:
    tarik = int(input("Tarik: "))
    saldo -= tarik
    print(f"Saldo: {saldo}")
```

## 🛑 Break, Continue, Pass

### break - Keluar dari loop

```python
# Break menghentikan loop sepenuhnya
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4 (berhenti di 5)

# Real-world: Cari item
angka = [1, 5, 3, 8, 2, 9]
target = 8

for num in angka:
    if num == target:
        print(f"Ditemukan: {target}")
        break
else:
    print(f"{target} tidak ditemukan")
```

### continue - Skip iterasi saat ini

```python
# Continue melanjutkan ke iterasi berikutnya
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)
# Output: 1 3 5 7 9 (hanya odd numbers)

# Real-world: Skip invalid data
data = [10, -5, 20, 0, 30, -10, 40]
for num in data:
    if num <= 0:
        continue  # Skip negative dan zero
    print(f"Processing: {num}")
```

### pass - Placeholder

```python
# Pass tidak melakukan apa-apa (placeholder)
for i in range(5):
    if i == 2:
        pass  # TODO: implement later
    else:
        print(i)

# Berguna untuk struktur yang belum diimplementasi
def function_belum_jadi():
    pass  # Implementation nanti
```

## 🔁 Loop dengan else

Loop bisa punya clause `else` yang dieksekusi jika loop selesai normal (tanpa break).

```python
# For loop dengan else
for i in range(5):
    print(i)
else:
    print("Loop selesai!")

# Dengan break - else tidak dieksekusi
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Tidak akan print karena ada break")

# Real-world: Cari item
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Ditemukan: {target}")
        break
else:
    print(f"{target} tidak ada dalam list")
```

## 🔲 Nested Loops

Loop di dalam loop.

```python
# Nested for loop
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print()  # New line after each row

# Pattern printing
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
# *
# **
# ***
# ****
# *****

# Nested loop dengan 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
```

## 💡 List Comprehension (Preview)

Cara singkat membuat list dengan loop.

```python
# Cara biasa
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# List comprehension (pythonic)
squares = [i ** 2 for i in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dengan kondisi
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_squares)
# [0, 4, 16, 36, 64]
```

## 🎮 Complete Examples

### Example 1: Tabel Perkalian

```python
print("=== TABEL PERKALIAN ===\n")

angka = int(input("Masukkan angka: "))
batas = int(input("Sampai berapa: "))

print(f"\nTabel Perkalian {angka}:")
print("-" * 20)

for i in range(1, batas + 1):
    hasil = angka * i
    print(f"{angka} x {i:2} = {hasil:3}")
```

### Example 2: Menu Loop

```python
print("=== MENU APLIKASI ===")

while True:
    print("\n1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("0. Exit")
    
    pilihan = input("\nPilih: ")
    
    if pilihan == "1":
        print("Anda memilih Option 1")
    elif pilihan == "2":
        print("Anda memilih Option 2")
    elif pilihan == "3":
        print("Anda memilih Option 3")
    elif pilihan == "0":
        print("Goodbye!")
        break
    else:
        print("Pilihan tidak valid!")
```

### Example 3: Validasi Input

```python
# Input validation dengan while loop
while True:
    try:
        umur = int(input("Umur (1-150): "))
        if 1 <= umur <= 150:
            break
        else:
            print("Umur harus antara 1-150!")
    except ValueError:
        print("Input harus angka!")

print(f"Umur Anda: {umur}")
```

### Example 4: Pattern Generator

```python
print("=== PATTERN GENERATOR ===\n")

tinggi = int(input("Tinggi pattern: "))

# Pattern 1: Right triangle
print("\nPattern 1:")
for i in range(1, tinggi + 1):
    print("* " * i)

# Pattern 2: Pyramid
print("\nPattern 2:")
for i in range(1, tinggi + 1):
    spasi = " " * (tinggi - i)
    bintang = "* " * i
    print(spasi + bintang)

# Pattern 3: Diamond
print("\nPattern 3:")
# Upper half
for i in range(1, tinggi + 1):
    print(" " * (tinggi - i) + "* " * i)
# Lower half
for i in range(tinggi - 1, 0, -1):
    print(" " * (tinggi - i) + "* " * i)
```

## ⚡ Performance Tips

```python
# ✅ GOOD - Iterasi langsung
for item in buah:
    print(item)

# ❌ BAD - Iterasi dengan index (jika tidak perlu)
for i in range(len(buah)):
    print(buah[i])

# ✅ GOOD - enumerate jika perlu index
for i, item in enumerate(buah):
    print(f"{i}: {item}")

# ✅ GOOD - List comprehension untuk simple cases
squares = [x**2 for x in range(10)]

# ❌ BAD - Loop untuk append (jika bisa pakai comprehension)
squares = []
for x in range(10):
    squares.append(x**2)
```

## ✅ Checklist Module 07

- [ ] Memahami for loop dan while loop
- [ ] Dapat menggunakan range() function
- [ ] Menguasai break dan continue
- [ ] Memahami loop dengan else
- [ ] Dapat membuat nested loops
- [ ] Mengenal list comprehension

## ➡️ Selanjutnya
[Module 08 - Lists & Tuples](../08-lists-tuples/)

---

**Selamat! Anda sudah menyelesaikan Module 07! 🎉**
