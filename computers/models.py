from django.db import models

# Create your models here.

class Computers(models.Model):

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'computers'
        managed = True
        verbose_name = 'Computers'
        verbose_name_plural = 'Computers'
    
    description = models.CharField("computers description", max_length=50)
    reference = models.CharField("reference of computer", max_length=30)
    mark = models.CharField(max_length=50)
    os = models.CharField("operating system", max_length=20)
    category = models.CharField("category of computer", max_length=30) #PC|mac|desktop
    assigned_to = models.IntegerField("is assigned", null=True)
    assigned_at = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("date of last update", auto_now=True)



