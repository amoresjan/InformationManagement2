from django.db import models
from apps.customer import choices

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(
        max_length = 30
    )
    middle_name = models.CharField(
        max_length = 30,
        blank = True,
        null = True
    )
    last_name = models.CharField(
        max_length = 30
    )
    profile_picture = models.ImageField(
        upload_to = 'static/apps/customer/img/profile_pictures/'
    )
    
    city = models.CharField(
        max_length = 50
    )
    province = models.CharField(
        max_length = 50
    )
    zip_code = models.CharField(
        max_length = 4
    )
    country = models.CharField(
        max_length = 30
    )

    sex = models.CharField(
        max_length = 1,
        choices = choices.Sex
    )
    birth_date = models.DateField()
    status = models.CharField(
        max_length = 1,
        choices = choices.Status
    )

    spouse_name = models.CharField(
        blank = True,
        max_length = 70
    )
    spouse_occupation = models.CharField(
        blank = True,
        max_length = 30
    )
    number_of_children = models.PositiveIntegerField(
        default = 0
    )

    father_name = models.CharField(
        max_length = 70
    )
    father_occupation = models.CharField(
        max_length = 30
    )
    
    mother_name = models.CharField(
        max_length = 70
    )
    mother_occupation = models.CharField(
        max_length = 30
    )

    height = models.PositiveIntegerField(
        verbose_name = 'Height (cm)'
    )
    weight = models.PositiveIntegerField(
        verbose_name = 'Weight (kg)'
    )
    religion = models.CharField(
        max_length = 30

    )
    