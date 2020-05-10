from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager

# Create your models here.


class IntegerRangeField(models.IntegerField):
	def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
		self.min_value, self.max_value = min_value, max_value
		models.IntegerField.__init__(self, verbose_name, name, **kwargs)

	def formfield(self, **kwargs):
		defaults = {'min_value': self.min_value, 'max_value': self.max_value}
		defaults.update(kwargs)
		return super(IntegerRangeField, self).formfield(**defaults)


class User(AbstractUser):
	# basic user info
	username = None
	email = models.EmailField(_('email address'), unique=True)
	phone = PhoneNumberField(_('phone number'), blank=True, null=True)

	# extended user info
	cnp = models.CharField(
		_('numeric personal code'),
		max_length=13,
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
	waist = models.IntegerField(blank=True, null=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email


class Log(models.Model):
	class Meta:
		abstract = True
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	preexisting = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)


class ExerciseLog(Log):
	class Exercises(models.TextChoices):
		WALKING = 'WA', _('Walking')
		RUNNING = 'RU', _('Running')
		CYCLING = 'CY', _('Cycling')
		SWIMMING = 'SW', _('Swimming')
	
	exercise = models.CharField(
		max_length=2,
		choices=Exercises.choices,
	)
	duration = models.DurationField()


class DietLog(Log):
	product = models.CharField(max_length=128)
	code = models.CharField(max_length=13, blank=True)
	calories = models.PositiveIntegerField()


class SymptomsLog(Log):
	class Statuses(models.IntegerChoices):
		OKAY = 0, _('Okay')
		NOT_OKAY = 1, _('Not okay')
		BAD = 2, _('Very bad')
	
	status = models.IntegerField(choices=Statuses.choices, default=Statuses.OKAY)


class MedicationLog(Log):
	medication = models.CharField(max_length=128)
	dose = models.PositiveIntegerField()


class NaturalRemediesLog(Log):
	natural_remedy = models.CharField(max_length=128)


class CardiovascularLog(Log):
	pulse = models.PositiveIntegerField()
	systolic_pressure = models.PositiveIntegerField(blank=True)
	diastolic_pressure = models.PositiveIntegerField(blank=True)
	blood_sugar = models.FloatField(blank=True)
	saturation = models.DecimalField(decimal_places=2, max_digits=5)


class CheckupLog(Log):
	timestamp = models.DateTimeField(auto_now_add=False)
	details = models.TextField()


class SleepLog(Log):
	start = models.TimeField()
	end = models.TimeField()
	quality = IntegerRangeField(min_value=1, max_value=5)
	rem = models.BooleanField(blank=True)


class StressLog(Log):
	level = IntegerRangeField(min_value=1, max_value=5)
	details = models.TextField()


class BodyLog(Log):
	height = models.IntegerField(blank=True, null=True)
	weight = models.IntegerField(blank=True, null=True)
	waist = models.IntegerField(blank=True, null=True)


class ViceLog(Log):
	vice = models.CharField(max_length=128)
	quantity = models.CharField(max_length=128)


class ToiletLog(Log):
	pass
