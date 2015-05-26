from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    stateid = models.AutoField(primary_key=True)
    stateshort = models.CharField(max_length=2)
    statelong = models.CharField(max_length=15)

    def __str__(self):
        return self.stateshort


class City(models.Model):
    cityid = models.AutoField(primary_key=True)
    cityname = models.CharField(max_length=50)
    state = models.ForeignKey('State', db_column='stateid')

    def __str__(self):
        return self.cityname


class UserProfile(models.Model):
    profileid = models.AutoField(primary_key=True, db_column='profileid')
    userid = models.ForeignKey(User, db_column='userid')
    city = models.ForeignKey('City', db_column='cityid')

    def __str__(self):
        return self.profileid
