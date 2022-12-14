from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


     

class List(models.Model):
        list_owner = models.CharField(max_length=30)
        list_items = ArrayField(
            ArrayField(
                models.CharField(max_length=20, blank=True),
                size=20,
            ),
            size=20
        )

lists = [
    List("Ben Baker",['apple','orange','chicken thighs','yogurt']),
    List("Brenna Langille", ['pickles','green cola','sausages','peppers'],
    List("Devin Larsen",['tempeh','grains','ointment','toothpaste']))
]