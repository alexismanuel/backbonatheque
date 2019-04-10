from rest_framework import viewsets
from .serializers import MusicianSerialiser, WriterSerialiser, CustomerSerialiser, PlayErrorSerialiser
from .models import Musician, Writer, Customer, PlayError


class MusicianViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MusicianSerialiser
    queryset = Musician.objects.all()

class WriterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WriterSerialiser
    queryset = Writer.objects.all()

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomerSerialiser
    queryset = Customer.objects.all()

class PlayErrorViewSet(viewsets.ModelViewSet):
    serializer_class = PlayErrorSerialiser
    queryset = PlayError.objects.all()
