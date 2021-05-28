from django.contrib import admin
from .models import CustomUser, EventName, EventPlace, EventBooking
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


class EventPlaceAdmin(admin.ModelAdmin):
    list_display = ['place']
    search_fields = ['place']
    list_filter = ['place']


class EventNameAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class EventBookingAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'event_name', 'event_place', 'event_time', 'amount', 'booking_time']
    search_fields = ['user_name', 'event_name', 'event_place', 'amount']
    list_filter = ['user_name', 'event_name', 'amount']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EventPlace, EventPlaceAdmin)
admin.site.register(EventName, EventNameAdmin)
admin.site.register(EventBooking, EventBookingAdmin)