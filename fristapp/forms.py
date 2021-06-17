from  django import forms
from  fristapp.models import  student,usercreation,login

class studemform(forms.ModelForm):
    class Meta:
        model = student
        fields =['name','age','address','phone','pic']


class usercreationform(forms.ModelForm):
    class Meta:
        model = usercreation
        fields ='__all__'


class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields='__all__'
