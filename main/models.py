from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)

    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='department', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse('main:DepartmentView', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Docter(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='docter', blank=True)
    qualification = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    queue = models.IntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Docter'
        verbose_name_plural = 'Docters'

    def get_url(self):
        return reverse('appoiment:DocDetails', args=[self.department.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
