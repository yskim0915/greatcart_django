from django.contrib import admin
from category.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name', )}
    list_display = ['category_name', 'slug', 'parent']
    list_filter = ['parent']

admin.site.register(Category, CategoryAdmin)