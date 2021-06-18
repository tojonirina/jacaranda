from django.db import models

# Create your models here.

class Material(models.Model):
    """
    Material model class
    """

    class Meta:
        db_table = 'materials'
        ordering = ['-created_at']

    STATE = (
        ('new','Nouveau'),
        ('occasion','Occasion'),
        ('hs','Hors service')
    )

    UNITY = (
        ('pcs','Piece'),
        ('cartoon','Carton'),
        ('box','Boite'),
        ('kg','Kg'),
        ('g','Gramme'),
        ('L','Litre'),
        ('m','Metre')
    )

    title = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    modele = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unity = models.CharField(max_length=50, choices=UNITY)
    state = models.CharField(max_length=10, choices=STATE)
    fournissor = models.CharField(max_length=50, null=True)
    fournissor_contact = models.CharField(max_length=30, blank=True)
    administrator = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return self.title

class MouvmentHistory(models.Model):
    """
    Material mouvement History 
    """

    class Meta:
        db_table = 'mouvment_history'
        ordering = ['-created_at']

    TYPES = (
        ('entry', 'Entree'),
        ('takeout', 'Sortie'),
        ('edit', 'Edition')
    )

    STATE = (
        ('new','Nouveau'),
        ('occasion','Occasion'),
        ('out_of_service','Hors service'),
        ('out_of_service_reparable','Hors service reparable'),
    )

    product_name = models.CharField(max_length=50, null=True)
    product_id = models.IntegerField(null=True)
    description = models.TextField(null=True)
    note = models.TextField(null=True)
    quantity = models.IntegerField()
    unity = models.CharField(max_length=20)
    types = models.CharField(max_length=50, choices=TYPES)
    state = models.CharField(max_length=10, choices=STATE)
    administrator = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description , self.types