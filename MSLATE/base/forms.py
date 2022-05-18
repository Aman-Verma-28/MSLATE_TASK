from django.forms import *
from .models import UserDetails
class DetailForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ["score"]
