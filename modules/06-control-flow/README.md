# Module 06 - Control Flow (If-Else)

## 🎯 Tujuan Pembelajaran

- Memahami konsep conditional statements
- Menguasai if, elif, else
- Dapat membuat nested conditions
- Memahami ternary operator
- Dapat membuat program dengan decision making

## 🔀 Apa itu Control Flow?

**Control Flow** menentukan urutan eksekusi kode berdasarkan kondisi tertentu.

```python
# Tanpa control flow
print("Baris 1")
print("Baris 2")
print("Baris 3")
# Semua baris dieksekusi

# Dengan control flow
umur = 15
if umur >= 17:
    print("Boleh punya KTP")  # Hanya dieksekusi jika kondisi True
else:
    print("Belum boleh punya KTP")
```

## 📝 If Statement

### Basic If

```python
# Sintaks:
# if kondisi:
#     kode yang dieksekusi jika kondisi True

umur = 20

if umur >= 18:
    print("Anda sudah dewasa")
    print("Boleh memilih dalam pemilu")

# Jika kondisi False, kode di dalam if tidak dieksekusi
umur = 15

if umur >= 18:
    print("Tidak akan terprint")  # Tidak dieksekusi

print("Program selesai")  # Tetap dieksekusi
```

### If-Else

```python
# Sintaks:
# if kondisi:
#     kode jika kondisi True
# else:
#     kode jika kondisi False

umur = 15

if umur >= 18:
    print("Sudah dewasa")
else:
    print("Masih anak-anak")  # Ini yang dieksekusi

# Real-world example: Login
password_benar = "python123"
password_input = input("Password: ")

if password_input == password_benar:
    print("Login berhasil!")
    print("Selamat datang!")
else:
    print("Password salah!")
    print("Akses ditolak")
```

### If-Elif-Else

```python
# Sintaks:
# if kondisi1:
#     kode
# elif kondisi2:
#     kode
# elif kondisi3:
#     kode
# else:
#     kode

# Grading system
nilai = 85

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"  # Ini yang dieksekusi
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Grade Anda: {grade}")

# ⚠️ Hanya SATU blok yang dieksekusi
nilai = 95

if nilai >= 60:
    print("Lulus")  # Ini dieksekusi
elif nilai >= 70:
    print("Tidak akan dieksekusi meskipun True")
elif nilai >= 80:
    print("Tidak akan dieksekusi meskipun True")
```

## 🔗 Multiple Conditions

### Logical Operators (and, or, not)

```python
# AND - semua kondisi harus True
umur = 25
punya_sim = True

if umur >= 17 and punya_sim:
    print("Boleh menyetir")

# OR - salah satu kondisi True sudah cukup
hari = "Sabtu"

if hari == "Sabtu" or hari == "Minggu":
    print("Akhir pekan!")

# NOT - membalik boolean
hujan = False

if not hujan:
    print("Tidak hujan, bisa pergi!")

# Kombinasi
umur = 25
member = True
total_belanja = 150000

if (umur >= 17 and member) or total_belanja >= 200000:
    print("Dapat diskon!")
```

### Comparison Chaining

```python
# ✅ Pythonic way
nilai = 85
if 80 <= nilai <= 89:
    print("Grade B")

# ❌ Cara lama
if nilai >= 80 and nilai <= 89:
    print("Grade B")

# Multiple chaining
x = 5
if 0 < x < 10 < 100:
    print("x antara 0 dan 10, dan 10 < 100")
```

## 🎯 Nested If (If Bersarang)

```python
# If di dalam if
umur = 20
punya_sim = True

if umur >= 17:
    print("Umur memenuhi syarat")
    if punya_sim:
        print("Punya SIM")
        print("Boleh menyetir!")
    else:
        print("Belum punya SIM")
        print("Daftar SIM dulu")
else:
    print("Umur belum cukup")

# Real-world: Login dengan role
username = "admin"
password = "admin123"
input_user = input("Username: ")
input_pass = input("Password: ")

if input_user == username:
    if input_pass == password:
        print("Login berhasil!")
        if username == "admin":
            print("Akses: Administrator")
        else:
            print("Akses: User biasa")
    else:
        print("Password salah!")
else:
    print("Username tidak ditemukan!")
```

