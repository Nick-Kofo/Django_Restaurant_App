from django import forms  # import forms
from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish  # which model will be used to create this form
        fields = (
            'name', 'price', 'type',  'categoryA', 'categoryB', 'description', 'photo')  # which fields will be shown to the form
