from django.db import models

class SessionHistory(models.Model):
    """
    Session history class model
    """

    class Meta:
        db_table = 'session_history'

    user_id = models.IntegerField()
    login = models.CharField(max_length=50)
    logged = models.BooleanField(default=True)
    token = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login 


class Users(models.Model):
    """
    User class model
    """
    class Meta:
        db_table = 'users'

    TYPES = (
        ('user', 'Standard User'),
        ('administrator', 'Administrator User'),
        ('super_user', 'Super Administrator User'),
    )

    directory_id = models.IntegerField()
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    types = models.CharField(max_length=20, choices=TYPES)
    status = models.IntegerField()
    administrator = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

