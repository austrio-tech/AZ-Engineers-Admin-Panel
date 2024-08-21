from django import forms
from .models import User, Award, Client, ProjectCategory, Project, Gallery, ProjectGallery

# User Forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role']  # Exclude 'password'

# Award Form
class AwardForm(forms.ModelForm):
    img = forms.FileField(required=False)  # Override to handle file uploads

    class Meta:
        model = Award
        fields = ['title', 'img', 'awarded_on', 'status']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['img']:
            instance.img = self.cleaned_data['img'].read()
        if commit:
            instance.save()
        return instance

# Client Form
class ClientForm(forms.ModelForm):
    logo_img = forms.FileField(required=False)  # Override to handle file uploads

    class Meta:
        model = Client
        fields = ['name', 'logo_img', 'description', 'status']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['logo_img']:
            instance.logo_img = self.cleaned_data['logo_img'].read()
        if commit:
            instance.save()
        return instance

# ProjectCategory Form
class ProjectCategoryForm(forms.ModelForm):
    class Meta:
        model = ProjectCategory
        fields = ['title', 'description', 'status']

# Project Form
class ProjectForm(forms.ModelForm):
    prime_img = forms.FileField(required=False)  # Override to handle file uploads

    class Meta:
        model = Project
        fields = [
            'title', 'description', 'category', 'client', 'contractor', 
            'value', 'start_date', 'end_date', 'prime_img', 'status'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['prime_img']:
            instance.prime_img = self.cleaned_data['prime_img'].read()
        if commit:
            instance.save()
        return instance

# Gallery Form
class GalleryForm(forms.ModelForm):
    img = forms.FileField(required=False)  # Override to handle file uploads

    class Meta:
        model = Gallery
        fields = ['title', 'img', 'status']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['img']:
            instance.img = self.cleaned_data['img'].read()
        if commit:
            instance.save()
        return instance

# ProjectGallery Form
class ProjectGalleryForm(forms.ModelForm):
    class Meta:
        model = ProjectGallery
        fields = ['project', 'gallery', 'status']
