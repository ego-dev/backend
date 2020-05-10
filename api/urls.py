from django.urls import include, path
from rest_framework import routers

from api.views import (
	UsersViewSet,
	CurrentUser,
	GroupViewSet,
	ExerciseLogViewSet,
	DietLogViewSet,
	SymptomsLogViewSet,
	MedicationLogViewSet,
	NaturalRemediesLogViewSet,
	CardiovascularLogViewSet,
	CheckupLogViewSet,
	SleepLogViewSet,
	StressLogViewSet,
	BodyLogViewSet,
	ViceLogViewSet,
	ToiletLogViewSet,
)


router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'log/exercise', ExerciseLogViewSet, basename='ExerciseLog')
router.register(r'log/diet', DietLogViewSet, basename='DietLog')
router.register(r'log/symptoms', SymptomsLogViewSet, basename='SymptomsLog')
router.register(r'log/medication', MedicationLogViewSet, basename='MedicationLog')
router.register(r'log/naturalremedies', NaturalRemediesLogViewSet, basename='NaturalRemediesLog')
router.register(r'log/cardiovascular', CardiovascularLogViewSet, basename='CardiovascularLog')
router.register(r'log/checkup', CheckupLogViewSet, basename='CheckupLog')
router.register(r'log/sleep', SleepLogViewSet, basename='SleepLog')
router.register(r'log/stress', StressLogViewSet, basename='StressLog')
router.register(r'log/body', BodyLogViewSet, basename='BodyLog')
router.register(r'log/vice', ViceLogViewSet, basename='ViceLog')
router.register(r'log/toilet', ToiletLogViewSet, basename='ToiletLog')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	path('', include(router.urls)),
	path('user', CurrentUser.as_view()),
	path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
