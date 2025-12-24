# 🐍 PYTHON CHEAT SHEET

## 📝 Variabel & Tipe Data

```python
# Variabel
nama = "Python"
umur = 30
tinggi = 175.5
is_active = True

# Tipe Data
int     # Integer: 1, 2, 3, -5
float   # Float: 3.14, -2.5
str     # String: "hello", 'world'
bool    # Boolean: True, False
None    # None type
```

## 🧮 Operators

```python
# Arithmetic
+   # Penjumlahan
-   # Pengurangan
*   # Perkalian
/   # Pembagian
//  # Floor Division
%   # Modulus
**  # Pangkat

# Comparison
==  # Sama dengan
!=  # Tidak sama dengan
>   # Lebih besar
<   # Lebih kecil
>=  # Lebih besar atau sama dengan
<=  # Lebih kecil atau sama dengan

# Logical
and  # Dan
or   # Atau
not  # Tidak
```

## 🔤 String Methods

```python
s = "Python Programming"

s.upper()          # PYTHON PROGRAMMING
s.lower()          # python programming
s.strip()          # Hapus whitespace
s.split()          # ['Python', 'Programming']
s.replace('P', 'J') # Jython Jrogramming
s.find('Py')       # 0
s.count('P')       # 2
s.startswith('Py') # True
s.endswith('ing')  # True
```

## 🔀 Control Flow

```python
# If-Elif-Else
if kondisi1:
    # kode
elif kondisi2:
    # kode
else:
    # kode

# Ternary
nilai = "A" if skor >= 90 else "B"
```

## 🔁 Loops

```python
# For Loop
for i in range(10):
    print(i)

for item in list:
    print(item)

for i, item in enumerate(list):
    print(f"{i}: {item}")

# While Loop
while kondisi:
    # kode

# Break & Continue
break     # Keluar dari loop
continue  # Skip iterasi saat ini
```

## 📦 Lists

```python
# Membuat list
lst = [1, 2, 3, 4, 5]
lst = list(range(10))

# Akses & Slicing
lst[0]      # Elemen pertama
lst[-1]     # Elemen terakhir
lst[1:4]    # Slice [index 1-3]

# Methods
lst.append(6)      # Tambah di akhir
lst.insert(0, 0)   # Insert di index 0
lst.remove(3)      # Hapus nilai 3
lst.pop()          # Hapus & return terakhir
lst.sort()         # Sort ascending
lst.reverse()      # Reverse
len(lst)           # Panjang list

# List Comprehension
[x**2 for x in range(10)]
[x for x in range(10) if x % 2 == 0]
```

## 📖 Dictionaries

```python
# Membuat dictionary
d = {"nama": "Budi", "umur": 25}
d = dict(nama="Budi", umur=25)

# Akses
d["nama"]        # "Budi"
d.get("nama")    # "Budi"
d.get("key", "default")

# Methods
d.keys()         # dict_keys(['nama', 'umur'])
d.values()       # dict_values(['Budi', 25])
d.items()        # dict_items([('nama', 'Budi'), ...])

# Update
d["kota"] = "Jakarta"  # Tambah/update
d.update({"tinggi": 175})

# Loop
for key in d:
    print(key)

for key, value in d.items():
    print(f"{key}: {value}")
```

## 🎯 Functions

```python
# Definisi
def fungsi(param1, param2):
    """Docstring"""
    return hasil

# Default parameters
def fungsi(a, b=10):
    return a + b

# *args & **kwargs
def fungsi(*args, **kwargs):
    pass

# Lambda
lambda x: x ** 2
lambda x, y: x + y
```

## 📄 File Handling

```python
# Write
with open("file.txt", "w") as f:
    f.write("Hello")

# Read
with open("file.txt", "r") as f:
    content = f.read()

# Append
with open("file.txt", "a") as f:
    f.write("New line\n")
```

## ⚠️ Exception Handling

```python
try:
    # kode yang mungkin error
except ValueError:
    # handle ValueError
except Exception as e:
    # handle general exception
else:
    # jika tidak ada error
finally:
    # selalu dieksekusi
```

## 📚 Modules

```python
# Import
import math
from math import pi, sqrt
from math import *
import math as m

# Membuat module
# file: mymodule.py
def my_function():
    pass
```

## 💡 Tips & Tricks

```python
# Swap values
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3

# Comprehensions
[x**2 for x in range(10)]           # List
{x: x**2 for x in range(10)}        # Dict
{x for x in range(10)}              # Set

# String multiplication
"-" * 50  # --------------------------------------------------

# Check membership
'a' in 'abc'  # True

# Ternary operator
"Genap" if x % 2 == 0 else "Ganjil"

# Chain comparisons
if 0 < x < 10:
    pass

# enumerate
for i, item in enumerate(['a', 'b', 'c']):
    print(f"{i}: {item}")

# zip
for a, b in zip([1,2,3], ['a','b','c']):
    print(f"{a}: {b}")
```

## 🎨 String Formatting

```python
nama = "Budi"
umur = 25

# F-strings (RECOMMENDED)
f"Nama: {nama}, Umur: {umur}"
f"Tahun depan: {umur + 1}"
f"Uppercase: {nama.upper()}"
f"Pi: {3.14159:.2f}"  # 3.14

# .format()
"Nama: {}, Umur: {}".format(nama, umur)
"Nama: {n}, Umur: {u}".format(n=nama, u=umur)

# % operator (old)
"Nama: %s, Umur: %d" % (nama, umur)
```

## 🐍 Python Zen

```python
import this

# Beautiful is better than ugly
# Simple is better than complex
# Readability counts
```

---

**Keep this cheat sheet handy! 📌**
