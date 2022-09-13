from django.contrib import admin

from basket.models import Bsket, BasketLine


class BasketLineInline(admin.TabularInline):
    model = BasketLine

class BasketAdmin(model.ModelAdmin):
    list_display = ['user', 'created_time']
    in_lines = (BasketLineInline, )

admin.site.register(Basket, BasketAdmin)