from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.CharField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True)


# from django.db import models
#
#
# class Phone(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField()
#     release_date = models.DateField()
#     lte_exist = models.BooleanField()
#     slug = models.SlugField(max_length=225, unique=True, db_index=True)
#
#     def __str__(self):
#         return self.name
