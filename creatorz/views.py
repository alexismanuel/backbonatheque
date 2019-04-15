import logging
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Album, Customer

logger = logging.getLogger()
def albums(request):
    """ Show albums in view for testing purpose """
    album_list = Album.objects.all()
    context = {'album_list': album_list}
    return render(request, 'templates/albums.html', context)

def play(request, customer_id, album_id):
    """ Toggle_plagin method call """
    if customer_id and album_id:
        customer = Customer.objects.filter(id=customer_id)[0]
        Album.objects.filter(id=album_id)[0].toggle_playing(customer)
    return redirect('/albums')
