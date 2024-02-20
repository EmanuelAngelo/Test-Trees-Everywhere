from rest_framework import serializers
from .models import PlantedTree


class PlantedTreeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlantedTree
    fields = ['id', 'title', 'age', 'publish', 'planted_at', 'location_latitude', 'location_longitude', 'status', 'body']
