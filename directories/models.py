from django.db import models

class Directories(models.Model):
    '''
    Directories class model
    '''

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'directories'
        managed = True
        verbose_name = 'Directories'
        verbose_name_plural = 'Directories'

    full_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=30)
    urgent_phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    date_of_service = models.DateField()
    end_of_service = models.DateField(null=True)
    state = models.IntegerField() # conge|permission|other
    avatar = models.CharField(max_length=100, null=True)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)