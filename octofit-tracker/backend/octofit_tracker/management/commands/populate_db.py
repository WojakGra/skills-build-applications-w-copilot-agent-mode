from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        self.stdout.write('Creating workouts...')
        workouts = [
            Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='Medium'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='Hard'),
        ]

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=users[0], type='Pushups', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], type='Running', duration=60, date=timezone.now())
        Activity.objects.create(user=users[2], type='Pushups', duration=25, date=timezone.now())
        Activity.objects.create(user=users[3], type='Running', duration=55, date=timezone.now())

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=85)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
