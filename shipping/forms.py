from django import forms
from shipping.models import ShippingAddress
from lib.validators import min_length_validator

class ShippingAddressForm(forms.ModelForm):
     # zipcode = forms.CharField(validators=[min_length_validator], max_length=16)

    class Meta:
        model = ShippingAddress
        fields = ['city', 'zipcode', 'address', 'number']
        #exclude = ['user']



        def clean_zipcode(self):
            zipcode = self.cleaned_data['zipcode']
            city = self.cleaned_data['city']
            if len(zipcode) !=16:
                raise ValidatorError("length is not 16")
            return zipcode

        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data