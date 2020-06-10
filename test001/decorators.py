from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
               return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<h1 style ="align-text: center"> You are Not Authorized to view this Page</h1>')
        return wrapper_func
    return decorator

def admin_only(view_func):
    
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Students':
            return redirect('user-page')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
