from django.db import models


class Gender(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class RichMans(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    money = models.PositiveBigIntegerField()
    country = models.CharField(max_length=80)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
