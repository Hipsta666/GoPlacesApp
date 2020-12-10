from django.contrib import admin
from django.utils.safestring import mark_safe

from goplaces.models import *

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating', 'average_check', 'get_image', 'tag_list', 'id')
    prepopulated_fields = {'url': ('name', 'address')}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="70" height="50">')
    get_image.short_description = 'Постер'
    readonly_fields = ('get_image',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = ('answer_text', 'tag_list')


admin.site.register([Tag, Question])

