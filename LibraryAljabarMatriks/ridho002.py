# ==========================================
# LIBRARY ALJABAR MATRIKS
# Nama : Ridho
# NPM  : 2555061002
# ==========================================

def tambah_matriks(A, B):
    hasil = []

    for i in range(len(A)):
        baris = []

        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])

        hasil.append(baris)

    return hasil


def kurang_matriks(A, B):
    hasil = []

    for i in range(len(A)):
        baris = []

        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])

        hasil.append(baris)

    return hasil


def transpose(A):
    hasil = []

    for j in range(len(A[0])):
        baris = []

        for i in range(len(A)):
            baris.append(A[i][j])

        hasil.append(baris)

    return hasil


def kali_matriks(A, B):

    if len(A[0]) != len(B):
        return "Perkalian tidak dapat dilakukan"

    hasil = []

    for i in range(len(A)):
        baris = []

        for j in range(len(B[0])):

            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            baris.append(total)

        hasil.append(baris)

    return hasil


def determinan3x3(A):

    if len(A) != 3 or len(A[0]) != 3:
        return "Matriks harus berordo 3x3"

    a = A[0][0]
    b = A[0][1]
    c = A[0][2]

    d = A[1][0]
    e = A[1][1]
    f = A[1][2]

    g = A[2][0]
    h = A[2][1]
    i = A[2][2]

    det = (
        a * ((e * i) - (f * h))
        - b * ((d * i) - (f * g))
        + c * ((d * h) - (e * g))
    )

    return det


def tampilkan_matriks(M):

    for baris in M:
        print(baris)


def minor_matriks(A):
    minor = []
    for i in range(3):
        baris = []
        for j in range(3):
            sub = []
            for r in range(3):
                if r != i:
                    temp = []
                    for c in range(3):
                        if c != j:
                            temp.append(A[r][c])
                    sub.append(temp)
            det_sub = (sub[0][0] * sub[1][1]) - (sub[0][1] * sub[1][0])
            baris.append(det_sub)
        minor.append(baris)
    return minor

def kofaktor(A):
    minor = minor_matriks(A)
    kof = []
    for i in range(3):
        baris = []
        for j in range(3):
            tanda = (-1) ** (i + j)
            baris.append(tanda * minor[i][j])
        kof.append(baris)
    return kof