from django.db import models

# Create your models here.
class User(models.Model):
    nama = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    no_hp = models.CharField(max_length=15, null=True)
    tempat_lahir = models.CharField(max_length=20)
    tanggal_lahir = models.CharField(max_length=20)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class Pendidikan(models.Model):
    sekolah = models.CharField(max_length=30)
    tahun_mulai = models.CharField(max_length=10)
    tahun_selesai = models.CharField(max_length=10)
    jurusan = models.CharField(max_length=30, null=True)
    jenjang = models.CharField(max_length=30, null=True)
    deskripsi_pendidikan = models.TextField(null=True)

    def __str__(self):
        return self.sekolah

class Sertifikat(models.Model):
    sertifikat = models.CharField(max_length=50)
    scan = models.ImageField(upload_to='scan/')

    def __str__(self):
        return self.sertifikat

class DeskripsiDiri(models.Model):
    deskripsi_diri = models.TextField()

    def __str__(self):
        return self.deskripsi_diri

class Kategori(models.Model):
    kategori = models.CharField(max_length=30)

    def __str__(self):
        return self.kategori
    

class Pengalaman(models.Model):
    pengalaman = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    bagian = models.CharField(max_length=30)

    def __str__(self):
        return self.pengalaman

class Kemampuan(models.Model):
    kemampuan = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')
    rating = models.IntegerField()

    def __str__(self):
        return self.kemampuan
    

class Hobi(models.Model):
    hobi = models.CharField(max_length=30)

    def __str__(self):
        return self.hobi