## 🚀 Ternary Operator (Conditional Expression)

```python
# Sintaks: nilai_if_true if kondisi else nilai_if_false

# Cara biasa
umur = 20
if umur >= 18:
    status = "Dewasa"
else:
    status = "Anak-anak"

# Ternary operator (satu baris)
status = "Dewasa" if umur >= 18 else "Anak-anak"
print(status)  # Dewasa

# Contoh lain
nilai = 85
hasil = "Lulus" if nilai >= 60 else "Tidak Lulus"
print(hasil)  # Lulus

# Dengan print langsung
umur = 25
print("Dewasa" if umur >= 18 else "Anak-anak")

# Nested ternary (tapi jangan terlalu kompleks!)
nilai = 85
grade = "A" if nilai >= 90 else "B" if nilai >= 80 else "C"
print(grade)  # B

# ⚠️ Untuk yang kompleks, lebih baik gunakan if-elif-else biasa
```

## 💡 Truthy dan Falsy Values

```python
# Falsy values (dianggap False)
if 0:
    print("Tidak akan print")  # 0 adalah falsy

if "":
    print("Tidak akan print")  # string kosong adalah falsy

if []:
    print("Tidak akan print")  # list kosong adalah falsy

if None:
    print("Tidak akan print")  # None adalah falsy

# Truthy values (dianggap True)
if 1:
    print("Akan print")  # angka bukan 0 adalah truthy

if "hello":
    print("Akan print")  # string tidak kosong adalah truthy

if [1, 2, 3]:
    print("Akan print")  # list tidak kosong adalah truthy

# Practical usage
nama = input("Nama: ").strip()
if nama:  # Cek apakah nama tidak kosong
    print(f"Halo, {nama}!")
else:
    print("Nama tidak boleh kosong!")
```

## 📊 Match-Case (Python 3.10+)

```python
# Seperti switch-case di bahasa lain
command = input("Command (start/stop/pause): ")

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:  # default
        print("Unknown command")

# Dengan multiple values
hari = "Sabtu"

match hari:
    case "Senin" | "Selasa" | "Rabu" | "Kamis" | "Jumat":
        print("Hari kerja")
    case "Sabtu" | "Minggu":
        print("Akhir pekan")
    case _:
        print("Hari tidak valid")
```

## 🎮 Complete Examples

### Example 1: Kalkulator Sederhana

```python
print("=== KALKULATOR SEDERHANA ===")
angka1 = float(input("Angka pertama: "))
operator = input("Operator (+, -, *, /): ")
angka2 = float(input("Angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        print("Error: Tidak bisa dibagi 0!")
        hasil = None
else:
    print("Operator tidak valid!")
    hasil = None

if hasil is not None:
    print(f"Hasil: {hasil}")
```

### Example 2: Sistem Penilaian

```python
print("=== SISTEM PENILAIAN ===")
nama = input("Nama siswa: ")
nilai = float(input("Nilai (0-100): "))

# Validasi
if nilai < 0 or nilai > 100:
    print("Nilai harus antara 0-100!")
else:
    # Tentukan grade
    if nilai >= 90:
        grade = "A"
        keterangan = "Excellent"
    elif nilai >= 80:
        grade = "B"
        keterangan = "Good"
    elif nilai >= 70:
        grade = "C"
        keterangan = "Fair"
    elif nilai >= 60:
        grade = "D"
        keterangan = "Poor"
    else:
        grade = "E"
        keterangan = "Fail"
    
    # Tentukan status
    status = "LULUS" if nilai >= 60 else "TIDAK LULUS"
    
    # Output
    print("\n" + "=" * 40)
    print("HASIL PENILAIAN")
    print("=" * 40)
    print(f"Nama       : {nama}")
    print(f"Nilai      : {nilai}")
    print(f"Grade      : {grade}")
    print(f"Keterangan : {keterangan}")
    print(f"Status     : {status}")
    print("=" * 40)
```

## ✅ Checklist Module 06

- [ ] Memahami if, elif, else
- [ ] Dapat menggunakan logical operators
- [ ] Memahami nested if
- [ ] Dapat menggunakan ternary operator
- [ ] Memahami truthy dan falsy values

## ➡️ Selanjutnya
[Module 07 - Loops (Perulangan)](../07-loops/)
