from django.db import models

class Absences(models.Model):

    class Meta():
        db_table = "absences"
        ordering = ["created_at"]


    TYPES = (
        ('MVCT', 'Maternity Vacation'),
        ('PVCT', 'Peternity Vacation'),
        ('SVCT', 'Sickness Vacation'),
        ('PRM', 'Permission'),
        ('FRM', 'Formation'),
        ('OTH', 'Other')
    )

    STATUS = (
        # You can get the 2nd value of the tuple with get_status_display
        (0, 'Waiting'),
        (1, 'Waiting for second validation'),
        (2, 'Validated'),
        (3, 'Abandoned'),
        (4, 'Rejected')
    )

    directory_id = models.IntegerField(help_text="The ID of person who does the request")
    types = models.CharField(max_length=20, choices=TYPES, help_text="Type of the absence (vacation|permission|external formation|other)")
    begin_date = models.DateField(help_text="Beginning date of the absence")
    end_date = models.DateField(help_text="Ending date of the absence")
    interim = models.CharField(max_length=50, null=True, help_text="The interim person")
    reasons = models.TextField(help_text="The reasons of absence")
    status = models.IntegerField(default=0, choices=STATUS, help_text="The status of absence if it is done = 1 or doing = 0 or abandoned = 2")
    validator_1 = models.CharField(null=True, max_length=50, help_text="The first responsible who valide the absence")
    first_validation_at = models.DateTimeField(null=True, help_text="Date of the first validation")
    validator_2 = models.CharField(null=True, max_length=50, help_text="The second responsible who valide the absence")
    second_validation_at = models.DateTimeField(null=True, help_text="Date of second validation and the last validation")
    justificative = models.CharField(max_length=50, null=True, help_text="Justivicative piece [optional]")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date of request")
    updated_at = models.DateTimeField(auto_now=True, null=True, help_text="Date of last update")

    # Calcul date number of absence
    def dateNumber(self):
        return self.end_date - self.begin_date 

    # Check if first validation is done
    def checkFirstValidation(self):
        if self.validator_1 == None and self.first_validation_at == None:
            return ""
        else:
            return "Valid"

    # Checkif second and the last validation is done
    def checkSecondValidation(self):
        if self.validator_2 == None and self.second_validation_at == None:
            return ""
        else:
            return "Valid"

    # Store a new absence
    def store(self, datas):
        super().save(datas)

    def __str__(self):
        return self.type

