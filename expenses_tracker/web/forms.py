import os

from django import forms

from expenses_tracker.web.models import Profile, Expenses


# Profile Forms
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        image_path = self.instance.image.path
        os.remove(image_path)
        if commit:
            self.instance.delete()

    class Meta:
        model = Profile
        fields = ()


# Expenses Forms
class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('title', 'description', 'image', 'price')


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('title', 'description', 'image', 'price')


class DeleteExpenseForm(forms.ModelForm):

    def save(self, commit=True):
        # image_path = self.instance.image.path
        # os.remove(image_path)
        if commit:
            self.instance.delete()

    class Meta:
        model = Expenses
        fields = ()



