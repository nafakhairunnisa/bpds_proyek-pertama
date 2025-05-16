# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000, dengan lebih dari 1.000 karyawan yang tersebar di seluruh Indonesia. Seiring ekspansi bisnis, perusahaan menghadapi tantangan dalam manajemen sumber daya manusia, terutama dalam hal mempertahankan talenta dan mengelola beban kerja secara efisien.

Meskipun perusahaan telah tumbuh besar, Jaya Jaya Maju menghadapi tantangan dalam manajemen sumber daya manusia, khususnya tingginya tingkat attrition rate (rasio karyawan yang keluar). Berdasarkan data terbaru, attrition rate perusahaan telah melebihi 10%, yang tentu berdampak signifikan terhadap stabilitas operasional dan biaya SDM.

Untuk menangani isu ini, proyek ini bertujuan untuk menganalisis data historis karyawan dengan pendekatan analitik dan machine learning, guna mengidentifikasi faktor-faktor utama yang berkontribusi terhadap attrition. Hasil analisis kemudian divisualisasikan dalam bentuk business dashboard interaktif yang dapat membantu tim HR dalam mengambil keputusan berbasis data (data-driven) untuk merancang strategi retensi yang lebih efektif di masa depan.

### Permasalahan Bisnis

### Permasalahan Bisnis

Berdasarkan pemahaman bisnis yang telah dijelaskan, berikut adalah permasalahan utama yang dihadapi oleh perusahaan:

- Tingginya tingkat attrition (lebih dari 10%) yang berdampak pada kestabilan operasional, peningkatan biaya perekrutan, dan hilangnya knowledge retention.
- Kurangnya pemahaman yang berbasis data mengenai faktor-faktor utama penyebab karyawan meninggalkan perusahaan.
- Belum adanya sistem pemantauan atau early warning system berbasis data yang dapat mendeteksi risiko attrition secara proaktif.
- Tidak adanya strategi retensi karyawan yang terukur dan berbasis analisis, sehingga menyulitkan upaya preventif dalam menurunkan tingkat attrition secara berkelanjutan.

### Cakupan Proyek

Untuk menjawab permasalahan bisnis terkait tingginya tingkat attrition di Jaya Jaya Maju, proyek ini akan berfokus pada pemanfaatan data historis karyawan guna mengidentifikasi faktor-faktor kunci yang memengaruhi keputusan karyawan untuk keluar dari perusahaan.

Lingkup kegiatan dalam proyek ini mencakup:

- Melakukan Exploratory Data Analysis (EDA) untuk memahami distribusi data dan mengidentifikasi pola awal.
- Menganalisis hubungan antara variabel demografis dan pekerjaan (misalnya: usia, departemen, masa kerja, pendapatan, kepuasan kerja) terhadap status attrition.
- Membangun business dashboard interaktif untuk memvisualisasikan temuan secara informatif dan mendukung monitoring rutin oleh tim HR.
- Menyusun rekomendasi strategis berbasis temuan analisis untuk mendukung kebijakan retensi yang lebih efektif.
- Membangun model prediktif berbasis machine learning untuk mengklasifikasikan risiko attrition dan membantu deteksi dini terhadap potensi keluarnya karyawan.

### Persiapan

