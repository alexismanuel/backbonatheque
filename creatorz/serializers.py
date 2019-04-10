from rest_framework import serializers
from .models import Musician, Writer, Customer, PlayError

class MusicianSerialiser(serializers.ModelSerializer):

    albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Musician
        fields = "__all__"


class WriterSerialiser(serializers.ModelSerializer):

    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = "__all__"

class CustomerSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = "__all__"


class PlayErrorSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = PlayError
        fields = "__all__"
