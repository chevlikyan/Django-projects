from django.contrib import admin
from testapplication.models import *


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'status', 'phone_number', 'age')
    list_display_links = ('id', 'name', 'surname')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'surname')
    list_editable = ('status',)
    list_per_page = 2


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'available')
    list_display_links = ('title', 'author', 'publisher')
    list_filter = ('available', 'title')
    search_fields = ('title', 'author')
    list_editable = ('available',)
    list_per_page = 3


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_after', 'school_number', 'address')
    list_display_links = ('school_after', 'school_number', 'address')
    list_filter = ('school_number',)
    search_fields = ('school_after', 'school_number')
    list_per_page = 2


@admin.register(TheClass)
class TheClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'stream')
    list_display_links = ('id', 'year', 'stream')
    list_filter = ('stream',)
    search_fields = ('year', 'stream')
    list_per_page = 2
    save_on_top = True


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'model', 'VIN_code', 'sales')
    list_display_links = ('id', 'mark', 'model')
    list_filter = ('mark', 'model', 'year')
    search_fields = ('mark',)
    list_per_page = 2
    save_on_top = True
    ordering = ('-created_at',)
    list_editable = ('sales',)
