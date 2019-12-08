import datetime
import csv
from sightings.models import Squirrel
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    
    def handle(self, *args, **options):
        vars_name = [v.name for v in Squirrel._meta.fields]
        
        with open(options['csv_file'], 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(['Y','X','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])
            
            for s in Squirrel.objects.all():
                
                row = []
                
                for var in vars_name:
                    
                    attr = getattr(s, var)
                    
                    if var == 'date':
                        attr = datetime.datetime.strftime(attr,'%m%d%Y')
                    row.append(attr)
                
                writer.writerow(row)
