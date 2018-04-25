from django.contrib import admin
from mysite import models

# Register your models here.
admin.site.register(models.Maker)
admin.site.register(models.PModel)
# admin.site.register(models.Product)
admin.site.register(models.PPhoto)


class ProductAdmin(admin.ModelAdmin):
	list_display = ('pmodel','nickname','price','year')
	search_fileds = ('nickname')
	ordering = ('-price',)

admin.site.register(models.Product,ProductAdmin)