from django.core.management.base import BaseCommand
import csv
import datetime
from sightings.models import Squirrel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    
    
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        
        def clean_data(data):
            if (data == 'true') or (data=='True') or (data=='TRUE'):
                return True
            elif (data == 'false') or (data=='False') or (data=='FALSE'):    
                return False
            else:
                return data   
        
        for item in data:
            s = Squirrel(
                    latitude = item['Y'],
                    longitude = item['X'],
                    unique_squirrel_id = item['Unique Squirrel ID'],
                    shift = item['Shift'],
                    date = datetime.datetime.strptime(item['Date'],'%m%d%Y'),
                    age = item['Age'],
                    primary_fur_color = item['Primary Fur Color'],
                    location = item['Location'],
                    specific_location = item['Specific Location'],
                    running = clean_data(item['Running']),
                    chasing = clean_data(item['Chasing']),
                    climbing = clean_data(item['Climbing']),
                    eating = clean_data(item['Eating']),
                    foraging = clean_data(item['Foraging']),
                    other_activities = item['Other Activities'],
                    kuks = clean_data(item['Kuks']),
                    quaas = clean_data(item['Quaas']),
                    moans = clean_data(item['Moans']),
                    tail_flags = clean_data(item['Tail flags']),
                    tail_twitches = clean_data(item['Tail twitches']),
                    approaches = clean_data(item['Approaches']),
                    indifferent = clean_data(item['Indifferent']),
                    runs_from = clean_data (item['Runs from']),
                    )

            s.save()
