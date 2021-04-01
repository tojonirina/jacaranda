from django.db import models

# Create your models here.

class Computers(models.Model):

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'computers'
        verbose_name = 'Computers'
        verbose_name_plural = 'Computers'

    STATE = (
        ('new','Nouveau'),
        ('reconditioned','Reconditionne')
    )

    name = models.CharField(max_length=50)
    description = models.CharField("computers description", max_length=50)
    state = models.CharField(max_length=20, choices=STATE)
    serial_number = models.CharField(max_length=30)
    modele = models.CharField("the modele of computer", max_length=30)
    mark = models.CharField(max_length=50)
    os = models.CharField("operating system", max_length=20)
    processor = models.CharField(max_length=10)
    processor_generation = models.CharField(max_length=10)
    category = models.CharField("category of computer", max_length=30) #PC|mac|desktop
    ram = models.IntegerField()
    type_of_ram = models.CharField(max_length=10)
    fournissor = models.CharField(max_length=50)
    fournissor_contact = models.CharField(max_length=30)
    assigned_to = models.CharField("is assigned", max_length=50, null=True)
    assigned_at = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("date of last update", auto_now=True)



