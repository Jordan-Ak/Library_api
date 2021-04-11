from django.contrib import admin
from .models import (Genre, Book, Borrowed, 
                     Rating, Publisher, Author, 
                     Quantity_Book, Quantity_Borrowed)

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    readonly_fields = ('books',)

class DateAdmin(admin.ModelAdmin):
    model = Borrowed
    readonly_fields = ('borrowed_date','returned_date')

class RateAdmin(admin.ModelAdmin):
    model = Book
    readonly_fields = ('rating_book', 'total_qty', 'avail_qty',)

class QuantityAdmin(admin.ModelAdmin):
    model = Quantity_Book
    readonly_fields = ('avail_qty',)

class PersonQuantityAdmin(admin.ModelAdmin):
    model = Quantity_Borrowed
    readonly_fields = ('books_borrowed_and_time_left','quantity_borrowed',)

admin.site.register(Genre,)
admin.site.register(Book, RateAdmin,)
admin.site.register(Borrowed, DateAdmin,)
admin.site.register(Rating,)
admin.site.register(Publisher,)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Quantity_Book, QuantityAdmin)
admin.site.register(Quantity_Borrowed, PersonQuantityAdmin)

