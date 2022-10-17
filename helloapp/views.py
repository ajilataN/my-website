# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

from.forms import UserForm

def Register_view(request):
    # if this is a POST request we need to process the form data
    if request.method =='POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        # process the d ata in form. cleane d_data as re quired
        # ...
        # redirect to a new URL:
        return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
form = UserForm()

return render(request, 'registration.html', {'form': form})
