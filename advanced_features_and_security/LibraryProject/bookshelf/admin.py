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

#Permission for groups
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Document

# Create Groups
editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')

# Get Permissions
content_type = ContentType.objects.get_for_model(Document)
can_view_permission = Permission.objects.get(codename='can_view_document', content_type=content_type)
can_create_permission = Permission.objects.get(codename='can_create_document', content_type=content_type)
can_edit_permission = Permission.objects.get(codename='can_edit_document', content_type=content_type)
can_delete_permission = Permission.objects.get(codename='can_delete_document', content_type=content_type)

# Assign Permissions to Groups
editors_group.permissions.add(can_create_permission, can_edit_permission)
viewers_group.permissions.add(can_view_permission)
admins_group.permissions.add(can_view_permission, can_create_permission, can_edit_permission, can_delete_permission)

# Register your models here.
