from django.db import models


class Category(models.Model):
    categoryid = models.AutoField(primary_key=True, db_column='categoryid')
    categoryname = models.CharField(max_length=40)

    def __str__(self):
        return self.categoryname
