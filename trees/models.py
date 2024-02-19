from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
  name    = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  update  = models.DateTimeField(auto_now=True)
  active  = models.BooleanField(default=True)


class Profile(models.Model):
  user    = models.OneToOneField(User, on_delete=models.CASCADE)
  about   = models.TextField()
  joined  = models.DateTimeField(auto_now_add=True)


class Tree(models.Model):
  name            = models.CharField(max_length=100)
  scientific_name = models.CharField(max_length=100)


class PlantedTree(models.Model):
  user               = models.ForeignKey(User, on_delete=models.CASCADE)
  account            = models.ForeignKey(Account, on_delete=models.CASCADE,
                                         related_name='planted_trees_account')
  tree               = models.ForeignKey(Account, on_delete=models.CASCADE,
                                         related_name='planted_trees_tree')
  age                = models.IntegerField()
  planted_at         = models.DateTimeField(auto_now_add=True)
  location_latitude  = models.DecimalField(max_digits=9, decimal_places=6 )
  location_longitude = models.DecimalField(max_digits=9, decimal_places=6 )