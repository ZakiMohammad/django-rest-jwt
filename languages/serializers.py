from rest_framework import serializers
from .models import Languages, Paradigm, Programmer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Languages
        fields = ("url", "id", "name", "paradigm")


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ("id", "url", "name")


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    # class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ("id", "url", "name", "Languages")
