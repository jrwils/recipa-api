from django.db import models


class Recipe(models.Model):
    recipeid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    intro = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    endcomments = models.TextField(blank=True)
    url = models.CharField(max_length=40, db_index=True)
    submitter = models.ForeignKey('submitter.Submitter')
    category = models.ManyToManyField('category.Category')

    def __str__(self):
        return self.title
