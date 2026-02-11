from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(str(team), "Test Team")

    def test_user_create(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Jan", email="jan@example.com", team=team)
        self.assertEqual(str(user), "Jan")

    def test_activity_create(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Jan", email="jan@example.com", team=team)
        activity = Activity.objects.create(user=user, type="run", duration=30, date=timezone.now().date())
        self.assertEqual(activity.type, "run")

    def test_workout_create(self):
        workout = Workout.objects.create(name="Pushups", description="Do pushups", difficulty="easy")
        self.assertEqual(workout.name, "Pushups")

    def test_leaderboard_create(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Jan", email="jan@example.com", team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
