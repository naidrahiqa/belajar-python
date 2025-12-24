# ============================================
# PROGRAM: Interactive Program
# Deskripsi: Program yang berinteraksi dengan user
# ============================================

"""
Program ini mendemonstrasikan:
1. Cara menerima input dari user
2. Cara memproses input
3. Cara menampilkan output yang dipersonalisasi
"""

# Header program yang menarik
print("=" * 50)
print("         PROGRAM PERKENALAN INTERAKTIF")
print("=" * 50)
print()

# Menerima input dari user
# input() akan menampilkan prompt dan menunggu user mengetik
nama = input("Siapa nama Anda? ")
umur = input("Berapa umur Anda? ")
hobi = input("Apa hobi Anda? ")

# Memberikan jarak (empty line)
print()

# Menampilkan hasil dengan format yang rapi
print("=" * 50)
print("           PROFIL ANDA")
print("=" * 50)
print(f"Nama  : {nama}")
print(f"Umur  : {umur} tahun")
print(f"Hobi  : {hobi}")
print("=" * 50)

# Pesan penutup yang dipersonalisasi
print()
print(f"Senang berkenalan dengan Anda, {nama}!")
print(f"Semoga Anda menikmati hobi {hobi} Anda! 😊")

# ============================================
# CATATAN PENTING:
# - input() SELALU mengembalikan string (teks)
# - Jika Anda butuh angka, harus di-convert:
#   umur = int(input("Umur: "))
# ============================================
