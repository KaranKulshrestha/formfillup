from django import forms
from form_app.models import Profile, Contact

class New_Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

