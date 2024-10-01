from django import forms
from .models import Author
from book.models import Book


class AuthorCreateForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(), 
        required=False, 
        widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic', 'books']
        
        
class AuthorUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorUpdateForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['name'].initial = instance.name
            self.fields['surname'].initial = instance.surname
            self.fields['patronymic'].initial = instance.patronymic
            self.fields['books'].queryset = Book.objects.all()
            self.fields['books'].initial = instance.books.all()
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(), 
        required=False, 
        widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic', 'books']

    
        
