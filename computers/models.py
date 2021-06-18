from django.db import models

class Computers(models.Model):

    class Meta:
        db_table = 'computers'
        ordering: ['name']

    STATE = (
        ('new','Nouveau'),
        ('old','Ancien')
    )

    CATEGORY = (
        ('laptop','Laptop'),
        ('desktop','Desktop'),
        ('mbp','MacBook Pro'),
        ('mbp_retina','MacBook Pro Retina'),
        ('notebook','Notebook')
    )

    STATUS = (
        ('assigned','Attribue'),
        ('not_assigned','Non attribue'),
        ('on_suspens','En suspens'),
        ('out_of_service','Hors service'),
        ('out_of_service_reparable','Hors service reparable'),
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
    category = models.CharField("category of computer", max_length=30, choices=CATEGORY)
    ram = models.IntegerField()
    type_of_ram = models.CharField(max_length=10)
    fournissor = models.CharField(max_length=50)
    fournissor_contact = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS)
    assigned_to = models.CharField("is assigned", max_length=50, null=True)
    administrator = models.CharField(max_length=50)
    assigned_at = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("date of last update", auto_now=True)

    def __str__(self):
        return self.description

class AllocationHistory(models.Model):

    class Meta:
        db_table = 'allocation_history'
        ordering : ['-created_at']

    name = models.CharField(max_length=50)
    assigned_to = models.CharField("is assigned", max_length=50)
    assigned_by = models.CharField(max_length=50)
    note = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

