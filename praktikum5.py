# Membuat list kosong untuk menyimpan data
data_nilai = []

# Menggunakan perulangan untuk meminta input data sebanyak-banyaknya
while True:
    # Meminta input nama dan nilai dari pengguna
    nama = input("Masukkan nama siswa: ")
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    
    # Menghitung nilai akhir dengan bobot masing-masing komponen
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
    
    # Menyimpan data ke dalam list sebagai dictionary
    data_nilai.append({
        'Nama': nama,
        'Nilai Tugas': nilai_tugas,
        'Nilai UTS': nilai_uts,
        'Nilai UAS': nilai_uas,
        'Nilai Akhir': nilai_akhir
    })
    
    # Menanyakan apakah ingin menambah data lagi
    lanjut = input("Apakah ingin menambah data lagi? (y/t): ").lower()
    if lanjut == 't':
        break

# Menampilkan daftar data yang sudah dimasukkan
print("\nDaftar Data Nilai Siswa:")
print("Nama\t\tNilai Tugas\tNilai UTS\tNilai UAS\tNilai Akhir")
for data in data_nilai:
    print(f"{data['Nama']}\t\t{data['Nilai Tugas']}\t\t{data['Nilai UTS']}\t\t{data['Nilai UAS']}\t\t{data['Nilai Akhir']:.2f}")
