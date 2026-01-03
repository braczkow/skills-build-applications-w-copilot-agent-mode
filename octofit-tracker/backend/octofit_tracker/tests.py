from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test Hero', email='test@hero.com', team='Marvel', is_superhero=True)
        self.assertEqual(user.name, 'Test Hero')
        self.assertEqual(user.team, 'Marvel')
        self.assertTrue(user.is_superhero)

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test Hero', type='Running', duration=30, date='2026-01-02')
        self.assertEqual(activity.type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Marvel', points=100, rank=1)
        self.assertEqual(lb.team, 'Marvel')
        self.assertEqual(lb.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body exercise', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
