from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResposnseForbidden

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

@user_passes_test(is_admin, login_url='/403/')
def admin_view(request):
    if request.user.role = 'admin':
        return render(request, 'admin_view.html')
    return HttpResponseForbidden("Denied Access")
