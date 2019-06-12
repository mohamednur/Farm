from django import forms
# from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Crops, Fertilizer


class ExtendedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2', 'is_staff')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserprofileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile_no',)


class CropsForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ('name', 'description', 'quantity')

    def clean_name(self):
        name = self.cleaned_data['name']

        name_qs = Crops.objects.filter(name__iexact=name)
        if name_qs.exists():
            raise forms.ValidationError("This crop already exists")

        return name


class addProduce(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ('name', 'description', 'quantity')

        def clean_name(self):
            name = self.cleaned_data['name']

            name_qs1 = Crops.objects.filter(name__iexact=name)
            if name_qs1.exists():
                raise forms.ValidationError("This crop already exists")

            return name


class addFertilizer(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ('fname', 'quantity', 'used_for_crop')

        def clean_name(self):
            fertilzer_name = self.cleaned_data['fname']
            return fertilzer_name
