from django import forms
from home.models import UserPost

class HomeForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            # 'class': 'form-control',
            'placeholder': 'User@bauercomp.com'
        }
    ))

    class Meta:
        model = UserPost
        fields = ['email','panel_size','panel_holes_punch_qty','panel_holes_cut_qty']
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("@bauercomp.com"):
            raise forms.ValidationError("This is not a valid email")
        return email

