from django.contrib import admin
from .models import About, FAQ, ContactInfo

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'message'
    )

admin.site.register(About, AboutAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)