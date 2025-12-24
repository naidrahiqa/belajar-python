# Module 01 - Pengenalan Python & Instalasi

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan modul ini, Anda akan:
- Memahami apa itu Python dan mengapa Python populer
- Mengetahui sejarah dan filosofi Python
- Dapat menginstal Python di komputer Anda
- Memahami cara menjalankan program Python
- Mengenal Python REPL dan IDE

## 📚 Apa itu Python?

### Definisi
**Python** adalah bahasa pemrograman tingkat tinggi (high-level programming language) yang:
- **Interpreted** - Kode dijalankan baris per baris oleh interpreter
- **Dynamically Typed** - Tidak perlu deklarasi tipe variabel
- **Object-Oriented** - Mendukung paradigma OOP
- **Multi-paradigm** - Mendukung procedural, OOP, dan functional programming

### Sejarah Python
- **Dibuat oleh**: Guido van Rossum
- **Tahun**: 1991
- **Nama**: Terinspirasi dari acara TV "Monty Python's Flying Circus"
- **Python 2** dirilis tahun 2000
- **Python 3** dirilis tahun 2008 (versi yang digunakan sekarang)

### Mengapa Python Populer?

#### 1. **Sintaks yang Mudah Dibaca**
Python menggunakan sintaks yang mirip bahasa Inggris dan menggunakan indentasi (spasi) untuk blok kode.

```python
# Contoh kode Python - sangat mudah dibaca!
nama = "Budi"
umur = 25

if umur >= 17:
    print(f"{nama} sudah dewasa")
else:
    print(f"{nama} masih anak-anak")
```

#### 2. **Produktivitas Tinggi**
Anda bisa menulis program dengan lebih sedikit baris kode dibanding bahasa lain.

**Contoh - Print angka 1-10:**

Python:
```python
for i in range(1, 11):
    print(i)
```

Java (sebagai perbandingan):
```java
public class Main {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }
    }
}
```

#### 3. **Library yang Sangat Banyak**
Python memiliki ribuan library untuk berbagai keperluan:
- **Web Development**: Django, Flask, FastAPI
- **Data Science**: Pandas, NumPy, Matplotlib
- **Machine Learning**: TensorFlow, PyTorch, Scikit-learn
- **Automation**: Selenium, PyAutoGUI
- **Dan masih banyak lagi!**

#### 4. **Komunitas yang Besar**
- Jutaan programmer Python di seluruh dunia
- Banyak tutorial, forum, dan sumber belajar gratis
- Mudah mendapat bantuan saat stuck

### Penggunaan Python

Python digunakan di berbagai bidang:

| Bidang | Contoh Penggunaan |
|--------|-------------------|
| 🌐 **Web Development** | Instagram, YouTube, Spotify, Pinterest |
| 📊 **Data Science** | Analisis data, visualisasi data |
| 🤖 **Machine Learning** | Self-driving cars, face recognition |
| 🎮 **Game Development** | Battlefield 2, Civilization IV |
| 🔬 **Scientific Computing** | NASA, CERN |
| 💼 **Automation** | Script otomasi tugas repetitif |
| 🔐 **Cybersecurity** | Penetration testing, security tools |

## 💻 Instalasi Python

### Windows

