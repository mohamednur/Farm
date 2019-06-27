from django import forms
from django.core.validators import validate_integer
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile, Crops, Fertilizer, FinancialRecords, FarmMachinery, Produce, ProduceSold
from .widgets import BootstrapDateTimePickerInput


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )


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

    # def clean_name(self):
        # name = self.cleaned_data['name']

        # name_qs = Crops.objects.filter(name__iexact=name)
        # if name_qs.exists():
        #  raise forms.ValidationError("This crop already exists")

        # return name


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

        Widgets = {
            'quantity': forms.TextInput(attrs={'placeholder': 'Enter Quantity in Kgs'}),
        }
        fields = ('fname', 'quantity', 'used_for_crop')
        labels = {
            "fname": "Fertilizer Name",
        }
        help_texts = {
            "fname": "Enter Fertilizer name",
            "quantity": "Enter Quantity in Kgs",
        }

        def clean_name(self):
            fertilizer_name = self.cleaned_data['fname']
            fertilizer_quantity = self.cleaned_data['quantity']


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


class ProduceForm(forms.ModelForm):
    class Meta:
        model = Produce
        fields = ('from_crop', 'quantity', 'submitted_by',
                  'date_submitted')
        labels = {
            'from_crop': "From crop",
            'quantity': "Quantity(in Kgs)",
            'date_submitted': "Date Submitted",
        }
        help_texts = {
            'from_crop': "Select the Crop which the produce is",
            'quantity': "Enter the produce quantity(in Kgs)",
            'submitted_by': "The employee who submitted the produce",
            'date_submitted': "Enter the date when the produce was submitted",
        }


class ProduceSoldForm(forms.ModelForm):
    class Meta:
        model = ProduceSold
        fields = ('produce', 'sold_quantity', 'amount', 'date_sold')
        labels = {
            'produce': "Produce",
            'sold_quantity': "Sold Quantity(in Kgs)",
            'amount': "Amount(in Ksh)",
            'date_sold': "Date sold",
        }
        help_texts = {
            'produce': "Select the farm produce to sell",
            'sold_quantity': "Enter the produce quantity sold in Kgs",
            'amount': "Enter the amount which the produce was sold for",
            'date_sold': "Enter the date when produce was sold",


        }
