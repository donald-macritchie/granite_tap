from django.contrib import admin
from .models import About, FAQ

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

admin.site.register(About, AboutAdmin)
admin.site.register(FAQ, FAQAdmin)
