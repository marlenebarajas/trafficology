from django.contrib import admin
from .models import Freeway, Junction, TrafficCondition, Traffic

admin.site.register(Freeway)
admin.site.register(Junction)
admin.site.register(TrafficCondition)
admin.site.register(Traffic)