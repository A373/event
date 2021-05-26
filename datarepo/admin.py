from django.contrib import admin
from .models import CustomUser, Event, EventBooking
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'email', 'username', 'phone', 'created']
    search_fields = ['username', 'phone']
    list_filter = ['username']


UserAdmin.fieldsets += (
    (
        'Custom fields', {
            'fields': ('phone', 'created')
        }
    ),
)


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'place']
    search_fields = ['name', 'place']
    list_filter = ['name', 'place']



class EventBookingAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'event_name', 'event_time', 'amount', 'booking_time']
    search_fields = ['user_name', 'event_name', 'amount']
    list_filter = ['user_name', 'event_name', 'amount']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventBooking, EventBookingAdmin)