#### Step 1: Download Python
1. Kunjungi [python.org/downloads](https://www.python.org/downloads/)
2. Download Python versi terbaru (3.11+ recommended)
3. Pilih installer untuk Windows

#### Step 2: Install Python
1. Jalankan installer (.exe file)
2. ✅ **PENTING**: Centang "Add Python to PATH"
3. Klik "Install Now"
4. Tunggu hingga instalasi selesai

#### Step 3: Verifikasi Instalasi
1. Buka Command Prompt (tekan Win + R, ketik `cmd`)
2. Ketik command berikut:

```bash
python --version
```

Jika berhasil, akan muncul versi Python (contoh: Python 3.11.0)

### macOS

#### Step 1: Cek Python Terinstall
macOS biasanya sudah memiliki Python 2.7. Kita perlu install Python 3.

```bash
python3 --version
```

#### Step 2: Install dengan Homebrew (Recommended)
```bash
# Install Homebrew jika belum ada
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3
```

#### Step 3: Verifikasi
```bash
python3 --version
```

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3
sudo apt install python3 python3-pip

# Verifikasi
python3 --version
```

## 🚀 Cara Menjalankan Python

### 1. Python REPL (Interactive Mode)

**REPL** = Read-Eval-Print Loop

Ini adalah cara tercepat untuk mencoba kode Python.

```bash
# Buka REPL
python
```

Anda akan melihat prompt seperti ini:
```
>>>
```

Sekarang Anda bisa langsung ketik kode Python:

```python
>>> print("Hello, World!")
Hello, World!

>>> 2 + 2
4

>>> nama = "Python"
>>> print(f"Saya belajar {nama}")
Saya belajar Python

>>> exit()  # Keluar dari REPL
```

**Kapan menggunakan REPL?**
- Mencoba kode cepat
- Testing fungsi kecil
- Kalkulator
- Eksperimen

### 2. Menjalankan File Python

#### Step 1: Buat File Python
Buat file dengan ekstensi `.py`, contoh: `hello.py`

```python
# hello.py
print("Hello, World!")
print("Selamat datang di Python!")

nama = input("Siapa nama Anda? ")
print(f"Halo, {nama}!")
```

#### Step 2: Jalankan File
```bash
python hello.py
```

Output:
```
Hello, World!
Selamat datang di Python!
Siapa nama Anda? 
```

### 3. Menggunakan IDE/Text Editor

**IDE** = Integrated Development Environment

#### Popular Python IDEs:

**1. VS Code (Recommended untuk pemula)**
- Gratis dan ringan
- Extension Python yang powerful
- Integrated terminal
- Download: [code.visualstudio.com](https://code.visualstudio.com)

**Setup VS Code untuk Python:**
1. Install VS Code
2. Install Extension "Python" by Microsoft
3. Buat file `.py`
4. Tekan F5 untuk run

**2. PyCharm**
- IDE khusus untuk Python
- Banyak fitur profesional
- Ada versi Community (gratis)
- Download: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)

**3. Jupyter Notebook**
- Bagus untuk data science
- Interactive coding
- Install: `pip install jupyter`
- Run: `jupyter notebook`

**4. IDLE**
- Built-in dengan Python
- Sederhana untuk pemula
- Buka dengan mengetik `idle` di terminal

## 🔍 Anatomy of Python Program

Mari kita bedah program Python sederhana:

```python
# 1. KOMENTAR
# Ini adalah komentar. Komentar tidak dijalankan oleh Python
# Digunakan untuk menjelaskan kode

"""
Ini adalah multi-line comment (docstring)
Biasanya digunakan untuk dokumentasi
"""

# 2. IMPORT MODULES
import math  # Mengimport module math untuk operasi matematika

# 3. VARIABEL DAN KONSTANTA
nama = "Budi"  # String (teks)
umur = 25      # Integer (bilangan bulat)
PI = 3.14159   # Float (bilangan desimal) - konstanta biasanya UPPERCASE

# 4. FUNGSI
def sapa(nama):
    """
    Fungsi untuk menyapa seseorang
    Parameter: nama (string)
    Return: pesan sapaan (string)
    """
    return f"Halo, {nama}!"

# 5. MAIN PROGRAM
if __name__ == "__main__":
    # Kode di sini akan dijalankan saat file dieksekusi
    pesan = sapa(nama)
    print(pesan)
    print(f"Umur: {umur} tahun")
    print(f"Nilai PI: {PI}")
```

**Penjelasan:**
- **Baris 1-6**: Komentar untuk dokumentasi
- **Baris 9**: Import module external
- **Baris 12-14**: Deklarasi variabel
- **Baris 17-23**: Definisi fungsi
- **Baris 26-31**: Kode utama yang akan dieksekusi

## 📝 Konvensi Python (PEP 8)

**PEP 8** adalah style guide resmi Python. Berikut beberapa aturan penting:

### 1. Indentasi
Gunakan **4 spasi** untuk indentasi (bukan tab)

```python
# ✅ BENAR
if True:
    print("Benar")

# ❌ SALAH
if True:
  print("Salah")  # Hanya 2 spasi
```

### 2. Naming Conventions

```python
# Variables dan Functions: lowercase dengan underscore
nama_depan = "Budi"
def hitung_luas_persegi(sisi):
    return sisi * sisi

# Classes: PascalCase (CapitalizedWords)
class MobilBalap:
    pass

# Constants: UPPERCASE dengan underscore
MAX_SPEED = 200
PI = 3.14159
```

### 3. Spasi di Sekitar Operator

```python
# ✅ BENAR
x = 5 + 3

# ❌ SALAH
x=5+3  # Tidak ada spasi
```

### 4. Panjang Baris
Maksimal **79 karakter** per baris

```python
# Jika terlalu panjang, pecah menjadi beberapa baris
total = (nilai_matematika + nilai_fisika + 
         nilai_kimia + nilai_biologi)
```

## 🎯 Filosofi Python (The Zen of Python)

Ketik di Python REPL:

```python
>>> import this
```

Output:
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
...
```

**Prinsip penting:**
- Kode harus **mudah dibaca**
- **Sederhana** lebih baik daripada kompleks
- **Jelas** lebih baik daripada implicit

## ✅ Checklist Module 01

Sebelum lanjut ke modul berikutnya, pastikan Anda sudah:

- [ ] Memahami apa itu Python
- [ ] Menginstall Python di komputer
- [ ] Bisa menjalankan Python REPL
- [ ] Bisa membuat dan menjalankan file `.py`
- [ ] Memahami struktur dasar program Python
- [ ] Mengenal PEP 8 style guide

## 📖 Latihan

Lihat folder `exercises/` untuk latihan praktis!

## ➡️ Selanjutnya

[Module 02 - Variabel & Tipe Data](../02-variabel-tipe-data/)

---

**Selamat! Anda sudah menyelesaikan Module 01! 🎉**
