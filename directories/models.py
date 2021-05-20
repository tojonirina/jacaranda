from django.db import models

class Directory(models.Model):
    '''
    Directory class model
    '''

    class Meta:
        db_table = 'directories'
        ordering = ['-created_at']

    GENDER = (
        ('man', 'Homme'),
        ('woman', 'Femme'),
        ('other', 'Other')
    )

    STATE = (
        (1, "En service"),
        (2, "En Pause"),
        (3, "En permission"),
        (4, "En conge"),
        (0, "Hors service")
    )

    full_name = models.CharField(max_length=30)
    gender = models.CharField(choices = GENDER, max_length=10)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    cin = models.CharField(max_length=20)
    delivered_on = models.DateField()
    delivered_at = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    urgent_phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    departement = models.CharField(max_length=20)
    date_of_service = models.DateField()
    end_of_service = models.DateField(null=True)
    matricule_number = models.CharField(max_length=10)
    state = models.IntegerField(default = 1, choices = STATE)
    avatar = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    administrator = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.full_name