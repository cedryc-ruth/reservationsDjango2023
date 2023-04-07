from django import forms
from  catalogue.models import Artist

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'
        #exclude = ['mobile']  #mobile field is excluded