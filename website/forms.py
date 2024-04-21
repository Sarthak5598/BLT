from captcha.fields import CaptchaField
from django import forms
from mdeditor.fields import MDTextFormField

from .models import Monitor, UserProfile ,Bid


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("user_avatar",)


class UserDeleteForm(forms.Form):
    delete = forms.BooleanField(required=True)


class HuntForm(forms.Form):
    content = MDTextFormField()
    start_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"class": "col-sm-6", "readonly": True}),
        label="",
        required=False,
    )
    end_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"class": "col-sm-6", "readonly": True}),
        label="",
        required=False,
    )


class CaptchaForm(forms.Form):
    captcha = CaptchaField()


class QuickIssueForm(forms.Form):
    url = forms.CharField()
    label = forms.CharField()
    description = forms.CharField()


class MonitorForm(forms.ModelForm):
    created = forms.DateTimeField(widget=forms.HiddenInput(), required=False, label="Created")
    modified = forms.DateTimeField(widget=forms.HiddenInput(), required=False, label="Modified")

    class Meta:
        model = Monitor
        fields = ["url", "keyword"]

class Bidding(forms.ModelForm):
    class Meta: 
        model= Bid
        fields= ['issue_url','current_bid','time_left','bid_amount']