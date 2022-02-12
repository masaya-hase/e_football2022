from django import forms
from .models import Player, Skill, Ability, Formation, RarityCategory
from django.forms import inlineformset_factory,widgets
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse



class PlayerCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model =  Player
        exclude = ('skill',)   

        widgets = {
            "new_date_field": widgets.SelectDateWidget(years=range(2021, 2030))
            }

class SkillForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model =  Player
        fields= ('skill',)

class AbilityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model =  Ability
        fields='__all__'

class FormationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model =  Formation
        fields='__all__'
        
# editform 
SkillInlineFormSet = forms.inlineformset_factory(
    Player, Player.skill.through, form=SkillForm, can_delete=False
)

AbilityFormSet = forms.inlineformset_factory(
    Player, Ability, form=AbilityForm, extra=0
)

FormationFormSet = forms.inlineformset_factory(
    Player, Formation, form=FormationForm, extra=0
)

# addform
SkillInlineAddFormSet = forms.inlineformset_factory(
    Player, Player.skill.through, form=SkillForm, can_delete=False, extra=10
)

AbilityAddFormSet = forms.inlineformset_factory(
    Player, Ability, form=AbilityForm, extra=1
)

FormationAddFormSet = forms.inlineformset_factory(
    Player, Formation, form=FormationForm, extra=1
)

class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    subject = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "件名",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")