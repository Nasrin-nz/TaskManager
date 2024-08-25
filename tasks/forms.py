from django import forms
from django.contrib.auth.models import User
from .models import Referral
from .models import Action

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['receiving_user', 'referral_description']

    receiving_user = forms.ModelChoiceField(queryset=User.objects.all(), label="کاربر ارجاع گیرنده")
    referral_description = forms.CharField(widget=forms.Textarea, label="توضیح ارجاع")



class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['action_description', 'attachment']
