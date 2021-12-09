from django.core.exceptions import ValidationError
from rest_framework import status, views
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from nashville_sell_and_trade_api.models import Category

class CategoryView(ViewSet):
    def list(self, request):
        
        category = Category.objects.all()
        serializer = CategorySerializer( category, many=True, context={'request': request})
        return Response(serializer.data)
    
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields =('id','label')