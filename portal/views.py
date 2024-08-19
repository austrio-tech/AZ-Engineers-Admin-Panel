import base64
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import User
from .forms import UserForm, UserUpdateForm

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
            return redirect('add_user')  # Redirect to a success page or another view
    else:
        form = UserForm()
    
    return render(request, 'add_user.html', {'form': form})


# def update_user(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('manage_users')
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'update_user.html', {'form': form})


def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile_pic =None
    if user.profile_pic:
        # Encode the binary data to base64
        profile_pic = base64.b64encode(user.profile_pic).decode('utf-8')

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)  # Create the User instance without saving to the database yet
            if 'profile_pic' in request.FILES:
                # Read the uploaded file as binary data
                user.profile_pic = request.FILES['profile_pic'].read()
            user.save() 
            return redirect('update_user')  # Replace with your actual success URL
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'update_user.html', {'form': form, 'user': user, 'profile_pic': profile_pic})



def read_user(request, user_id):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        new_status = request.POST.get('new_status')
        user = get_object_or_404(User, id=user_id)
        user.status = int(new_status)
        user.save()
        return redirect('read_user', user_id)
    
    user = get_object_or_404(User, id=user_id)
    profile_pic = None
    
    if user.profile_pic:
        # Encode the binary data to base64
        profile_pic = base64.b64encode(user.profile_pic).decode('utf-8')
    
    return render(request, 'read_user.html', {'user': user, 'profile_pic': profile_pic})

def read_all_users(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        new_status = request.POST.get('new_status')
        user = get_object_or_404(User, id=user_id)
        user.status = int(new_status)
        user.save()
        return redirect('read_all_users')  # Reload the same page after updating status

    users = User.objects.all()
    return render(request, 'read_all_users.html', {'users': users})


def search_user(request):
    search_query = request.GET.get('search_query', None)
    user = None

    if search_query:
        try:
            # Try to search by ID first
            user = User.objects.get(id=int(search_query))
        except (ValueError, User.DoesNotExist):
            # If not found by ID, search by name (first name or last name)
            user = User.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)).first()

    return render(request, 'search_user.html', {'user': user, 'search_query': search_query})