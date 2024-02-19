from django.contrib import admin
from .models import Account, Profile, Tree, PlantedTree


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
  list_display = ('name','active','created')
  list_filter  = ('active','created')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ('user','joined')
  list_filter  = ('joined',)


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
  list_filter = ('name', 'scientific_name')
  list_filter = ('name',)


@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
  list_display = ('user','account','age','tree','location_latitude',
                  'location_longitude',)
  list_filter  = ('user','planted_at')