from django.db import models
from datetime import datetime

# Default
'''
freeway
id = 0
name = 'Catalina Island'
start_coordinates='33.34281 -118.32785'
end_coordinates='33.34281 -118.32785'

traffic_condition
id = 0
description = 'unknown'
'''


class Freeway(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=False, blank=False, default='Catalina Island')
    alternate_names = models.JSONField(null=True)
    start_coordinates = models.TextField(null=False, blank=False, default='33.34281 -118.32785')
    end_coordinates = models.TextField(null=False, blank=False, default='33.34281 -118.32785')

    def __str__(self):
        return self.name


class Junction(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=False)
    coordinates = models.TextField(null=False, blank=False, default='33.34281 -118.32785')
    cardinal_bound = models.TextField(null=True, blank=False)
    fk_point_a = models.ForeignKey(Freeway, on_delete=models.CASCADE, related_name='junction_a_freeway',
                                   default=0)
    fk_point_b = models.ForeignKey(Freeway, on_delete=models.CASCADE, related_name='junction_b_freeway',
                                   default=0)

    def __str__(self):
        return self.name


class TrafficCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField(null=False, default='unknown')

    def __str__(self):
        return self.description


class Traffic(models.Model):
    id = models.IntegerField(primary_key=True)
    date_hour = models.DateTimeField(null=False, default=datetime.now)
    fk_point_a = models.ForeignKey(Freeway, on_delete=models.CASCADE, related_name='traffic_a_freeway',
                                   default=0)
    fk_point_b = models.ForeignKey(Freeway, on_delete=models.CASCADE, related_name='traffic_b_freeway',
                                   default=0)
    traffic_condition = models.ForeignKey(TrafficCondition, on_delete=models.CASCADE, related_name='traffic_condition',
                                          default=0)

    def __str__(self):
        return (f'Traffic between {self.fk_point_a.name} and {self.fk_point_a.name} on {self.date_hour} is '
                f'{self.traffic_condition.description}')
