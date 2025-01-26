import requests
import pandas as pd

# URL untuk mengambil data kabupaten
url_kabupaten = "https://sig.bps.go.id/rest-bridging/getwilayah?level=kabupaten&parent=12&periode_merge=2023_1.2022"

# Mengambil data kabupaten
response_kabupaten = requests.get(url_kabupaten)

# Memeriksa apakah permintaan berhasil
if response_kabupaten.status_code == 200:
    # Mengonversi data JSON menjadi objek Python
    data_kabupaten = response_kabupaten.json()
    
    # Mengambil data kecamatan dan desa untuk setiap kabupaten
    for kabupaten in data_kabupaten:
        kode_bps_kabupaten = kabupaten['kode_bps']
        nama_kabupaten = kabupaten['nama_bps']
        kode_dagri_kabupaten = kabupaten['kode_dagri']
        nama_dagri_kabupaten = kabupaten['nama_dagri']
        
        # Mengambil data kecamatan
        url_kecamatan = f"https://sig.bps.go.id/rest-bridging/getwilayah?level=kecamatan&parent={kode_bps_kabupaten}&periode_merge=2023_1.2022"
        response_kecamatan = requests.get(url_kecamatan)
        
        if response_kecamatan.status_code == 200:
            data_kecamatan = response_kecamatan.json()
            all_data = []  # Reset list untuk setiap kabupaten
            for kecamatan in data_kecamatan:
                kode_bps_kecamatan = kecamatan['kode_bps']
                nama_kecamatan = kecamatan['nama_bps']
                kode_dagri_kecamatan = kecamatan['kode_dagri']
                nama_dagri_kecamatan = kecamatan['nama_dagri']
                
                # Mengambil data desa
                url_desa = f"https://sig.bps.go.id/rest-bridging/getwilayah?level=desa&parent={kode_bps_kecamatan}&periode_merge=2023_1.2022"
                response_desa = requests.get(url_desa)
                
                if response_desa.status_code == 200:
                    data_desa = response_desa.json()
                    for desa in data_desa:
                        # Menyimpan semua informasi ke dalam list
                        all_data.append([
                            kode_bps_kabupaten, 
                            nama_kabupaten, 
                            kode_dagri_kabupaten, 
                            nama_dagri_kabupaten,
                            kode_bps_kecamatan, 
                            nama_kecamatan, 
                            kode_dagri_kecamatan, 
                            nama_dagri_kecamatan,
                            desa['kode_bps'], 
                            desa['nama_bps'], 
                            desa['kode_dagri'], 
                            desa['nama_dagri']
                        ])
                else:
                    print(f"Terjadi kesalahan saat mengambil data desa untuk kecamatan {nama_kecamatan}: {response_desa.status_code}")
        else:
            print(f"Terjadi kesalahan saat mengambil data kecamatan untuk kabupaten {nama_kabupaten}: {response_kecamatan.status_code}")
        
        # Membuat DataFrame dari data yang telah dikumpulkan
        df = pd.DataFrame(all_data, columns=[
            'Kode BPS Kabupaten', 
            'Nama BPS Kabupaten', 
            'Kode DAGRI Kabupaten', 
            'Nama DAGRI Kabupaten',
            'Kode BPS Kecamatan', 
            'Nama BPS Kecamatan', 
            'Kode DAGRI Kecamatan', 
            'Nama DAGRI Kecamatan',
            'Kode BPS Desa', 
            'Nama BPS Desa', 
            'Kode DAGRI Desa', 
            'Nama DAGRI Desa'
        ])
        
        # Menambahkan informasi tambahan sebagai baris pertama
        info_header = pd.DataFrame([
            ["Periode Wilkerstat 2023 Semester 1 (BPS) - 2022 (Kemendagri)"],
            ["Sumber: https://sig.bps.go.id/bridging-kode/index"]
        ])
        info_header.columns = ['Informasi']
        
        # Menggabungkan header dengan data
        df_final = pd.concat([info_header, df], ignore_index=True)
        
        # Mengganti spasi dan karakter khusus dalam nama kabupaten untuk nama file
        safe_nama_kabupaten = nama_kabupaten.replace(" ", "_").replace(".", "").replace(",", "").replace("(", "").replace(")", "")
        file_name = f"data_{safe_nama_kabupaten}.csv"
        
        # Menyimpan DataFrame ke dalam file CSV
        df.to_csv(file_name, index=False, encoding='utf-8')
        print(f"Data untuk kabupaten {nama_kabupaten} berhasil disimpan ke dalam file '{file_name}'")
else:
    print(f"Terjadi kesalahan saat mengambil data kabupaten: {response_kabupaten.status_code}")
