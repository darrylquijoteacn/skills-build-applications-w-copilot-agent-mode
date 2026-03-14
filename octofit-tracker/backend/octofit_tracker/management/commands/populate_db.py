from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='walk', duration=60, distance=4)
        Activity.objects.create(user=bruce, type='strength', duration=45, distance=0)
        Activity.objects.create(user=clark, type='run', duration=25, distance=6)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio session for all')
        Workout.objects.create(name='Strength Training', description='Strength session for all')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
