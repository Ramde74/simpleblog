from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','description','url')
    search_fields = ('title',)

admin.site.register(Category,CategoryAdmin)