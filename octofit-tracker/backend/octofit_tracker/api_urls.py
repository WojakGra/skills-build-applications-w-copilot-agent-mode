from rest_framework import routers
from octofit_tracker import api_views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'teams', api_views.TeamViewSet)
router.register(r'activities', api_views.ActivityViewSet)
router.register(r'workouts', api_views.WorkoutViewSet)
router.register(r'leaderboard', api_views.LeaderboardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]