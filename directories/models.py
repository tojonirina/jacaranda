from django.db import models

# Create your models here.

class Directories(models.Model):

    def __str__(self):
        self.full_name

    class Meta:
        db_table = 'directories'
        managed = True
        verbose_name = 'Directories'
        verbose_name_plural = 'Directoriess'

    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    urgent_phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    date_of_service = models.DateField()
    end_of_service = models.DateField(null=True)
    state = models.IntegerField() # conge|permission|other
    avatar = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)