from django.shortcuts import render, redirect
from ..forms import RejestracjaForm


def register_user(request):
    print(request.user)
    form = RejestracjaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    data = {
        'form': form,
        'name': request.user,
        'title': 'Rejestracja'
    }
    return render(request, 'rejestracja.html', data)
