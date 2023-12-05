from django.contrib import admin

from contact import models


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_at', 'update_at', 'description', 'show',)
    ordering = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_at', 'update_at', 'description', 'show',)
    # list_filter = ('create_date', 'created_at', 'update_at', 'show')
    search_fields = ('id', 'first_name', 'phone',)
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ('last_name', 'email', 'show',)
    list_display_links = ('first_name', 'phone',)
