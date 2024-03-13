from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required

# from .forms import LoginForm
# from .models import AdminUser, TeacherUser, StudentUser

# @login_required
# def dashboard(request):
#     # Your dashboard view logic here
#     return render(request, 'dashboard.html')

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password_or_otp = form.cleaned_data['password_or_otp']

#             user = authenticate(request, username=username, password=password_or_otp)

#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')
#             else:
#                 # Authentication failed, handle accordingly
#                 pass
#     else:
#         form = LoginForm()

#     return render(request, 'login.html', {'form': form})