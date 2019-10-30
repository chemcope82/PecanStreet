from django.contrib import admin
from .models import Artist, TattooImage

# Register your models here.
admin.site.register(Artist)
admin.site.register(TattooImage)