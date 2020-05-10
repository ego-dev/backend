from django.contrib.auth.models import Group
from rest_framework import serializers

from common.models import (
	User,
	Log,
	ExerciseLog,
	DietLog,
	SymptomsLog,
	MedicationLog,
	NaturalRemediesLog,
	CardiovascularLog,
	CheckupLog,
	SleepLog,
	StressLog,
	BodyLog,
	ViceLog,
	ToiletLog,
)


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'email', 'first_name', 'last_name', 'phone', 'cnp', 'address', 'birth_date', 'birth_place', 'blood_type', 'rhesus_factor', 'height', 'weight', 'waist']


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']


class ExerciseLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExerciseLog
		fields = ['id', 'preexisting', 'timestamp', 'exercise', 'duration']


class DietLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = DietLog
		fields = ['id', 'preexisting', 'timestamp', 'product', 'code', 'calories']


class SymptomsLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = SymptomsLog
		fields = ['id', 'preexisting', 'timestamp', 'status']


class MedicationLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = MedicationLog
		fields = ['id', 'preexisting', 'timestamp', 'medication', 'dose']


class NaturalRemediesLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = NaturalRemediesLog
		fields = ['id', 'preexisting', 'timestamp', 'natural_remedy']


class CardiovascularLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = CardiovascularLog
		fields = ['id', 'preexisting', 'timestamp', 'pulse', 'systolic_pressure', 'diastolic_pressure', 'blood_sugar', 'saturation']


class CheckupLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = CheckupLog
		fields = ['id', 'preexisting', 'timestamp', 'details']


class SleepLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = SleepLog
		fields = ['id', 'preexisting', 'timestamp', 'start', 'end', 'quality', 'rem']


class StressLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = StressLog
		fields = ['id', 'preexisting', 'timestamp', 'level', 'details']


class BodyLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = BodyLog
		fields = ['id', 'preexisting', 'timestamp', 'height', 'weight', 'waist']


class ViceLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = ViceLog
		fields = ['id', 'preexisting', 'timestamp', 'vice', 'quantity']


class ToiletLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToiletLog
		fields = ['id', 'preexisting', 'timestamp']
