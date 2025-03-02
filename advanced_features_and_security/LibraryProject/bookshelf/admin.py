from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
  
admin.site.register(Book)

#Custom User Model Admin
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='photos/', null=True, blank=True )

admin.site.register(CustomUser, CustomUserAdmin)



# Register your models here.
