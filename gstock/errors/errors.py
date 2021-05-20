from django.http import HttpResponse

class Http401(HttpResponse):
    """
    401 unauthoriezd error response
    """
    def __init__(self, errorMessage):
        super().__init__(errorMessage, status=401)