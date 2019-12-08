from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    
    latitude = models.FloatField(
    #max_digits = 100,
    #decimal_places = 80,
    help_text = _('(Required) Latitude coordinate for squirrel sighting point'),
    )
    
    longitude = models.FloatField(
    #max_digits = 100,
    #decimal_places = 80,
    help_text = _('(Required) Longitude coordinate for squirrel sighting point'),
    )

    unique_squirrel_id = models.CharField(
    max_length = 50,
    help_text = _('(Required) Identification tag for each squirrel sightings. The tag is comprised of "Hectare ID" + "Shift" + "Date" + "Hectare Squirrel Number."'),
    primary_key=True,
    )
    
    # Value is either "AM" or "PM," to communicate whether or not the sighting session occurred in the morning or late afternoon.
    AM = 'AM'
    PM ='PM'
    
    SHIFT_CHOICES = (
        (AM,'AM'),
        (PM,'PM'),
    )
    
    shift = models.CharField(
    choices = SHIFT_CHOICES,
    max_length = 10,
    help_text = _('(Required) Value is either "AM" or "PM," to communicate whether or not the sighting session occurred in the morning or late afternoon.'),
    )
    
    
    date= models.DateField(
    help_text = _('(Required) Concatenation of the sighting session day and month.'),
    )
    
    # Value is either "Adult" or "Juvenile."
    Adult = 'Adult'
    Juvenile ='Juvenile'
    
    AGE_CHOICES = (
        (Adult,'Adult'),
        (Juvenile,'Juvenile'),
    )
    
    
    age= models.CharField(
    choices = AGE_CHOICES,
    max_length = 20,
    help_text = _('Value is either "Adult" or "Juvenile."'),
    null = True,
    blank = True,
    )
    
    # Value is either "Gray," "Cinnamon" or "Black."
    
    Gray = 'Gray'
    Cinnamon ='Cinnamon'
    Black = 'Black'
    
    COLOR_CHOICES = (
        (Gray,'Gray'),
        (Cinnamon,'Cinnamon'),
        (Black,'Black'),
    )
    
    primary_fur_color= models.CharField(
    choices = COLOR_CHOICES,
    max_length = 20,
    help_text = _('Value is either "Gray," "Cinnamon" or "Black."'),
    null = True,
    blank = True,
    )
    
    # Value is either "Ground Plane" or "Above Ground." Sighters were instructed to indicate the location of where the squirrel was when first sighted.
    
    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    
    LOC_CHOICES = (
        (Ground_Plane,'Ground Plane'),
        (Above_Ground,'Above Ground'),
    )
    
    location= models.CharField(
    max_length = 20,
    choices = LOC_CHOICES,
    help_text = _('Value is either "Ground Plane" or "Above Ground." Sighters were instructed to indicate the location of where the squirrel was when first sighted.'),
    null = True,
    blank = True,
    )
    
    specific_location = models.TextField(
    help_text = _('Sighters occasionally added commentary on the squirrel location. These notes are provided here.'),
    null = True,
    blank = True,
    )
    
    running= models.BooleanField(
    help_text = _('Whether the squirrel is running'),
    )
    
    chasing= models.BooleanField(
    help_text = _('Whether the squirrel is chasing'),
    )
    
    climbing= models.BooleanField(
    help_text = _('Whether the squirrel is climbing'),
    )
    
    eating= models.BooleanField(
    help_text = _('Whether the squirrel is eating'),
    )
    
    foraging= models.BooleanField(
    help_text = _('Whether the squirrel is foraging'),
    )
    
    other_activities= models.TextField(
    help_text = _('Other activities the squirrel is conducting'),
    null = True,
    blank = True,
    )
    
    kuks= models.BooleanField(
    help_text = _('Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.'),
    )
    
    quaas= models.BooleanField(
    help_text = _('Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.'),
    )
    
    moans= models.BooleanField(
    help_text = _('Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.'),
    )
    
    tail_flags= models.BooleanField(
    help_text = _("Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air."),
    )
    tail_twitches= models.BooleanField(
    help_text = _('Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.'),
    )
    
    approaches= models.BooleanField(
    help_text = _('Squirrel was seen approaching human, seeking food.'),
    )
    
    indifferent= models.BooleanField(
    help_text = _('Squirrel was indifferent to human presence.'),
    )
    
    runs_from= models.BooleanField(
    help_text = _('Squirrel was seen running from humans, seeing them as a threat.'),
    )
            
        
    def __str__(self):
        return self.unique_squirrel_id
# Create your models here.
