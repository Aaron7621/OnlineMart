from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Book, BookAdmin)
