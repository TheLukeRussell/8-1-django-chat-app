from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .models import Profile
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:profile')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out!")
    return redirect("chat:index")

def login_request(request):
    form = AuthenticationForm()
    def get_success_url(self):
        return reverse_lazy('chat:index')

class ProfileView(generic.CreateView):
    model = Profile
    success_url = reverse_lazy('chat:index')
    fields = ('country', 'avatar',)
    template_name = 'profile_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'profile_detail.html'