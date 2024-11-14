## Kode program
```
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
```


## Output program
```
Masukkan nama siswa: Adit 
Masukkan nilai tugas: 100
Masukkan nilai UTS: 80
Masukkan nilai UAS: 90
Apakah ingin menambah data lagi? (y/t): t

Daftar Data Nilai Siswa:
Nama            Nilai Tugas     Nilai UTS       Nilai UAS       Nilai Akhir
Hanif           90.0            75.0            90.0            84.75
Rafly           100.0           80.0            75.0            84.25
Adit            100.0           80.0            90.0            89.50
PS C:\tugas membuat struk>
```

## Cara kerja program
Berikut adalah penjelasan cara kerja program berikut:

1. **Inisialisasi**: Program dimulai dengan membuat list kosong `data_nilai` untuk menyimpan data siswa.

2. **Input Data**:
   - Program meminta pengguna untuk memasukkan nama siswa.
   - Pengguna juga diminta untuk memasukkan nilai tugas, nilai UTS, dan nilai UAS.

3. **Penghitungan Nilai Akhir**:
   - Nilai akhir dihitung dengan rumus:
     \[
     \text{Nilai Akhir} = (\text{Nilai Tugas} \times 0.3) + (\text{Nilai UTS} \times 0.35) + (\text{Nilai UAS} \times 0.35)
     \]

4. **Penyimpanan Data**:
   - Data yang dimasukkan (nama dan nilai) disimpan dalam bentuk dictionary dan ditambahkan ke dalam list `data_nilai`.

5. **Tanya Lanjut**:
   - Program menanyakan apakah pengguna ingin memasukkan data lagi. Jika ya, proses input diulang. Jika tidak, program melanjutkan ke langkah berikutnya.

6. **Menampilkan Data**:
   - Setelah pengguna selesai memasukkan data, program menampilkan semua data siswa yang telah dimasukkan dalam format tabel.

7. **Selesai**: Program berakhir setelah menampilkan data.

Jika ada yang ingin Anda tanyakan lebih lanjut atau butuh penjelasan tambahan, silakan beri tahu!


## Flowchart
![flowchart](/flowchart5.png)

