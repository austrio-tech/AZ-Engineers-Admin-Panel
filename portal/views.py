import base64
from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import Q
from .customWrappers import tryIt # type: ignore
from .models import User, Award
from .forms import UserForm, UserUpdateForm, AwardForm

def home(request):
    return render(request, 'home.html')

def manage_user(request):
    return render(request, 'users/manage_users.html')

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
    
    return render(request, 'users/add_user.html', {'form': form})

def update_user(request, user_id):
    user = tryIt(get_object_or_404, User, id=user_id)
    profile_pic =None
    if user and user.profile_pic:
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

    return render(request, 'users/update_user.html', {'form': form, 'user': user, 'profile_pic': profile_pic})

def read_user(request, user_id=None):
    if user_id is None:
        return render(request, 'users/read_user.html', {"user": None})
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        new_status = request.POST.get('new_status')
        user = tryIt(get_object_or_404, User, id=user_id)
        user.status = int(new_status)
        user.save()
        return redirect('read_user', user_id)
    
    user = tryIt(get_object_or_404, User, id=user_id)
    profile_pic = None
    
    if user and user.profile_pic:
        # Encode the binary data to base64
        profile_pic = base64.b64encode(user.profile_pic).decode('utf-8')
    
    return render(request, 'users/read_user.html', {'user': user, 'profile_pic': profile_pic})

def read_all_users(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        new_status = request.POST.get('new_status')
        user = tryIt(get_object_or_404, User, id=user_id)
        user.status = int(new_status)
        user.save()
        return redirect('read_all_users')  # Reload the same page after updating status

    users = User.objects.all()
    return render(request, 'users/read_all_users.html', {'users': users})


def manage_award(request):
    """
    This view renders the manage_awards.html template, which is the main page for managing awards.

    It does not take any parameters and does not perform any actions other than rendering the template.
    """
    return render(request, 'awards/manage_awards.html')


def add_award(request):
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            award = form.save(commit=False)  
            if 'img' in request.FILES:
                # Read the uploaded file as binary data
                award.img = request.FILES['img'].read()
            award.save() 
            return redirect('add_award')  # Redirect to a success page or another view
    else:
        form = AwardForm()
    
    return render(request, 'awards/add_award.html', {'form': form})

def update_award(request, award_id):
    award = tryIt(get_object_or_404, Award, id=award_id)
    img =None
    if award and award.img:
        # Encode the binary data to base64
        img = base64.b64encode(award.img).decode('utf-8')

    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES, instance=award)
        if form.is_valid():
            award = form.save(commit=False)  # Create the Award instance without saving to the database yet
            if 'img' in request.FILES:
                # Read the uploaded file as binary data
                award.img = request.FILES['img'].read()
            award.save() 
            return redirect('update_award')  # Replace with your actual success URL
    else:
        form = AwardForm(instance=award)

    return render(request, 'awards/update_award.html', {'form': form, 'award': award, 'img': img})

def read_award(request, award_id=None):
    if award_id is None:
        return render(request, 'awards/read_award.html', {"award": None})
    if request.method == "POST":
        award_id = request.POST.get('award_id')
        new_status = request.POST.get('new_status')
        award = tryIt(get_object_or_404, Award, id=award_id)
        award.status = int(new_status)
        award.save()
        return redirect('read_award', award_id)
    
    award = tryIt(get_object_or_404, Award, id=award_id)
    img = None
    
    if award and award.img:
        # Encode the binary data to base64
        img = base64.b64encode(award.img).decode('utf-8')
    
    return render(request, 'awards/read_award.html', {'award': award, 'img': img})

def read_all_awards(request):
    if request.method == "POST":
        award_id = request.POST.get('award_id')
        new_status = request.POST.get('new_status')
        award = tryIt(get_object_or_404, Award, id=award_id)
        award.status = int(new_status)
        award.save()
        return redirect('read_all_awards')  # Reload the same page after updating status

    awards = Award.objects.all()
    return render(request, 'awards/read_all_awards.html', {'awards': awards})



def manage_client(request):
    return render(request, 'clients/manage_clients.html')

def manage_project(request):
    return render(request, 'projects/manage_projects.html')

def manage_service(request):
    return render(request, 'services/manage_services.html')
