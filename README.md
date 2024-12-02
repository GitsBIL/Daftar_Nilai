# Data Nilai Mahasiswa
Nama    : Nabil Putra Alamsyah
Nim     : 312410376

Program ini adalah aplikasi sederhana berbasis Python untuk mengelola data nilai mahasiswa. Aplikasi ini memanfaatkan fungsi-fungsi untuk menambahkan, menampilkan, mengubah, dan menghapus data mahasiswa dengan format yang mudah digunakan.

## Fitur Utama
    -Menambahkan Data Mahasiswa: Memasukkan nama mahasiswa beserta nilai tugas, UTS, dan UAS.
    -Menampilkan Data Mahasiswa: Menampilkan semua data mahasiswa dalam format tabel.
    -Menghapus Data Mahasiswa: Menghapus data mahasiswa berdasarkan nama.
    -Mengubah Data Mahasiswa: Mengubah nilai mahasiswa berdasarkan nama.

## Struktur Program
    1. tambah()
        Fungsi untuk menambahkan data mahasiswa.

    2. tampilkan()
        Fungsi untuk menampilkan semua data mahasiswa.

    3. hapus(nama)
        Fungsi untuk menghapus data mahasiswa berdasarkan nama.

    4. ubah(nama)
        Fungsi untuk mengubah data mahasiswa berdasarkan nama.

## Langkah - langkah membuat program :

### 1. Membuat Struktur Data untuk Menyimpan Data Mahasiswa
        - Gunakan list untuk menyimpan data mahasiswa.
        - Setiap mahasiswa akan disimpan sebagai dictionary yang berisi nama, nilai tugas, UTS, UAS, dan nilai akhir.

![Gambar](./Gambar/gambar1.png)

### 2. Fungsi Tambah()
        - Tambahkan fungsi untuk memasukkan data mahasiswa.
        - Gunakan input dari pengguna untuk mendapatkan nama, nilai tugas, UTS, dan UAS.
        - Hitung nilai akhir berdasarkan bobot.
        - Simpan data mahasiswa ke dalam list data_mahasiswa.

![Gambar](./Gambar/gambar2.png)

### 3. Fungsi tampilkan()
        - Tambahkan fungsi untuk mencetak semua data mahasiswa.
        - Tampilkan data dalam format tabel.
    
![Gambar](./Gambar/gambar3.png)

### 4. Fungsi hapus(nama)
        - Tambahkan fungsi untuk menghapus data mahasiswa berdasarkan nama.
        - Gunakan perulangan untuk mencari mahasiswa dengan nama yang diberikan.

![Gambar](./Gambar/)

### 5. Fungsi ubah(nama)
        - Tambahkan fungsi untuk mengubah data mahasiswa berdasarkan nama.
        - Jika ditemukan, minta input nilai baru dan perbarui data.

![Gambar](./Gambar/gambar5.png)

### 6. Buat Menu Utama
        - Tambahkan logika utama untuk menampilkan menu dan memanggil fungsi berdasarkan pilihan pengguna.

![Gambar](./Gambar/gambar6.png)

### 7. Flowchart

![Gambar](./Gambar/Flowchart_Mahasiswa.jpg)

### 8. Penjelasan Akhir
    - Program menggunakan list untuk menyimpan data mahasiswa.
    - Setiap operasi dilakukan melalui fungsi, sehingga mudah dipelihara dan dikembangkan.
    - Menu utama memberikan antarmuka sederhana untuk pengguna.

## 9. Contoh Output
    - Menu Utama :

![Gambar](./Gambar/gambar7.png)

    - Menu Tabel Data Mahasiswa :

![Gambar](./Gambar/gambar8.png)