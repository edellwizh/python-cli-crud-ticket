# Python CLI CRUD System

## Deskripsi & Latar Belakang
Proyek ini dibuat sebagai bagian dari **Kuis Kuliah** Algoritma dan Pemrograman. 

Melalui tugas ini, saya mendapatkan sebuah *insight* baru: **Saya baru benar-benar paham bahwa konsep CRUD (Create, Read, Update, Delete) tidak harus menggunakan *Database* (DB)**. Logika CRUD ternyata bisa dibangun dan dipahami dari bentuk sederhana, yaitu menyimpan data sementara di dalam memori program menggunakan CLI (*Command Line Interface*).

## Apa yang Saya Pelajari?
Selain memahami fondasi CRUD, dalam proyek ini saya mengeksplorasi dan mempraktikkan beberapa fitur penting di Python:

1. **`match-case`**: Menggunakan fitur modern Python (pengganti `if-elif`) untuk membuat navigasi menu terminal yang jauh lebih rapi dan terstruktur.
2. **Built-in Modules (`random` & `datetime`)**: 
   - Memanfaatkan modul `random` untuk men-generate kode/ID unik secara otomatis.
   - Menggunakan `datetime` untuk mengambil tahun saat ini dan memformat tanggal secara dinamis.
3. **Pencegahan Error TANPA Blok Eksepsi (`try...except`)**:
   Ini adalah bagian pembelajaran favorit saya. karena saya baru menyadari bahwa kita bisa menangani berbagai *input* yang tidak valid (misalnya mencegah program *crash* karena *user* memasukkan huruf pada kolom angka) **tanpa harus bergantung pada fungsi `try...except`**. Semua potensi *error* (`ValueError`, `TypeError`)
   berhasil dicegah sejak awal menggunakan logika perulangan dan metode *string* bawaan Python seperti:
   - `.isdecimal()`, `.isdigit()`, `.isalpha()` (Mencegah *error* sebelum tipe data diubah ke `int`)
   - `.istitle()`, `.title()`
   - `.split()`, `.strip()`
   - `.startswith()`
5. **String Slicing**: Memanipulasi indeks string untuk menyensor data sensitif (seperti menyensor nomor HP: `0812******89`).

## Fitur Program
- **Create**: Mendaftarkan data baru dengan validasi input yang ketat berlapis.
- **Read**: Menampilkan detail data yang sudah terdaftar dengan format yang mudah dibaca (*formatting string*).
- **Update**: Mengubah sebagian data tanpa menghancurkan data lainnya, lengkap dengan *looping* validasi ulang.
- **Delete**: Menghapus data dari memori (reset variabel) dengan sistem konfirmasi (y/n) untuk mencegah penghapusan tidak sengaja.
