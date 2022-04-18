from django.contrib import admin

from phones.models import Phone


@admin.register(Phone)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'release_data', 'lte_exist', 'slug']
    prepopulated_fields = {"slug": ("name",)}
