from django.db import models
from django.urls import reverse

# Create your models here.


class School(models.Model):
    """This model contain all info about the schools."""
    
    name = models.CharField("School Name", max_length=250)
    principal = models.CharField("School Principal", max_length=100)
    location = models.CharField("School Location ", max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('schDetails:details',kwargs={'pk':self.pk})


class Student(models.Model):
    """This model contain all info about the students."""
    
    name = models.CharField("Student Name", max_length=250)
    age = models.PositiveIntegerField('Student Age')
    School = models.ForeignKey(School, verbose_name="Student School", on_delete=models.CASCADE, related_name='students')
    profile_pic = models.ImageField(upload_to='images/schDetails/student_profile_pic', blank = True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('schDetails:listst')


# class Hotel(models.Model):
#     name = models.CharField(max_length=50)
#     hotel_Main_Img = models.ImageField(upload_to='images/student_profile_pic', blank = True)