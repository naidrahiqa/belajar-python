# Module 08 - Lists & Tuples

## 🎯 Tujuan Pembelajaran

- Memahami Lists dan Tuples
- Dapat melakukan operasi pada Lists
- Menguasai list methods
- Memahami list slicing dan indexing
- Mengerti perbedaan Lists dan Tuples
- Dapat menggunakan list comprehension

## 📋 Lists

**List** adalah collection yang ordered, mutable (bisa diubah), dan allow duplicate values.

### Membuat List

```python
# Empty list
lst = []
lst = list()

# List dengan data
angka = [1, 2, 3, 4, 5]
buah = ["apel", "jeruk", "mangga"]
mixed = [1, "dua", 3.0, True, [5, 6]]

# List from range
numbers = list(range(10))  # [0,1,2,3,4,5,6,7,8,9]
```

### Accessing Elements

```python
buah = ["apel", "jeruk", "mangga", "pisang"]

# Positive indexing (dari kiri, mulai 0)
print(buah[0])   # apel
print(buah[1])   # jeruk

# Negative indexing (dari kanan, mulai -1)
print(buah[-1])  # pisang
print(buah[-2])  # mangga

# Slicing [start:stop:step]
print(buah[0:2])    # ['apel', 'jeruk']
print(buah[1:])     # ['jeruk', 'mangga', 'pisang']
print(buah[:2])     # ['apel', 'jeruk']
print(buah[::2])    # ['apel', 'mangga']
print(buah[::-1])   # Reverse
```

### List Methods

```python
# append() - tambah di akhir
buah = ["apel"]
buah.append("jeruk")
print(buah)  # ['apel', 'jeruk']

# insert() - sisipkan di index tertentu
buah.insert(0, "mangga")
print(buah)  # ['mangga', 'apel', 'jeruk']

# extend() - gabungkan dengan list lain
buah.extend(["pisang", "anggur"])
print(buah)  # ['mangga', 'apel', 'jeruk', 'pisang', 'anggur']

# remove() - hapus nilai tertentu (first occurrence)
buah.remove("apel")

# pop() - hapus dan return (default: terakhir)
last = buah.pop()
first = buah.pop(0)

# clear() - hapus semua
buah.clear()

# index() - cari index nilai tertentu
buah = ["apel", "jeruk", "mangga"]
idx = buah.index("jeruk")  # 1

# count() - hitung berapa kali nilai muncul
angka = [1, 2, 2, 3, 2, 4]
print(angka.count(2))  # 3

# sort() - sort in-place
angka = [3, 1, 4, 1, 5, 9]
angka.sort()  # [1, 1, 3, 4, 5, 9]
angka.sort(reverse=True)  # [9, 5, 4, 3, 1, 1]

# sorted() - return sorted copy
angka = [3, 1, 4]
sorted_angka = sorted(angka)  # angka tetap [3,1,4]

# reverse() - reverse in-place
angka.reverse()
```

### List Operations

```python
# Concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2  # [1, 2, 3, 4]

# Repetition
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# Membership
print(1 in [1, 2, 3])  # True
print(5 not in [1, 2, 3])  # True

# Length
print(len([1, 2, 3]))  # 3

# Min/Max/Sum
angka = [1, 5, 3, 9, 2]
print(min(angka))  # 1
print(max(angka))  # 9
print(sum(angka))  # 20
```

## 📦 Tuples

**Tuple** adalah collection yang ordered, immutable (tidak bisa diubah), dan allow duplicates.

### Membuat Tuple

```python
# Empty tuple
tpl = ()
tpl = tuple()

# Tuple dengan data
coordinates = (10, 20)
data = (1, "dua", 3.0, True)

# Single element tuple (perlu comma!)
single = (1,)  # Tuple
not_tuple = (1)  # Integer!

# Tanpa parentheses (tuple packing)
point = 10, 20  # (10, 20)
```

### Accessing Tuples

```python
coords = (10, 20, 30)

# Indexing (sama seperti list)
print(coords[0])   # 10
print(coords[-1])  # 30

# Slicing (sama seperti list)
print(coords[0:2])  # (10, 20)

# Tuple unpacking
x, y, z = coords
print(x)  # 10
print(y)  # 20
```

### Tuple Methods (Terbatas)

```python
# count()
angka = (1, 2, 2, 3, 2)
print(angka.count(2))  # 3

# index()
print(angka.index(3))  # 3

# Tidak ada append, remove, sort, dll
# Karena tuple immutable!
```

### Kapan Pakai List vs Tuple?

```python
# ✅ Gunakan LIST untuk:
# - Data yang bisa berubah
siswa = ["Budi", "Siti"]
siswa.append("Andi")  # OK

# ✅ Gunakan TUPLE untuk:
# - Data yang fixed/constant
coordinates = (10, 20)
# coordinates.append(30)  # Error!

# - Return multiple values dari function
def min_max(numbers):
    return min(numbers), max(numbers)

# - Dictionary keys (tuple bisa, list tidak)
location = {(0, 0): "origin", (1, 1): "point"}
```

## 🔁 Looping Lists/Tuples

```python
buah = ["apel", "jeruk", "mangga"]

# Loop dengan value
for item in buah:
    print(item)

# Loop dengan index
for i in range(len(buah)):
    print(f"{i}: {buah[i]}")

# Loop dengan enumerate (pythonic!)
for i, item in enumerate(buah):
    print(f"{i}: {item}")

# Loop dengan index custom start
for i, item in enumerate(buah, start=1):
    print(f"{i}. {item}")
```

## 💎 List Comprehension

Cara singkat dan elegant membuat list.

```python
# Cara biasa
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(10)]

# Dengan kondisi
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Transform list
buah = ["APEL", "JERUK", "MANGGA"]
lower = [f.lower() for f in buah]
# ['apel', 'jeruk', 'mangga']

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0,0,0], [0,1,2], [0,2,4]]

# Dengan if-else
numbers = [1, 2, 3, 4, 5]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
```

## ✅ Checklist
- [ ] Memahami Lists dan cara mengaksesnya
- [ ] Menguasai list methods
- [ ] Memahami Tuples dan immutability
- [ ] Dapat loop Lists/Tuples
- [ ] Menguasai list comprehension

## ➡️ Selanjutnya
[Module 09 - Dictionaries & Sets](../09-dictionaries-sets/)
