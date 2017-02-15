from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator


class Customer_Assistant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='photos', null=True, blank=True,)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9}$',
                                 message="Numer telefonu powinien zawierać 9 cyfr.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    date_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def get_absolute_url(self):
        return reverse('user_details', args=[self.user.username,])

class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    customer_assistant = models.ForeignKey(Customer_Assistant)
    nip_regex = RegexValidator(regex=r'^\+?1?\d{10}$',
                                 message="NIP powinien zawierać 10 cyfr.")
    NIP = models.CharField(validators=[nip_regex], max_length=10, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9}$',
                                 message="Numer telefonu powinien zawierać 9 cyfr.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True) #można zmienić
    adress = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='photos', blank=True)
    joined = models.DateTimeField(auto_now_add=True, blank=True)
    adnotations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_details', args=[self.slug,])






