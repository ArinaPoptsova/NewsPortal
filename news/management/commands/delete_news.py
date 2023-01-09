from django.core.management.base import BaseCommand, CommandError
from news.models import Post

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Do you want to delete all news? (y/n) ')
        answer = input()

        if answer.lower() == 'y':
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All news have deleted successfully'))
            return

        self.stdout.write(self.style.ERROR('Access denied'))
