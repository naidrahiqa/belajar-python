# 🎯 Project 01: Kalkulator Lengkap

## Deskripsi
Buat kalkulator yang dapat melakukan operasi matematika dasar dan advanced.

## Fitur
1. Operasi dasar (+, -, *, /)
2. Operasi advanced (pangkat, akar, modulus)
3. History perhitungan
4. Clear history
5. Menu interaktif

## Konsep yang Digunakan
- Variables & Data Types
- Operators
- Control Flow (if-elif-else)
- Loops (while, for)
- Functions
- Lists (untuk history)

## Template Code

```python
def tambah(a, b):
    """Penjumlahan"""
    return a + b

def kurang(a, b):
    """Pengurangan"""
    return a - b

def kali(a, b):
    """Perkalian"""
    return a * b

def bagi(a, b):
    """Pembagian"""
    if b == 0:
        return "Error: Tidak bisa dibagi 0"
    return a / b

def pangkat(a, b):
    """Pangkat"""
    return a ** b

def akar(a):
    """Akar kuadrat"""
    if a < 0:
        return "Error: Tidak bisa akar dari bilangan negatif"
    return a ** 0.5

def tampilkan_menu():
    """Menampilkan menu"""
    print("\n" + "="*50)
    print("           KALKULATOR LENGKAP")
    print("="*50)
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (^)")
    print("6. Akar kuadrat (√)")
    print("7. Modulus (%)")
    print("8. Lihat History")
    print("9. Clear History")
    print("0. Keluar")
    print("="*50)

def main():
    """Fungsi utama"""
    history = []
    
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih operasi (0-9): ").strip()
        
        if pilihan == '0':
            print("\nTerima kasih telah menggunakan kalkulator!")
            break
        
        elif pilihan == '8':
            print("\n=== HISTORY ===")
            if history:
                for i, item in enumerate(history, 1):
                    print(f"{i}. {item}")
            else:
                print("History kosong")
        
        elif pilihan == '9':
            history.clear()
            print("\nHistory telah dihapus!")
        
        elif pilihan in ['1', '2', '3', '4', '5', '7']:
            try:
                a = float(input("Angka pertama: "))
                b = float(input("Angka kedua: "))
                
                if pilihan == '1':
                    hasil = tambah(a, b)
                    operasi = f"{a} + {b} = {hasil}"
                elif pilihan == '2':
                    hasil = kurang(a, b)
                    operasi = f"{a} - {b} = {hasil}"
                elif pilihan == '3':
                    hasil = kali(a, b)
                    operasi = f"{a} * {b} = {hasil}"
                elif pilihan == '4':
                    hasil = bagi(a, b)
                    operasi = f"{a} / {b} = {hasil}"
                elif pilihan == '5':
                    hasil = pangkat(a, b)
                    operasi = f"{a} ^ {b} = {hasil}"
                else:  # '7'
                    hasil = a % b
                    operasi = f"{a} % {b} = {hasil}"
                
                print(f"\nHasil: {hasil}")
                history.append(operasi)
                
            except ValueError:
                print("\nError: Input harus angka!")
        
        elif pilihan == '6':
            try:
                a = float(input("Angka: "))
                hasil = akar(a)
                operasi = f"√{a} = {hasil}"
                print(f"\nHasil: {hasil}")
                history.append(operasi)
            except ValueError:
                print("\nError: Input harus angka!")
        
        else:
            print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main()
```

## Cara Menjalankan
```bash
python kalkulator.py
```

## Challenge
1. Tambahkan operasi faktorial
2. Tambahkan konversi suhu (Celsius, Fahrenheit, Kelvin)
3. Tambahkan fitur simpan history ke file
4. Tambahkan error handling yang lebih baik
5. Buat versi GUI dengan tkinter

## Learning Outcomes
Setelah mengerjakan project ini, Anda akan:
- Lebih memahami functions dan cara mengorganisir code
- Mahir menggunakan control flow
- Memahami cara membuat program interaktif
- Bisa handle user input dengan baik
