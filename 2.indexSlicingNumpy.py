import numpy as np

print('# Bilangan random 0-1 (distribusi uniform)')
print(np.random.rand(7))

print('# Bilangan random 0-1 dalam bilangan matrik 2D (distribusi uniform)')
print(np.random.rand(5, 4))


print('# Bilangan random dari minus takterhingga hingga tak terhingga (distribusi gursian)')
print(np.random.randn(3, 4))

print('# Bilangan random integer randint(awal, akhir, banyaknya)')
print(np.random.randint(0, 10, 20))

print('# Merubah array angka menjadi matrik 2D reshape(baris, kolom)')
bilangan = np.random.randint(0, 10, 20)
print(bilangan.reshape(4, 5))

bil1d = np.random.randint(0, 100, 20)
bil2d = np.random.randint(0, 100, 20).reshape(4, 5)

# Mencari bilangan paling besar
print(bil1d.max())
print(bil2d.max())

# Mencari bilangan paling kecil
print(bil1d.min())
print(bil2d.min())

# Mencari no index bilangan
print(bil1d.argmax())
print(bil2d.argmin())

number = np.arange(0, 11)
print(number[6]) # Mendapatkan angka nomer index 6
print(number[5:]) # Mendapatkan angka nomor index 5 sampai habis
print(number[:5]) # Mendapatkan angka nomor index 0 sampai 5
print(number[5:8]) # Mendapatkan angka nomor index 5 sampai 8

# Mengabil nilai matrik berdasarkan no index
bil = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(bil[2, 1]) # [baris, kolom]
print(bil[bil>5]) # mengabil nilai yg lebih besar dari 5