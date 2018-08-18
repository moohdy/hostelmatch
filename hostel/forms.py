from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=25, label='',widget=forms.TextInput (attrs=
                {'class':'form-control','placeholder':'Name(required)','id':'name','name':'name','required':True}))
    email = forms.EmailField( label='', widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email(required)','id':'email',
                'name':'email','required':True}))
    subject = forms.CharField( label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subject(optional)','id':'subject',
                'name':'subject','required':True}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','style':'max-height:8em','rows':'3',
                'placeholder':'Message(required)','id':'message', 'name':'message','required':True}))
    
    