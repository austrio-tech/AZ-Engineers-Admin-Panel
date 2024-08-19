import base64
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

def home(request):
    return render(request, 'home.html')

def manage_users(request):
    return render(request, 'manage_users.html')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  # Create the User instance without saving to the database yet
            if 'profile_pic' in request.FILES:
                # Read the uploaded file as binary data
                user.profile_pic = request.FILES['profile_pic'].read()
            user.save()  # Save the User instance with the profile_pic
            return redirect('success_url')  # Redirect to a success page or another view
    else:
        form = UserForm()
    
    return render(request, 'add_user.html', {'form': form})


def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

def read_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile_pic = None
    
    if user.profile_pic:
        # Encode the binary data to base64
        profile_pic = base64.b64encode(user.profile_pic).decode('utf-8')
    
    return render(request, 'read_user.html', {'user': user, 'profile_pic': profile_pic})

def read_all_users(request):
    users = User.objects.all()
    return render(request, 'read_all_users.html', {'users': users})

