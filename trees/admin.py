from django.contrib import admin
from django.utils.text import slugify
from .models import Account, Profile, Tree, PlantedTree


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created')
    list_filter = ('active', 'created')
    actions = ['activate_acc', 'deactivate_acc']

    def activate_acc(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, 'As contas selecionadas foram ativadas com sucesso.')

    activate_acc.short_description = 'Ativar contas selecionadas'

    def deactivate_acc(self, request, queryset):
        queryset.update(active=False)
        self.message_user(request, 'As contas selecionadas foram desativadas com sucesso.')

    deactivate_acc.short_description = 'Desativar contas selecionadas'


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
                  'location_longitude', 'slug', 'status')
  list_filter  = ('user','planted_at')
  prepopulated_fields = {'slug':('title',)}