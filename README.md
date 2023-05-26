# Deteksi-Sakit-Kepala-Backward-Chaining
Sistem Pakar untuk mendiagnosis penyakit sakit kepala
sistem pakar yang menggunakan metode inferensi backward chaining untuk mendiagnosis penyakit sakit kepala berdasarkan gejala yang dialami pasien. Berikut adalah penjelasan konsep-konsep yang digunakan dalam program tersebut:
1.	Aturan sistem pakar
Sistem pakar memanfaatkan aturan-aturan yang sudah didefinisikan sebelumnya untuk mendiagnosis penyakit. Dalam program ini, aturan-aturan tersebut didefinisikan dalam bentuk kamus Python, dengan setiap penyakit memiliki satu atau lebih aturan yang mengaitkan gejala-gejala dengan penyakit tersebut.

2.	Gejala-gejala yang dialami pasien
Gejala-gejala yang dialami pasien didefinisikan dalam bentuk daftar Python. Daftar ini kemudian digunakan oleh sistem pakar untuk mencocokkan gejala-gejala yang dialami pasien dengan aturan-aturan yang sudah didefinisikan sebelumnya. Contoh :
• 1, Rasa nyeri terus menerus pada kedua sisi kepala
  2, Terasa tekanan di belakang mata
  3, Otot leher yang tegang
  4, Adanya rasa mual
  5, Rasa demam dan linglung
  6, Pandangan kabur
  7, Sakit kepala pada satu sisi
  8, Kepala terasa sering berdenyut
  9, Pening
  10, Menjadi sensitif pada suara, bau, cahaya, atau sentuhan
  11, Nyeri disertai sensasi terbakar atau tertusuk
  12, Terasa sakit di sisi kepala yang sama
  13, Sakit terpusat di belakang satu mata
  14, Hidung tersumbat
  15, Mata berair

3.	Metode inferensi backward chaining
Sistem pakar menggunakan metode inferensi backward chaining untuk mencari penyakit yang mungkin dialami pasien berdasarkan gejala-gejala yang dialami. Metode inferensi ini bekerja dengan cara memulai dari hipotesis akhir (yaitu penyakit yang ingin didiagnosis) dan mencari fakta-fakta yang dapat mendukung hipotesis tersebut, hingga didapatkan gejala-gejala yang dialami pasien. Dalam program ini, metode inferensi backward chaining dilakukan dengan fungsi backward_chaining.

4.	Hasil diagnosis
Setelah mencocokkan gejala-gejala yang dialami pasien dengan aturan-aturan yang sudah didefinisikan, sistem pakar akan memberikan diagnosis yang paling sesuai dengan gejala-gejala yang dialami pasien. Dalam program ini, diagnosis diberikan dalam bentuk teks yang ditampilkan di layar.

Secara keseluruhan di atas menunjukkan cara sistem pakar dapat digunakan untuk mendiagnosis penyakit berdasarkan gejala yang dialami pasien. Program ini hanya merupakan contoh sederhana, dan dalam implementasi yang lebih kompleks, sistem pakar dapat mengandung lebih banyak aturan dan mempertimbangkan lebih banyak faktor dalam proses diagnosis.

Nama Kelompok :
1204004     -   JOSE CHASEY PRATAMA
1204022     -   HANAN DESTRIARIN KISHENDRIAN
1204025     -   CHRISTIAN YUDA PRATAMA
1204026     -   HARYADI YUSUF

