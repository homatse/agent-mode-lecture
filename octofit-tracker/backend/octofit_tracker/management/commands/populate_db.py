from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    suggestion = models.CharField(max_length=200)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', first_name='Steve', last_name='Rogers'),
        ]

        # Activities
        Activity.objects.create(user='superman', type='Flight', duration=60, team='DC')
        Activity.objects.create(user='batman', type='Martial Arts', duration=45, team='DC')
        Activity.objects.create(user='ironman', type='Tech Training', duration=50, team='Marvel')
        Activity.objects.create(user='captain', type='Shield Practice', duration=40, team='Marvel')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=90)
        Leaderboard.objects.create(team='DC', points=80)

        # Workouts
        Workout.objects.create(name='Super Strength', difficulty='Hard', suggestion='Lift heavy objects')
        Workout.objects.create(name='Stealth', difficulty='Medium', suggestion='Move unseen')
        Workout.objects.create(name='Flight', difficulty='Easy', suggestion='Practice flying')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
