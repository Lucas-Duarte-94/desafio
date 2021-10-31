from rest_framework import serializers
from .models import Card, Tag

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'texto', 'data_criacao', 'data_modificacao', 'tags')

class CreateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('texto', 'tags')

class UpdateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('texto', 'data_modificacao', 'tags')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')