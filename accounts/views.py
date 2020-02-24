from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import generic
from django.contrib.auth import logout
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out!")
    return redirect("chat:index")

def login_request(request):
    form = AuthenticationForm()
    def get_success_url(self):
        return reverse_lazy('chat:index')