from django.forms import ModelForm
from .models import Uses, Merchant

class UsesForm(ModelForm):
  class Meta:
    model = Uses
    fields = ['date', 'quest', 'details']