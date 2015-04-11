from django.db import models


class Category(models.Model):
    categoryid = models.AutoField(primary_key=True, db_column='categoryid')
    categoryname = models.CharField(max_length=40)
    categoryurl = models.CharField(max_length=25)

    def __str__(self):
        return self.categoryname
