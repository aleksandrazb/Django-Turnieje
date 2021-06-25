from django.shortcuts import render


def login(request):
    print(request.user)
    data = {
        'name': request.user,
        'title': 'Login'
    }
    return render(request, 'login.html', data)
