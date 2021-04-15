from django.db import models

# class SessionHistory(models.Model):
#     """
#     Session history class model
#     """

#     class Meta:
#         db_table = 'session_history'

#     user_id = models.IntegerField()
#     login = models.CharField(max_length=50)
#     logged = models.BooleanField(default=True)
#     token = models.CharField(max_length=100)
#     user_agent = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.login 


class User(models.Model):
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

    directory_id = models.IntegerField(unique=True, null=False, help_text="Directory ID which the owner of the account")
    login = models.CharField(max_length=50, null=False, unique=True, help_text="Users login")
    password = models.CharField(max_length=100, null=False, help_text="Users password")
    types = models.CharField(default="user", max_length=20, choices=TYPES, help_text="Users account type [user, administrator, super_user]")
    status = models.IntegerField(default=1, help_text="Users accout status [blocked or unlocked]")
    administrator = models.CharField(max_length=50, null=False, help_text="Users who create the account")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Account creation date")
    updated_at = models.DateTimeField(auto_now=True, null=True, help_text="Last date of update")

    def __str__(self):
        return self.login

