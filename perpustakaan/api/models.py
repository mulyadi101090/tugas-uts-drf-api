from django.db import models

class Penulis(models.Model):
    nama = models.CharField(max_length=100)
    biografi = models.TextField(blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.ManyToManyField(Penulis, related_nama='books')
    keterangan = models.TextField(blank=True)
    tanggal_dipublis = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul

class Pinjaman(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    pinjaman = models.ManyToManyField(Buku, through='PinjamanBuku')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

class PinjamanBuku(models.Model):
    pinjaman = models.ForeignKey(Pinjaman, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.borrower} - {self.buku}"
