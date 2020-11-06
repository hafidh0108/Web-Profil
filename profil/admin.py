from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Pendidikan)
admin.site.register(Sertifikat)
admin.site.register(Pengalaman)
admin.site.register(DeskripsiDiri)
admin.site.register(Hobi)
admin.site.register(Kategori)
admin.site.register(Kemampuan)