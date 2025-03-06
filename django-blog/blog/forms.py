from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','content']
        labels = {'name': 'نام و نام خانوادگی','email':'ایمیل','content':'نظر'}
        widgets = {'name': forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'content':forms.Textarea(attrs={'class':'form-control'})
                   }

    

class SearchForm(forms.Form):
    query = forms.CharField(label='جستجو',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))