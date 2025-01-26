# Data Wilayah BPS dan Kemendagri

Repository ini berisi skrip Python untuk mengambil dan menyimpan data wilayah dari Badan Pusat Statistik (BPS) dan Kementerian Dalam Negeri (Kemendagri) berdasarkan kabupaten, kecamatan, dan desa/kelurahan. Data yang diambil mengacu pada Periode Wilkerstat 2023 Semester 1 (BPS) - 2022 (Kemendagri).

## Deskripsi

Skrip ini melakukan scraping data dari API BPS untuk mendapatkan informasi mengenai:
- Kode BPS dan Nama BPS untuk kabupaten
- Kode DAGRI dan Nama DAGRI untuk kabupaten
- Kode BPS dan Nama BPS untuk kecamatan
- Kode DAGRI dan Nama DAGRI untuk kecamatan
- Kode BPS dan Nama BPS untuk desa/kelurahan
- Kode DAGRI dan Nama DAGRI untuk desa/kelurahan

Data yang diambil akan disimpan dalam format CSV dengan nama file yang sesuai dengan nama kabupaten.

## Fitur

- Mengambil data kabupaten, kecamatan, dan desa/kelurahan dari API BPS.
- Menyimpan data dalam format CSV.
- Menyertakan informasi periode dan sumber dalam file CSV.


### Penyesuaian kode provinsi
url_kabupaten = "https://sig.bps.go.id/rest-bridging/getwilayah?level=kabupaten&parent=12&periode_merge=2023_1.2022"

Untuk provinsi lain, ganti 12 dengan kode provinsi yang sesuai.


## Prerequisites

Sebelum menjalankan skrip ini, pastikan Anda telah menginstal Python dan library yang diperlukan. Anda dapat menginstal library yang diperlukan dengan perintah berikut:

```bash
pip install requests pandas


