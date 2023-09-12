from rest_framework import serializers
from .models import *

class FootballSerializer(serializers.Serializer):
    team = models.CharField(max_length=150)
    player = models.CharField(max_length=150)
    jersey_no = models.IntegerField()
    
    def update(self,instance,validated_data):
        print(instance.name)
        instance.team = validated_data.get('team' , instance.team)
        print(instance.name)
        instance.player = validated_data.get('player' , instance.player)
        instance.jersey_no = validated_data.get('jersey_no' , instance.jersey_no)
        instance.save()
        return instance