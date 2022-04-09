from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    # Have to use reverse_lazy() instead of reverse(), as the urls are not loaded when the file is imported.
    # Provides a reversed URL as the url attribute of a generic class-based view
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
