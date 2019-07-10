# naive-bayes
Machine Learning

Naïve Bayes Classifier merupakan sebuah metoda klasifikasi yang berakar pada teorema Bayes. Metode pengklasifikasian dg menggunakan metode probabilitas dan statistik yg dikemukakan oleh ilmuwan Inggris Thomas Bayes, yaitu memprediksi peluang di masa depan berdasarkan pengalaman di masa sebelumnya sehingga dikenal sebagai Teorema Bayes. Ciri utama dr Naïve Bayes Classifier ini adalah asumsi yg sangat kuat (naïf) akan independensi dari masing-masing kondisi / kejadian.

Studi Kasus:

Diberikan sebuah Trainset berupa himpunan data berisi 160 objek data yang memiliki 7 atribut input (age, workclass, education, marital-status, occupation, relationship, hours-per-week) dan 1 output (label kelas income) yang memiliki 2 kelas/label (>50K, dan <=50K). Bangunlah sebuah sistem klasifikasi menggunakan metode Naïve Bayes untuk menentukan kelas/label data testing dalam Testset. Sistem membaca masukan file TrainsetTugas1ML.csv  dan TestsetTugas1ML.csv dan mengeluarkan output berupa file TebakanTugas1ML.csv berupa satu kolom berisi 40 baris yang menyatakan kelas/label baris yang bersesuaian pada file TestsetTugas1ML.csv. Teorema Bayes menyediakan sebuah jalan untuk menghitung posterior probability P(c|x) dari P(c), P(x) dan P(x|c)

Strategi Penyelesaian Masalah :

Step 1: Membuat tabel frekuensi untuk semua fitur terhadap kelas yang berbeda.
Step 2: Gambar tabel kesamaan untuk semua fitur terhadap kelas yang berbeda.
Step 3: Hitung probabilitas bersyarat untuk semua kelas.
Step 4: Hitung maxiP (Ci | x1, x2, ..., xn). Dalam contoh tabel dari Train Set, probabilitas maksimum untuk kelas income >50, yakni, age = young, workclass = private, education = some-college, merupakan class income >50 oleh Algoritma Naive Bayes.
