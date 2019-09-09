from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    founder = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('name',)

class Region(models.Model):

    description = models.CharField(blank=True, max_length=50)
    token = models.CharField(blank=True, max_length=20)

    class Meta:
        ordering = ('description',)

#    def get_absolute_url(self):  # get_absolute_url
#
#        return reverse('token:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.road
