from django.contrib import admin
from .models import Genre, Book, Borrowed, Rating, Publisher, Author, Quantity

# Register your models here.

class DateAdmin(admin.ModelAdmin):
    model = Borrowed
    readonly_fields = ('borrowed_date','returned_date')

class RateAdmin(admin.ModelAdmin):
    model = Book
    readonly_fields = ('rating_book', 'total_qty', 'avail_qty',)

class QuantityAdmin(admin.ModelAdmin):
    model = Quantity
    readonly_fields = ('avail_qty',)






admin.site.register(Genre,)
admin.site.register(Book, RateAdmin,)
admin.site.register(Borrowed, DateAdmin,)
admin.site.register(Rating,)
admin.site.register(Publisher,)
admin.site.register(Author,)
admin.site.register(Quantity, QuantityAdmin)
