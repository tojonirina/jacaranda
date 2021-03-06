from django.db import models
from directories.models import Directory

class SessionHistory(models.Model):
    """
    Session history class model
    """

    class Meta:
        db_table = 'session_history'
        ordering = ['-created_at']

    user_id = models.IntegerField()
    login = models.CharField(max_length=50)
    user_agent = models.CharField(max_length=255)
    computer_user = models.CharField(max_length=50)
    computer_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login 


class User(models.Model):
    """
    User class model
    """
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

    TYPES = (
        ('user', 'Standard User'),
        ('administrator', 'Administrator User'),
        ('super_user', 'Super Administrator User'),
    )

    directory_id = models.IntegerField(unique=True, null=False, help_text="Directory ID which the owner of the account")
    # directory = models.ForeignKey(Directory, on_delete=models.CASCADE)
    login = models.CharField(max_length=50, null=False, unique=True, help_text="Users login")
    password = models.CharField(max_length=100, null=False, help_text="Users password")
    types = models.CharField(default="user", max_length=20, choices=TYPES, help_text="Users account type [user, administrator, super_user]")
    status = models.IntegerField(default=1, help_text="Users accout status [blocked or unlocked]")
    administrator = models.CharField(max_length=50, null=False, help_text="Users who create the account")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Account creation date")
    updated_at = models.DateTimeField(auto_now=True, null=True, help_text="Last date of update")

    def __str__(self):
        return self.login

