from django.contrib import admin
from .models import Tasks,Profile
# Register your models here.
admin.site.register(Tasks)

@admin.register(Profile)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_username')  # Show 'id' in list view
    readonly_fields = ('id',)  # Make 'id' visible (and read-only) in detail view
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'