from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, post_delete, pre_delete, post_init, pre_init, pre_save
from django.dispatch import receiver

# Create your models here.


class Symbol(models.Model):
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.image


class Country(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField(null=True)
    population = models.IntegerField(default=0)
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE)
    cities_count = models.IntegerField(default=0)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=City)
def city_save_signal(sender, **kwargs):
    print(f"Город {kwargs['instance']} добавлен")


@receiver(post_save, sender=City)
def city_post_save_signal(sender, instance, **kwargs):
    instance.country.cities_count += 1
    instance.country.save()


@receiver(pre_delete, sender=City)
def city_del_signal(sender, instance, **kwargs):
    instance.country.cities_count -= 1
    instance.country.save()


@receiver(post_delete, sender=City)
def city_post_del_signal(sender, instance, **kwargs):
    print(f"Город {instance} удален ")
