import ridho002

A = [
    [4, -2, 5],
    [3, 1, -4],
    [2, 6, 7]
]

B = [
    [5, 6, 1],
    [7, 8, 5],
    [2, 3, 2]
]

print("===================================")
print("PROGRAM OPERASI ALJABAR MATRIKS")
print("===================================\n")

print("Matriks A")
ridho002.tampilkan_matriks(A)

print("\nMatriks B")
ridho002.tampilkan_matriks(B)

# PENJUMLAHAN
print("\nHASIL PENJUMLAHAN")
hasil = ridho002.tambah_matriks(A, B)
ridho002.tampilkan_matriks(hasil)

# PENGURANGAN
print("\nHASIL PENGURANGAN")
hasil = ridho002.kurang_matriks(A, B)
ridho002.tampilkan_matriks(hasil)

# TRANSPOSE
print("\nTRANSPOSE MATRIKS A")
hasil = ridho002.transpose(A)
ridho002.tampilkan_matriks(hasil)

# DETERMINAN
print("\nDETERMINAN MATRIKS A")
print(ridho002.determinan3x3(A))

# PERKALIAN
print("\nHASIL PERKALIAN")
hasil = ridho002.kali_matriks(A, B)
ridho002.tampilkan_matriks(hasil)

#Minor
print("\nMINOR MATRIK A")
hasil = ridho002.minor_matriks(A)
ridho002.tampilkan_matriks(hasil)

#Kofaktor
print("\nKOFAKTOR MATRIK A")
hasil = ridho002.kofaktor(A)
ridho002.tampilkan_matriks(hasil)