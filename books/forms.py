from django.forms import ModelForm
from books.models import Store

class StoreForms(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'