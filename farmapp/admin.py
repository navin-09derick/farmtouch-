from django.contrib import admin

# Register your models here.
from farmapp.models import Product1,Sellproduct
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('title','price','image','description','page')
#ProductAdmin class
admin.site.register(Product1,ProductAdmin)

#admin.site.register(UserProfile)
admin.site.register(Sellproduct)
admin.site.site_header="Farm Touch"
admin.site.site_title="Farm Touch"
admin.site.index_title="Welcome To Farm Touch"
