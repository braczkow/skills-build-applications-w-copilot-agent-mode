from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Batman', email='batman@dc.com', team='DC', is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Spider-Man', type='Running', duration=30, date='2026-01-01'),
            Activity(user='Iron Man', type='Cycling', duration=45, date='2026-01-01'),
            Activity(user='Batman', type='Swimming', duration=25, date='2026-01-01'),
            Activity(user='Wonder Woman', type='Yoga', duration=60, date='2026-01-01'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=175, rank=1)
        Leaderboard.objects.create(team='DC', points=85, rank=2)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body exercise', difficulty='Easy'),
            Workout(name='Squats', description='Lower body exercise', difficulty='Medium'),
            Workout(name='Plank', description='Core strength exercise', difficulty='Hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
