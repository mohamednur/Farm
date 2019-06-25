from django import forms
from django.core.validators import validate_integer
# from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Crops, Fertilizer, FinancialRecords, FarmMachinery


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
        quantity = self.cleaned_data['quantity']
        if (quantity < 0):
            raise forms.ValidationError("Quantity cannot be less than 0")

        name_qs = Crops.objects.filter(name__iexact=name)
        if name_qs.exists():
            raise forms.ValidationError("This crop already exists")

        return name


class AddProduceForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ('name', 'description', 'quantity')

        def clean_name(self):
            name = self.cleaned_data['name']

            quantity = self.cleaned_data['quantity']
            if (quantity == 0):
                raise forms.ValidationError("Quantity cannot be less than 0")

            # validate_integer(quantity, None)

            name_qs1 = Crops.objects.filter(name__iexact=name)
            if name_qs1.exists():
                raise forms.ValidationError("This crop already exists")

            return name, quantity


class AddFertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ('fname', 'quantity', 'used_for_crop')
        labels = {
            "fname": "Fertilizer Name",
        }
        help_texts = {
            "fname": "Enter Fertilizer name",
        }

        def clean_name(self):
            fertilizer_name = self.cleaned_data['fname']
            fertilizer_quantity = self.cleaned_data['quantity']

            if (fertilizer_quantity < 3):
                raise forms.ValidationError("Quantity cannot be less than 0")
            return fertilizer_name, fertilizer_quantity


class FinancialRecordsForms(forms.ModelForm):
    class Meta:
        model = FinancialRecords

        fields = ('receipt_no', 'Amount', 'date_of_payment')
        labels = {
            "receipt_no": "Receipt Number",
            "date_of_payment": "Date Of Payment",
        }
        help_texts = {
            "receipt_no": "Enter The Receipt Number",
            "date_of_payment": "Enter The Date when the payment was made",
        }


class FarmMachineryForm(forms.ModelForm):
    class Meta:
        model = FarmMachinery

        fields = ('machinery_type', 'name', 'identification_no',
                  'status', 'last_serviced', 'date_of_purchase')
        labels = {

        }
        help_texts = {
            'machinery_type': "Select The type of Machinery",
            'name': "Enter the name of the machine",
            'identification_no': "Enter Identification Number of the machine",
            'status': "Select the status of the machine",
            'last_serviced': "Enter the date when the machine was last serviced",
            'date_of_purchase': "Enter the date when the machine was purchased",
        }
