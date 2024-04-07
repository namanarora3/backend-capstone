from django.db import models
CATEGORY_CHOICES = (
  ("GAMING","gaming"),
  ("FURNITURE","furniture"),
  ("EDUCATION","educaiton"),
  ("DAILY NEEDS","daily needs"),
  ("FASHION","fashion"),
)
CONDITION_CHOICES = (
  ("new","new"),
  ("good","as good as new"),
  ("average","slightly used"),
  ("poor","extremely used")
)
# Create your models here.
class Product(models.Model):
  Name = models.TextField()
  Description = models.TextField()
  Category = models.TextField(choices=CATEGORY_CHOICES)
  Condition = models.TextField(choices=CONDITION_CHOICES)
  Price = models.DecimalField(max_digits=7, decimal_places=2)

