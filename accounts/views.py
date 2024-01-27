from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_user(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['email']
            user =  form.save(commit=False)
            user.set_password(password)
            user.username = username
            user.is_active = True
            user.save()
            # messages.success(request,"Registration successful")
            return redirect('login')
        # else:
        #     print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registeruser.html',context)


# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         print(f"Attempting login with email: {email}, password: {password}")
#         user=User.objects.all()
#         print(user)
#         try:
#             user = User.objects.get(email=email)
#             print("dbuser")
#         except User.DoesNotExist:
#             user = None

#         print(f"User found: {user}")

#         if user:
#             print(f"User password in database: {user.password}")

#             authenticated_user = authenticate(request, email=email, password=password)

#             print(f"Authenticated user: {authenticated_user}")

#             if authenticated_user is not None:
#                 login(request, authenticated_user)
#                 print('Login successful')
#                 # return redirect('dashboard')
#                 messages.success(request, "Successfully Logged In")
#             else:
#                 messages.error(request, "Invalid email or password")
#         else:
#             messages.error(request, "User does not exist")

#     return redirect('dashboard')
  


@login_required(login_url='login_user')
def dashboard(request):
   
    user = User.objects.get(email=request.user.email)
    # print(user.email,user.username)
    # print(user.role,"ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    role =user.get_role_display()
    context = {
        'user': request.user.first_name,  # Pass the user object to the template context
        'role': role,
    }
    print(role)
    if role == 'Student':
        return render(request, 'accounts/student.html',context)
    elif role == 'Staff':
        return render(request, 'accounts/staff.html',context)
    elif role == 'Admin':
        return render(request, 'accounts/admin.html',context)
    elif role == 'Editor':
        return render(request, 'accounts/editor.html',context)



def check(request):
    print("Checking")
    return render(request, 'accounts/login_form.html')


def login_user(request):
    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']
        # print(email, password,"ASJHSJKHSKJSH")
        # dbuser = User.objects.get(email=email)
        # print(dbuser,"AASJHSJKSJKHSKJSH")
        # print(dbuser.password,"DBUSER EMAIL")
        user = auth.authenticate(email=email, password=password)
        # print(user)
        if user is not None:
            auth.login(request,user)
            print ('login successful')
            return redirect('dashboard')
            # messages.success(request,"Successfully Logged In")
        else:
            messages.error(request,"Invalid username or password")
    return redirect('login')

def logout_user(request):
    logout(request)
    return redirect('login')