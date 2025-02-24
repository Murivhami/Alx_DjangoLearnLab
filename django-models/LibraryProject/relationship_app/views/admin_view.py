from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

@user_passes_test(is_admin, login_url='/403/')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
