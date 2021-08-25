from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles: list[str]):
    def decorator(view_func):
        def wrapper_func(request: HttpRequest, *args, **kwargs):
            # print('Working', allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            message = '<h1>You are not authorized to view this page!</h1>'
            return HttpResponse(message)

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_func(request: HttpRequest, *args, **kwargs):
        # print('Working', allowed_roles)
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user_page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
