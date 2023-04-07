from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect

from catalogue.models import Artist
from catalogue.forms.ArtistForm import *

# Create your views here.
def index(request):
    artists = Artist.objects.all()
    
    return render(request, 'artist/index.html', {
        'artists':artists,
    })

def show(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant');

    title = 'Fiche d\'un artiste'

    return render(request, 'artist/show.html', {
        'artist':artist,
    })

def edit(request, artist_id):
    # Récupérer l'artiste à modifier
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant');
        
    form = ArtistForm(instance=artist)
    
    return render(request, 'artist/edit.html', {
        'form':form,
        'artist':artist,
    })

def update(request, artist_id):
    method = request.POST.get('_method', '').upper()

    # Vérifier s'il s'agit bien d'une méthode PUT
    if method == 'PUT':
        # Récupérer l'artiste à modifier
        try:
            artist = Artist.objects.get(id=artist_id)
        except Artist.DoesNotExist:
            raise Http404('Artist inexistant');

        # Créer un formulaire pour modifier un artiste existant, mais
        # utiliser les données du POST pour remplir le formulaire
        form = ArtistForm(request.POST, instance=artist)

        # Vérifier si les données du formulaire sont valides
        if form.is_valid():
            # Persister les données en base de données           
            form.save();

            return render(request, 'artist/show.html', {
                'artist':artist,
            })

    return HttpResponseRedirect('artist-show')