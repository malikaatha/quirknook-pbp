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
![alt text](image.png)

## Fungsi git dalam pengembangan perangkat lunak!
Git memungkinkan pengembang perangkat lunak untuk melacak setiap perubahan yang dilakukan pada kode sumber proyek secara detail, termasuk siapa yang membuat perubahan maupun kapan perubahan itu dilakukan. Dengan Git, pengembang dapat dengan mudah kembali ke versi sebelumnya jika terjadi kesalahan, menggabungkan perubahan dari beberapa pengembang, dan bekerja secara kolaboratif dalam tim. Selain itu, Git juga menyediakan fitur-fitur seperti _branching_, _merging_, dan _pull request_ yang sangat berguna untuk mengelola proyek yang kompleks.

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering digunakan sebagai permulaan dalam pembelajaran pengembangan perangkat lunak karena mengadopsi arsitektur Model-Template-View (MTV) yang memisahkan logika bisnis, presentasi, dan data, sehingga memudahkan pemahaman konsep dasar pengembangan web. Arsitektur ini membantu pemula memahami bagaimana komponen-komponen aplikasi berinteraksi. Selain itu, Django menyediakan banyak alat bawaan (template) yang memungkinkan pemula yang sedang belajar untuk fokus pada pembelajaran struktur dan alur kerja pengembangan tanpa harus membuat semuanya dari awal.

## Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM (Object-Relational Mapper) karena ORM merupakan fitur yang memungkinkan developer untuk berinteraksi dengan database secara intuitif menggunakan sintaks Python. Dengan ORM, user dapat memetakan struktur database ke dalam objek Python, sehingga user tidak perlu menulis query SQL secara langsung. Django akan secara otomatis menerjemahkan operasi pada objek Python ini menjadi query SQL yang sesuai. Hal ini membuat pengelolaan data menjadi lebih mudah dan efisien, sehingga Anda dapat fokus pada pengembangan fitur-fitur inti aplikasi Anda.


<br /><br />
# Tugas 3: Implementasi Form dan Data Delivery pada Django

## Data delivery dalam pengimplementasian sebuah platform?
Dalam mengimplementasikan platform, data delivery diperlukan untuk memastikan pertukaran informasi antara berbagai komponen sistem/sistem yang berbeda dapat berjalan secara efisien.Dengan menggunakan format seperti HTML, XML, atau JSON, data delivery memungkinkan data diproses dengan cara yang sesuai dengan kebutuhan spesifik aplikasi secara tampilan maupun penyimpanan data.

## Lebih baik XML atau JSON? Mengapa JSON lebih populer?
Menurut saya, JSON merupakan markup language yang lebih baik daripada XML. Alasan JSON lebih baik daripada XML dan juga merupakan format yang lebih populer adlah karena struktur data JSON yang sederhana dengan menggunakan key-value yang membuatnya lebih efisien dibandingkan XML yang menggunakan tag-tag yang lebih kompleks. Selain itu, JSON cenderung lebih efisien data karena tidak memiliki overhead tag. Karena kepopuleran ini, JSON lebih umum digunakan oleh developer sehingga developer lain juga menggunakan JSON.

##  Fungsi dari `is_valid()` pada form Django?
Method `is_valid()` pada form Django berfungsi untuk memvalidasi data yang dikirimkan. Method tersebut memastikan bahwa data tersebut memenuhi semua kriteria validasi yang telah ditetapkan dalam form. Jika semua data valid, nilai yang dikembalikan adalah `True` dan jika ada kesalahan, nilai yang dikembalikan adalah `False`. Method ini memungkinkan developer untuk menangani dan menampilkan pesan kesalahan dengan tepat. Penggunaan `is_valid()` penting untuk menjaga keamanan dan konsistensi data serta memisahkan logika validasi dari pemrosesan data lebih lanjut.

## csrf_token
csrf_token diperlukan di Django untuk melindungi aplikasi web dari serangan Cross-Site Request Forgery (CSRF). Tanpa csrf_token, aplikasi menjadi rentan terhadap serangan di mana penyerang dapat memanfaatkan kredensial user yang sudah login untuk mengirimkan permintaan berbahaya secara tidak sah. Token ini bekerja dengan memastikan bahwa setiap permintaan POST yang diterima berasal dari sumber yang sah dan bukan dari pihak ketiga yang mencoba mengeksploitasi aplikasi. Dengan menyertakan csrf_token dalam form, Django dapat memverifikasi bahwa permintaan tersebut benar-benar berasal dari aplikasi/web yang sama. Hal ini dapat mengurangi risiko tindakan tidak sah serta meningkatkan keamanan aplikasi.

## Cara pengimplementasian checklist secara step-by-step
### 1. Menambahkan Input Form untuk Menambahkan Objek Model
- Untuk memungkinkan penambahan objek model ke dalam aplikasi, saya membuat formulir input menggunakan `ModelForm`. Form ini akan memungkinkan user untuk memasukkan data untuk model MoodEntry. Buat berkas `forms.py` di aplikasi Django dan mendefinisikan form dengan atribut yang diperlukan seperti `name`, `price`, dan `description`.<br /> <br />
- Saya menambahkan fungsi view baru untuk menampilkan formulir ini dan menangani data yang di-submit. Formulir akan ditampilkan pada halaman HTML baru yang saya buat di direktori templates.<br /> <br />

### 2. Menambahkan Empat Fungsi Views untuk Melihat Objek dalam Format XML dan JSON
- Saya menambahkan dua fungsi view baru. Satu fungsi untuk mengembalikan data objek model Product dalam format JSON dan satu lagi dalam format XML. Fungsi ini akan meng-serialize data objek dan mengirimkannya dalam format yang sesuai.<br /> <br />
- Saya juga menambahkan dua fungsi view untuk menampilkan objek berdasarkan ID dalam format JSON dan XML. Fungsi ini berfungsi untuk mencari objek dengan ID tertentu dan mengembalikannya dalam format yang sesuai.<br /> <br />

### 3. Menambahkan Routing URL untuk Masing-Masing Views
- Untuk mengakses fungsi-fungsi view yang telah ditambahkan, saya membuat routing URL baru. Routing ini akan mengarahkan permintaan ke fungsi view yang sesuai berdasarkan path URL. Selain itu, berkas `urls.py` dimodifikasi dengan menambahkan URL baru untuk form input, serta URL untuk melihat data dalam format JSON dan XML baik untuk semua objek maupun berdasarkan ID.