from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-joined',)

    def __str__(self):
        return f"{self.user.first_name}"

class Tree(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('-scientific_name',)

    def __str__(self):
        return self.name

class PlantedTree(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='planted_trees_account')
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='planted_trees_tree')
    title = models.CharField(max_length=250)
    age = models.IntegerField()
    publish = models.DateTimeField(default=timezone.now)
    planted_at = models.DateTimeField(auto_now_add=True)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    slug = models.SlugField(max_length=250, unique_for_date='planted_at')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager
    body = models.TextField()

    class Meta:
        ordering = ('-planted_at',)

    def __str__(self):
        return f"Planted Tree #{self.id}"

    def get_absolute_url(self):
        return reverse('trees:planted_tree_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def clean(self):
        self.title = self.tree.name

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def plant_tree(self, tree, latitude, longitude):
        PlantedTree.objects.create(
            user=self.user,
            account=self.user.profile.account,
            tree=tree,
            age=1,
            publish=timezone.now(),
            planted_at=timezone.now(),
            location_latitude=latitude,
            location_longitude=longitude,
            slug=f"{tree.name}-{timezone.now().strftime('%Y-%m-%d-%H-%M-%S')}",
            status='published'
        )

    def plant_trees(self, tree_coordinates):
        for tree, latitude, longitude in tree_coordinates:
            self.plant_tree(tree, latitude, longitude)
