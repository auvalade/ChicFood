from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from .models import Food

text_only_validator = RegexValidator(r'^[a-zA-Z ]*$', "Ensure this value only contains letters and spaces.")


# Add Food Form 
class AddFoodForm(forms.Form):
    name = forms.CharField(max_length=20, validators=[text_only_validator], label='What food is it ? (20 char)')
    short_desc = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea', 'rows':'3'}), max_length=256, label='Describe it in a few words (256 char)')
    healthy_level = forms.IntegerField(label='How healthy is it ? (0 - 10)', validators=[MaxValueValidator(10), MinValueValidator(0)])
    taste_level = forms.IntegerField(label='How good is it ? (0 - 10)', validators=[MaxValueValidator(10), MinValueValidator(0)])
    quantity = forms.IntegerField(label='Quantity (0-999)', validators=[MaxValueValidator(999), MinValueValidator(1)])
    price = forms.DecimalField(label='Price (0 - 99.99)', max_digits=4, decimal_places=2, validators=[MaxValueValidator(99.99), MinValueValidator(0.0)])


# Login Form 
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
