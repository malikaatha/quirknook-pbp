# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
Malika Atha Indurasmi <br />
2306275203 <br />
PBP A <br />
### Link to PWS Deployment: http://malika-atha31-quirknook.pbp.cs.ui.ac.id/ <br /> 
### Link to Repository: https://github.com/malikaatha/quirknook-pbp <br />

## Cara pengimplementasian checklist secara step-by-step

### 1. Membuat proyek Django
- Setelah menginisiasi git pada direktori utama yang berjudul **quirknook**, saya menghubungkan direktori tersebut dengan repository github yang berjudul **quirknook-pbp**. Setelah itu, untuk menginstal Django, saya mengaktifkan virtual environment dengan mengetik command `python -m venv env`, lalu `env\Scripts\activate`. Virtual environment berfungsi untuk menginstall package yang diperlukan hanya pada direktori tertentu tanpa memengaruhi direktori lain agar tidak terjadi conflict. <br /> <br />
- Di dalam direktori yang sama, saya membuat berkas berjudul **requirements.txt**, yaitu dokumen yang berisi dependencies yang dibutuhkan untuk diinstal pada direktori tersebut. Untuk membaca dan menginstall dependencies pada berkas tersebut, saya menjalankan perintah `pip install -r requirements.txt`. Setelah terinstal, maka saya menuliskan perintah `django-admin startproject quirknook` untuk membuat proyek django baru yang berjudul quirknook. Jika proyek django telah dibuat, maka file yang muncul di direktori tersebut di antara lain adalah **manage.py, __init__.py, asgi.py, settings.py, urls.py, wsgi.py** <br /> <br />
- Jika proyek sudah berhasil dibuat, yang selanjutnya saya lakukan adalah menlakukan konfigurasi agar proyek tersebut berjalan dengan sesuai. Untuk deployment, kita perlu menambahkan akses untuk host lokal, yaitu menambahkan `ALLOWED_HOSTS = ["localhost", "127.0.0.1"]` pada file **settings.py**.<br /> <br />
- Untuk menjalankan server Django, saya me-run perintah `python manage.py runserver`, lalu membuka local host (http://localhost:8000/). Jika sudah muncul animasi roket, maka proyek Django telah berhasil dibuat dan saya dapat menonaktifkan server Django dan juga virtual environment. <br /> <br />

### 2. Membuat aplikasi main
- Untuk membuat sebuah Django app, maka kita dapat menjalankan perintah `python manage.py startapp main`. Artinya, kita akan membuat sebuah direktori baru yang berjudul main dengan struktur berupa file-file untuk pembuatan aplikasi Django yang dibuat. <br /> <br />

### 3. Routing pada proyek untuk aplikasi main
- Untuk menambahkan aplikasi yang telah kita buat ke penggunaan Django, kita harus menambahkan nama aplikasi ke dalam konfigurasi di **settings.py** sebagai berikut: `INSTALLED_APPS = [...,'main']`<br /> <br />

### 4. Membuat model pada aplikasi dengan atribut name, price, description
- Model berisi data yang akan diproses oleh aplikasi kita. Data yang diperlukan yaitu berupa beberapa atribut seperti nama produk, harga, dan juga deskripsi produk. <br /> <br />
- Atribut-atribut dapat didefinisikan di dalam sebuah class. Class yang saya buat berjudul Product, yang nantinya akan memiliki attributes berupa nama produk, harga, dan juga deskripsi produk. <br /> <br />
- Atribut diimplementasikan dengan suatu variabel yang terikat dengan suatu data type tertentu. Contohnya adalah untuk nama produk menggunakan CharField, harga produk menggunakan IntegerField, serta deskripsi produk menggunakan TextField. <br /> <br />
- Pengimplementasian variabel tersebut dalam kode contohnya adalah sebagai berikut untuk deskripsi produk: `description = models.TextField()` <br /> <br />
- Jika saya telah selesai membuat/mengubah model, maka hal yang harus dilakukan adalah migrasi model. Migrasi model adalah cara Django melacak perubahan pada model basis data. Migrasi model dilakukan dengan command berikut: `python manage.py makemigrations` lalu `python manage.py migrate`<br /> <br />

### 5. Membuat fungsi pada views.py untuk dikembalikan ke template
- Buat fungsi show_main yang menerima parameter request untuk mengatur penerimaan http dan menampilkan tampilan yang sesuai. <br /> <br />
- Didalam fungsi show_main, terdapat dictionary _***context***_ yang berisi key berupa nama dari variabel data-data yang ingin ditampilkan pada template. Value dari key tersebut merupakan data yang nantinya akan ditampilkan pada template. <br /> <br />
- Terdapat tiga argumen return render, yaitu *request, "main.html", dan context*, yaitu request merupakan permintaan HTTP yang dikirim, *main.html* berupa berkas template untuk merender tampilan, dan *context* merupakan dictionary yang berisi data untuk ditampilkan secara dinamis. <br /> <br />

### 6. Routing pada urls.py untuk memetakan fungsi pada views.py
- Buat **urls.py** di direktori aplikasi `main` dan atur rute URL menggunakan `path('', show_main, name='show_main')` untuk menampilkan tampilan `show_main` saat URL diakses. <br /> <br />

- Tambahkan rute URL di **urls.py** proyek utama dengan `path('', include('main.urls'))` untuk menghubungkan rute URL aplikasi `main` dengan proyek secara keseluruhan, sehingga aplikasi dapat diakses melalui `http://localhost:8000/`. <br /> <br />

### 7. Deployment ke PWS
- Saya membuat proyek baru di PWS dengan nama *quirknook*. Lalu, saya juga menambahkan url dari proyek tersebut ke *settings.py* sama seperti konfigurasi untuk local host, yaitu: `ALLOWED_HOSTS = ["localhost", "127.0.0.1", "malika-atha31-quirknook.pbp.cs.ui.ac.id"]`. <br /> <br />
- Untuk setiap perubahan yang dilakukan, jika hendak mendeploy ke PWS, maka yang dilakukan untuk menge-push perubahan tersebut ke deployment adalah dengan menjalankan command berikut: `git push pws main:master`. <br /> <br />


## Bagan Request Client Django

## Fungsi git dalam pengembangan perangkat lunak!

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

## Mengapa model pada Django disebut sebagai ORM?