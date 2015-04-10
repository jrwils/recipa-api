from django.db import models


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


class Submitter(models.Model):
    submitterid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    city = models.ForeignKey('City', db_column='cityid')

    def __str__(self):
        return self.firstname + ' ' + self.lastname
