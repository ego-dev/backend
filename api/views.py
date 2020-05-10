from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions, generics
from api.serializers import (
	UserSerializer,
	GroupSerializer,
	ExerciseLogSerializer,
	DietLogSerializer,
	SymptomsLogSerializer,
	MedicationLogSerializer,
	NaturalRemediesLogSerializer,
	CardiovascularLogSerializer,
	CheckupLogSerializer,
	SleepLogSerializer,
	StressLogSerializer,
	BodyLogSerializer,
	ViceLogSerializer,
	ToiletLogSerializer,
)

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

from .permissions import IsOwner


class UsersViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAdminUser]


class CurrentUser(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_object(self):
		return self.request.user


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]


class LogViewSet(viewsets.ModelViewSet):
	model = None
	serializer_class = None
	permission_classes = [permissions.IsAdminUser | IsOwner]

	class Meta:
		abstract = True
	
	def get_queryset(self):
		return self.model.objects.filter(owner=self.request.user).order_by('-timestamp')

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class ExerciseLogViewSet(LogViewSet):
	model = ExerciseLog
	serializer_class = ExerciseLogSerializer


class DietLogViewSet(LogViewSet):
	model = DietLog
	serializer_class = DietLogSerializer


class SymptomsLogViewSet(LogViewSet):
	model = SymptomsLog
	serializer_class = SymptomsLogSerializer


class MedicationLogViewSet(LogViewSet):
	model = MedicationLog
	serializer_class = MedicationLogSerializer


class NaturalRemediesLogViewSet(LogViewSet):
	model = NaturalRemediesLog
	serializer_class = NaturalRemediesLogSerializer


class CardiovascularLogViewSet(LogViewSet):
	model = CardiovascularLog
	serializer_class = CardiovascularLogSerializer


class CheckupLogViewSet(LogViewSet):
	model = CheckupLog
	serializer_class = CheckupLogSerializer


class SleepLogViewSet(LogViewSet):
	model = SleepLog
	serializer_class = SleepLogSerializer


class StressLogViewSet(LogViewSet):
	model = StressLog
	serializer_class = StressLogSerializer


class BodyLogViewSet(LogViewSet):
	model = BodyLog
	serializer_class = BodyLogSerializer


class ViceLogViewSet(LogViewSet):
	model = ViceLog
	serializer_class = ViceLogSerializer


class ToiletLogViewSet(LogViewSet):
	model = ToiletLog
	serializer_class = ToiletLogSerializer
