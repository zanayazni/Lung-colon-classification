

# Lung-colon-classification

## Deskripsi

Repositori ini digunakan untuk classification kanker paru-paru dan kolon menggunakan machine learning. Terdapat dua komponen utama:

- **Tubes_PCD.ipynb**: Notebook Jupyter untuk eksplorasi data, preprocessing, training model, dan evaluasi.
- **WebApps**: Folder berisi aplikasi web untuk menggunakan model secara interaktif.

---

## Cara Penggunaan

### 1. Menjalankan Tubes_PCD.ipynb

1. **Persyaratan**:  
   - Pastikan sudah menginstall Jupyter Notebook dan dependensi yang dibutuhkan (lihat requirements di bawah).
   - Anda bisa menggunakan Anaconda atau pip untuk instalasi library yang diperlukan.

2. **Buka Notebook**:  
   - Jalankan terminal/command prompt.
   - Navigasi ke direktori repository ini.
   - Ketik `jupyter notebook` lalu tekan Enter.
   - Buka file `Tubes_PCD.ipynb` di browser yang muncul.

3. **Jalankan Sel**:  
   - Jalankan setiap sel secara berurutan untuk melakukan preprocessing data, training, dan evaluasi model.
   - Ikuti instruksi atau penjelasan yang tersedia di dalam notebook.

### 2. Menjalankan Aplikasi Web (WebApps)

1. **Masuk ke Folder WebApps**:  
   - Buka terminal/command prompt dan masuk ke folder `WebApps`:
     ```
     cd WebApps
     ```

2. **Install Dependensi**:  
   - Pastikan sudah menginstall Python 3.x.
   - Install semua dependensi yang dibutuhkan (misalnya Flask, Streamlit, atau library lain yang digunakan di WebApps).

3. **Menjalankan Aplikasi**:  
     ```
     streamlit run webapps.py
     ```
   - Ikuti instruksi di terminal. Biasanya aplikasi akan bisa diakses melalui browser di alamat `http://localhost:5000` atau sesuai yang tertera.

---

## Requirements

Beberapa library yang umumnya dibutuhkan:

- numpy
- pandas
- scikit-learn
- matplotlib
- flask / streamlit (untuk WebApps)
- jupyter

Install dengan pip:
```
pip install numpy pandas scikit-learn matplotlib flask streamlit jupyter
```

---

## Catatan

- Pastikan dataset yang digunakan sudah berada di path yang benar seperti disebutkan di notebook atau aplikasi web.
- Untuk detail lebih lanjut, baca komentar di dalam kode masing-masing file.

---