Sumber data: [Employee Data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Dataset awal berisi 1.470 data karyawan dengan 35 fitur. Hasil eksplorasi awal menunjukkan bahwa fitur `Attrition` (yang merupakan label target) memiliki 412 missing values.

Karena data tanpa label tidak bisa digunakan untuk pelatihan maupun evaluasi model klasifikasi, maka seluruh baris yang memiliki nilai kosong pada `Attrition` dihapus. Setelah pembersihan, dataset berkurang menjadi 1.058 baris data bersih.

Dataset yang telah dibersihkan disimpan ulang ke dalam file `employee_clean.csv` dan digunakan dalam proses analisis dan pembuatan dashboard berikutnya.

#### Data Preparation

Untuk memastikan kualitas data sebelum dilakukan analisis dan pemodelan, beberapa langkah persiapan dilakukan sebagai berikut:

- Penanganan Missing Value  
  Fitur `Attrition` yang merupakan label target memiliki 412 sampel kosong (missing values). Nilai-nilai tersebut dihapus agar tidak menimbulkan bias pada proses analisis. Dataset bersih kemudian disimpan ke dalam file baru bernama `employee_clean.csv`.

- Penanganan Outlier  
  Beberapa fitur numerik diperiksa untuk mendeteksi keberadaan outlier. Outlier ditangani dengan metode yang sesuai untuk menjaga distribusi data tetap representatif.

- Encoding Fitur Kategorikal  
  Fitur-fitur kategorikal seperti `Gender`, `Department`, dan `JobRole` dikonversi menjadi format numerik dengan teknik encoding agar dapat digunakan dalam pemodelan machine learning.

#### Feature Analysis (Chi-Square dan T-Test)
  Untuk mengetahui fitur mana saja yang paling berpengaruh terhadap tingkat `Attrition`, dilakukan analisis relevansi fitur menggunakan pendekatan statistik:
  - Chi-Square Test  
    Digunakan untuk fitur-fitur kategorikal. Tujuannya adalah untuk mengetahui apakah terdapat hubungan signifikan antara fitur kategorikal dengan variabel target `Attrition`.
  - T-Test (Uji t dua sampel)  
    Digunakan untuk fitur numerik. Uji ini mengevaluasi apakah terdapat perbedaan signifikan pada nilai rata-rata antara karyawan yang keluar (`Attrition = Yes`) dan yang bertahan (`Attrition = No`).

    Hasil dari pengujian ini membantu dalam proses feature selection, serta menjadi dasar dalam pemilihan fitur yang divisualisasikan pada dashboard, terutama fitur-fitur yang secara statistik signifikan terhadap attrition.

  - Splitting data. Fitur-fitur yang terpilih dimasukkan ke dalam dataframe baru dan displit berdasarkan training set 80% dan testing set 20% untuk modeling dan evaluation.

## Business Dashboard

### Dashboard

Business dashboard merupakan tools yang berisi grafik analitik dari suatu dataset. Pada studi kasus ini, dashboard digunakan untuk mengetahui alasan tingginya attrition berdasarkan fitur-fitur yang memiliki keterkaitan signifikan dengan attrition. Dengan demikian, tim HR dapat mengidentifikasi penyebab utama karyawan resign dan mengambil keputusan berbasis data.

Pemilihan fitur pada dashboard didasarkan pada hasil uji Chi-Square dan T-Test, yang dilakukan untuk mengidentifikasi variabel-variabel yang signifikan terhadap Attrition. Berdasarkan hasil tersebut, dipilih beberapa komponen utama yang divisualisasikan dalam dashboard, seperti ditunjukkan pada Tabel 1.

Tabel 1. Komponen Dashboard
| Komponen                      | Visualisasi                 | Jenis Data    | Tujuan    |
| ----------------------------- | --------------------------- | ------------- | ------------- |
| **KPI Summary**               | Total Karyawan, Total Attrition, Attrition Rate | Ringkasan     | Menyajikan ringkasan data attrition |
| **Filter**                    | Department                  | Filter Global | Filter berdasarkan  departemen |
| Resigned                    | Pie Chart                  | Label | Mengetahui jumlah resign dan stay |
| Job Role         | Horizontal Bar              | Kategorikal   | Melihat distribusi attrition berdasarkan posisi atau jabatan |
| Overtime         | Bar Chart                 | Kategorikal   | Perbandingan attrition antara karyawan yang lembur dan tidak |
| Marital Status   | Bar Chart                 | Kategorikal   | Apakah status pernikahan memengaruhi turnover |
| Job Satisfaction | Bar Chart           | Kategorikal   | Hubungan tingkat kepuasan kerja terhadap attrition |
| Distance from Home            | Histogram                   | Numerikal     | Apakah jarak rumah berpengaruh terhadap attrition |
| Monthly Income                | Bar Chart           | Numerikal     | Apakah penghasilan rendah lebih rentan terhadap attrition |
| Years at Company              | Bar Chart       | Numerikal     | Lama bekerja berkorelasi dengan attrition |

Tools yang digunakan untuk membuat dashboard adalah Tableau Public versi 2024.1. Dashboard ini dibuat interaktif agar siapapun dapat mengeksplorasi dan memperoleh insight secara mandiri dari data yang tersedia.

**Preview Dashboard**
![HR Dashboard](HR Dashboard.png)
Gambar 1. Preview Dashboard

Tautan dashboard dapat diakses [di sini](https://public.tableau.com/shared/RCC2KSMKP?:display_count=n&:origin=viz_share_link).

Insight dari dashboard:
- Total karyawan yang terdata adalah 1.058 orang.
- Terdapat 179 karyawan yang resign, yaitu sekitar 16.9% dari total.
- Laboratory Technician merupakan job role dengan tingkat attrition tertinggi, kemungkinan disebabkan oleh beban kerja yang berat.
- Karyawan yang kerja overtime cenderung lebih tinggi tingkat resign-nya dibanding yang tidak lembur.
- Karyawan yang berstatus single memiliki tingkat attrition tertinggi (26.7% dari seluruh karyawan single).
- Karyawan dengan nilai Job Satisfaction = 3 cenderung resign — bisa jadi karena merasa kurang puas terhadap kondisi kerja.
- Karyawan dengan rata-rata Monthly Income sebesar 4.873 lebih banyak yang resign, mengindikasikan bahwa pendapatan yang relatif rendah bisa berpengaruh terhadap keputusan keluar.
- Karyawan yang tinggal dalam radius 0–4 km dari kantor justru banyak yang resign, kemungkinan karena faktor lain di luar jarak.
- Karyawan yang bekerja selama 0–6 tahun paling banyak mengalami attrition, yang bisa mencerminkan fase eksplorasi di awal karier.
- Departemen Research & Development menjadi penyumbang attrition terbanyak, yakni 107 dari total 179 kasus attrition.

## Model Machine Learning

Model machine learning dikembangkan untuk memprediksi kemungkinan seorang karyawan akan keluar dari perusahaan (attrition) secara individual. Model ini bertujuan mendukung tim HR dalam mengambil keputusan berbasis data, seperti memberikan intervensi lebih awal bagi karyawan berisiko tinggi.

Setelah dilakukan eksperimen dengan beberapa algoritma, model Random Forest menunjukkan performa terbaik dengan akurasi sebesar 84%, sehingga dipilih sebagai model utama dalam proyek ini.

Model ini telah diimplementasikan ke dalam aplikasi web sederhana menggunakan Streamlit, agar dapat digunakan oleh pengguna non-teknis secara mudah.

Berikut link akses aplikasi: [Klik di sini](link).

Berikut cara run aplikasi di lokal:

**1. Download file zip**
**2. Setup Environment**
**Anaconda**
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
pip install streamlit
```
**Shell/Terminal**
```
mkdir bpds_proyek-pertama
cd bpds_proyek-pertama
pipenv install
pipenv shell
pip install -r requirements.txt
pip install streamlit
```
**3. Buka direktori file attrition_predict.py berada melalui anaconda**
```
cd ...\bpds_proyek-pertama
```
**4. Run streamlit app**
```
streamlit run attrition_predict.py
```

Aplikasi akan berjalan di browser secara otomatis dan menampilkan form prediksi attrition berdasarkan input karakteristik karyawan. Model ini dapat membantu dalam proses pengambilan keputusan preventif terhadap risiko resign.

## Conclusion

Berdasarkan hasil analisis data, visualisasi dashboard, serta implementasi model machine learning, proyek ini berhasil mengidentifikasi faktor-faktor utama yang memengaruhi keputusan karyawan untuk keluar dari perusahaan (attrition). Pengetahuan ini dapat digunakan sebagai dasar dalam pengambilan keputusan strategis oleh tim Human Resource (HR).

**Insights**:
- Tingkat attrition pada data mencapai 16.9% dari total 1.058 karyawan.
- Tujuh faktor signifikan penyebab utama tingginya attrition, yaitu:
    - Beban kerja yang berat terutama pada job role seperti Laboratory Technician.
    - Overtime (lembur) tinggi berdampak pada meningkatnya niat resign.
    - Status pernikahan, di mana karyawan lajang memiliki risiko attrition lebih tinggi.
    - Job satisfaction rendah, terutama pada nilai 3 dari skala 1–4.
    - Penghasilan rendah dan jarak rumah yang terlalu dekat atau terlalu jauh dapat memengaruhi loyalitas.
    - Lama bekerja <6 tahun menunjukkan masa rawan keluar, kemungkinan karena fase eksplorasi karier.
- Model machine learning Random Forest dengan akurasi 84% telah diimplementasikan dalam bentuk aplikasi prediksi attrition berbasis web (Streamlit).
- Dashboard interaktif telah dibuat menggunakan Tableau 2024.1 untuk memudahkan eksplorasi dan monitoring faktor risiko attrition.

**Rekomendasi Action Items**:
Untuk membantu perusahaan mengurangi angka attrition dan meningkatkan retensi karyawan, berikut lima rekomendasi action items yang bisa dilakukan:
- Membatasi lembur secara bertahap, dan evaluasi ulang beban kerja tiap job role yang terdampak attrition tinggi.
- Meningkatkan kompensasi dan tunjangan secara adil berdasarkan beban kerja dan tanggung jawab posisi.
- Melaksanakan survei kepuasan kerja berkala untuk mendeteksi job satisfaction dan menyesuaikan strategi retensi.
- Membangun program onboarding dan mentorship yang kuat untuk mendampingi karyawan baru dan mengurangi risiko keluar di masa awal kerja.