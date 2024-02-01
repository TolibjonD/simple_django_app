from django.contrib import admin
from .models import Postlar
# Register your models here.

@admin.register(Postlar)
class PostlarAdmin(admin.ModelAdmin):
    list_display = ['sarlavha' , 'created_at']
    search_fields = ['sarlavha' , 'post_matni']