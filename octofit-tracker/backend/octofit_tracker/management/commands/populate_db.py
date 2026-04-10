from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

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
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne')
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', first_name='Steve', last_name='Rogers')

        # Activities
        Activity.objects.create(user=superman, type='Flight', duration=60, team=dc)
        Activity.objects.create(user=batman, type='Martial Arts', duration=45, team=dc)
        Activity.objects.create(user=ironman, type='Tech Training', duration=50, team=marvel)
        Activity.objects.create(user=captain, type='Shield Practice', duration=40, team=marvel)

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=90)
        Leaderboard.objects.create(team=dc, points=80)

        # Workouts
        Workout.objects.create(name='Super Strength', difficulty='Hard', suggestion='Lift heavy objects')
        Workout.objects.create(name='Stealth', difficulty='Medium', suggestion='Move unseen')
        Workout.objects.create(name='Flight', difficulty='Easy', suggestion='Practice flying')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
