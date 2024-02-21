from django import forms
from .models import PlantedTree, Account, Tree



class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ['account', 'tree', 'title', 'age', 'location_latitude', 'location_longitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.all()
        self.fields['tree'].queryset = Tree.objects.all()

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
