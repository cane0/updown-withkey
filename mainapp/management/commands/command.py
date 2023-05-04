from random import randint
from time import sleep
from datetime import datetime
from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management import call_command
from django.core.management.base import BaseCommand
from mainapp.models import *

class Command(BaseCommand):
    help = 'Generate a random number every four minutes and store it in a SQLite database.'
    
    def handle(self, *args, **options):
        call_command('runserver', '127.0.0.1:8000')
        
        while True:
            if EncKey.objects.exists() == True:
                current_key = EncKey.objects.last()
                EncKey.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted random number: {current_key}'))
            now = datetime.now().time()
            my_key = randint(100000, 999999)  # Generate a random number between 1 and 100
            my_key = str(my_key)
            EncKey.objects.create(my_key=my_key)
            self.stdout.write(self.style.SUCCESS(f'Successfully generated and saved random number: {my_key} at {now}\n'))
            sleep(240)  # Sleep for four minutes
