from django.db import models


STATE_CHOICE = (
    ('Chittagong','ctg'),
    ("Dhaka","dhaka"),
    ("Rajshahi","rajshahi"),
    ("cox'sbazar","cox'sbazar"),
)
# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=300)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField()
    state = models.CharField(max_length=50,choices=STATE_CHOICE)
    mobiles = models.PositiveIntegerField()
    email = models.EmailField( max_length=254)
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg',blank=True)
    myfile = models.FileField(upload_to='doc',blank=True)