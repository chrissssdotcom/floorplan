from django.db import models

class Building(models.Model):
    site_display_name = models.CharField(max_length=100)
    site_address = models.TextField()
    site_prefix = models.CharField(max_length=10)
    site_state = models.CharField(max_length=50)

    def __str__(self):
        return self.site_display_name

class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors')
    floor_number = models.IntegerField()
    floor_description = models.TextField()
    floor_image = models.ImageField(upload_to='floor_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.building.site_display_name} - Floor {self.floor_number}"

class Location(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='locations')
    location_name = models.CharField(max_length=100)
    location_description = models.TextField(blank=True, null=True)
    location_url = models.URLField(blank=True, null=True)
    x_coordinate = models.FloatField(default=0)
    y_coordinate = models.FloatField(default=0)

    def __str__(self):
        return f"{self.floor.building.site_prefix}_{self.floor.floor_number}_{self.location_name}"
      
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, related_name='people', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"