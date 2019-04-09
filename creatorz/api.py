from rest_framework import viewsets
from .serializers import MusicianSerialiser
from .serializers import WriterSerialiser
from .serializers import CustomerSerialiser

from .models import Musician
from .models import Writer
from .models import Customer


class MusicianViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MusicianSerialiser
    queryset = Musician.objects.all()

class WriterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WriterSerialiser
    queryset = Writer.objects.all()

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomerSerialiser
    queryset = Customer.objects.all()
