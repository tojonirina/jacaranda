from django.db import models

# Create your models here.

class Materials(models.Model):
    """
    Materiel model class
    """

    class Meta:
        db_table = 'materials'

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unity = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    administrator = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class MouvmentHistory(models.Model):
    """
    Material mouvement History 
    """

    class Meta:
        db_table = 'mouvment_history'

    title = models.CharField(max_length=100)
    product_id = models.IntegerField(null=True)
    description = models.TextField(null=True)
    note = models.TextField(null=True)
    quantity = models.IntegerField()
    unity = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    administrator = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description , self.type