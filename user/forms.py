from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import AccountModel, Review

class AccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            AccountModel.objects.create(
                user = user,
            )
        return user


class DepositeForm(forms.Form):
    amount = forms.DecimalField(max_digits=12, decimal_places=2)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']