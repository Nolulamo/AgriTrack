from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')  # Redirect to your home page or any other page you want
        return view_func(request, *args, **kwargs)
    return wrapper