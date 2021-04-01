from django.contrib import admin
from .models import Genre, Book, Borrowed

# Register your models here.

class DateAdmin(admin.ModelAdmin):
    model = Borrowed
    readonly_fields = ('borrowed_date','returned_date')



admin.site.register(Genre,)
admin.site.register(Book, )
admin.site.register(Borrowed, DateAdmin)