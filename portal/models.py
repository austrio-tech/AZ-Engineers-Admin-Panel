from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('User', 'User')])
    profile_pic = models.BinaryField(null=True, blank=True) 
    last_edit = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
    def __repr__(self):
        return self.__str__()

class Award(models.Model):
    title = models.CharField(max_length=40)
    img = models.BinaryField(null=True, blank=True, editable=True)
    awarded_on = models.IntegerField()  # Assuming you only need the year, otherwise use DateField()
    last_edit = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()
    

class Client(models.Model):
    name = models.CharField(max_length=40)
    logo_img = models.BinaryField(null=True, blank=True, editable=True)
    description = models.TextField(null=True, blank=True)
    last_edit = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
    

class ProjectCategory(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    last_edit = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    contractor = models.CharField(max_length=40)
    value = models.FloatField()  # Assuming value is in OMR as you mentioned
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    prime_img = models.BinaryField(null=True, blank=True, editable=True)
    last_edit = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    img = models.BinaryField(null=True, blank=True, editable=True)
    last_edit = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class ProjectGallery(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)
    last_edit = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Project: {self.project.title} - Gallery: {self.gallery.title}"

    def __repr__(self):
        return self.__str__()

