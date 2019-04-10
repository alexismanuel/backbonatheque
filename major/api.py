from rest_framework import viewsets
from random import randint
from time import sleep

from .serializers import MajorPlaybackSerializer
from .models import MajorPlayback


class MajorException(Exception):
    pass


class MajorPlaybackView(viewsets.ModelViewSet):
    serializer_class = MajorPlaybackSerializer
    queryset = MajorPlayback.objects.all()

    def create(self, request, *args, **kwargs):
        album = self.request.data.get('album')
        status = self.request.data.get('status')
        customer = self.request.data.get('customer')
        last_play = MajorPlayback.objects.filter(customer=customer, album=album).order_by("-pk").first()
        # Validators
        if not last_play and status == "STOP":
            raise MajorException
        if last_play and last_play.status == status:
            raise MajorException
        # Simulate random timeout
        if randint(1, 10) >= 9:
            sleep(10)
        return super(MajorPlaybackView, self).create(request, *args, **kwargs)
