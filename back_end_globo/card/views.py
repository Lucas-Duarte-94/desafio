from copy import error
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CardSerializer, CreateCardSerializer, UpdateCardSerializer, TagSerializer
from .models import Card, Tag
from django.utils import timezone

# Create your views here.

class CardView(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

class CreateCardView(APIView):
    serializer_class = CreateCardSerializer

    def post(self, request, format=None):
        updated_request = request.POST.copy()
        tag = Tag.objects.get_or_create(name=updated_request['tags'])
        updated_request['tags'] = tag[0].id

        serializer = CreateCardSerializer(data=updated_request)
        
        if serializer.is_valid():

            instance = Tag.objects.get(id=serializer.data['tags'])
            
            new_card = Card.objects.create(texto=serializer.data['texto'], tags=instance)

            new_card.save()

            new_serializer = CreateCardSerializer(new_card)

            return Response(new_serializer.data, status=status.HTTP_201_CREATED)    
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class UpdateDeleteCardView(APIView):
    serializer_class = CreateCardSerializer

    def put(self, request, pk, format=None):
        card_object = Card.objects.get(pk=pk)
        req_copy = request.POST.copy()
        tag_object = Tag.objects.get_or_create(name=req_copy['tags'])
        req_copy['tags'] = tag_object[0].id
        
        serializer = UpdateCardSerializer(card_object, data=req_copy)

        if serializer.is_valid():
            data_modificacao = timezone.now()

            instance = Tag.objects.get(id=tag_object[0].id)

            serializer.validated_data['texto'] = request.data['texto'] 
            serializer.validated_data['data_modificacao'] = data_modificacao
            serializer.validated_data['tags'] = instance

            serializer.save()

            res = serializer.data

            return Response(data=res, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        card_object = Card.objects.get(pk=pk)
        card_object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TagView(APIView):
    serializer_class = TagSerializer

    def get(self, request, format=None):
        queryset = Tag.objects.all()

        serializer = TagSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)

        if serializer.is_valid():
            try:
                tag_exists = Tag.objects.get(name=serializer.data['name'])

                res = {
                    'id': tag_exists.id,
                    'name': tag_exists.name
                }
                
                return Response(res, status=status.HTTP_200_OK)


            except Tag.DoesNotExist:
                new_tag = Tag.objects.create(name=serializer.data['name'])

                new_tag.save()

                serialized = TagSerializer(new_tag)
                
                return Response(serialized.data, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(data=request.data)

        if serializer.is_valid():
            tag.name = serializer.validated_data['name']
            tag.save()
      
            res = {
                'id': tag.id,
                'name': tag.name
            }

            return Response(data=res, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tag_object = Tag.objects.get(pk=pk)
        tag_object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
