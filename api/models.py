from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    title_kana = models.CharField(max_length=100)
    title_english = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    release_date = models.DateField(auto_now=False)
    release_price = models.IntegerField()
    loose_price = models.IntegerField()
    boxed_price = models.IntegerField()
    def __str__(self):
        return self.title
