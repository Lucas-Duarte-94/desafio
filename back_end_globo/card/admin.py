from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Card, Tag

class CardAdmin(admin.ModelAdmin):
    list_display = ('texto', 'data_criacao', 'data_modificacao', 'tags')

class TagAdmin(admin.ModelAdmin):
    display = 'name'

# Register your models here.

admin.site.register(Card, CardAdmin)
admin.site.register(Tag, TagAdmin)