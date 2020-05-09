from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
	# basic user info
	username = None
	email = models.EmailField(_('email address'), unique=True)
	phone = PhoneNumberField(_('phone number'), null=True)

	# extended user info
	cnp = models.CharField(
		_('numeric personal code'),
		max_length=13,
		unique=True,
		blank=True)
	address = models.TextField(blank=True)
	birth_date = models.DateField(_('date of birth'), null=True, blank=True)
	birth_place = models.TextField(blank=True)

	# medical info
	class BloodTypes(models.TextChoices):
		TYPE_O = 'O', _('O(I)')
		TYPE_A = 'A', _('A(II)')
		TYPE_B = 'B', _('B(III)')
		TYPE_AB = 'AB', _('AB(IV)')
	
	class RhesusFactors(models.TextChoices):
		POSITIVE = '+', _('Positive')
		NEGATIVE = '-', _('Negative')
	
	blood_type = models.CharField(
		max_length=2,
		choices=BloodTypes.choices,
		blank=True,
	)
	rhesus_factor = models.CharField(
		max_length=1,
		choices=RhesusFactors.choices,
		blank=True,
	)
	height = models.IntegerField(blank=True, null=True)
	weight = models.IntegerField(blank=True, null=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['phone']

	objects = CustomUserManager()

	def __str__(self):
		return self.email
