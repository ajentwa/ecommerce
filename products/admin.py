from django.contrib import admin

from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('id','title','price','active','updated_at')
    list_display_links = ('id','title')
    search_fields = ('title','description')
    list_editable = ('price','active')
    list_filter = ('price','active')
    readonly_fields = ('created_at','updated_at')
    prepopulated_fields = {'slug':  ('title',)}
    list_per_page = 10


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
