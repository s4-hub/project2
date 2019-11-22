from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class':
                                          'quantity form-control input-number',
                                          'value': 1,
                                          'min': 1}),)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
