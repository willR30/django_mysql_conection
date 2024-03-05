from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'person'  # Specify the custom table name

    def __str__(self):
        return self.name