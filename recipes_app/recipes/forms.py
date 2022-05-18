from django import forms


class NewRecipeForm(forms.Form):
    title = forms.CharField(label='Recipe Title', max_length=300)
    portions = forms.IntegerField(label='Portions')
    ingredients = forms.CharField(label='Ingredients', max_length=300)
    steps = forms.CharField(label='Steps', widget=forms.Textarea)
    filters = forms.CharField(label="Filters")
