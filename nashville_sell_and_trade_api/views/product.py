from django.core.exceptions import ValidationError
from rest_framework import status, views
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action

from nashville_sell_and_trade_api.models import Product, NashUser, Category, category, nash_user, product


class ProductView(ViewSet):
    def create(self, request):

        nash_user = NashUser.objects.get(user=request.auth.user)

        try:
            product = Product.objects.create(
                title=request.data['title'],
                description=request.data["description"],
                trade=request.data["trade"],
                price=request.data["price"],
                image=request.data["image"],
                quantity=request.data["quantity"],
                nash_user=nash_user

            )
            product.categories.set(request.data['categories'])
            serializer = ProductSerializer(
                product, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        
        products = Product.objects.all()
        categories = request.GET.getlist('category')

        if len(categories) != 0:
            for category in categories:
                products = products.filter(categories__id=category).distinct()

        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(
                product, context={'request': request})
            return Response(serializer.data)
        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        nash_user = NashUser.objects.get(user=request.auth.user)

        product = Product.objects.get(pk=pk)
        product.title = request.data['title']
        product.description = request.data["description"]
        product.trade = request.data["trade"]
        product.price = request.data["price"]
        product.image = request.data["image"]
        product.quantity = request.data["quantity"]
        product.nash_user = nash_user
        
        product.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["get"], detail=False)
    def my_products(self, request):
        nash_user = NashUser.objects.get(user=request.auth.user)

        products = Product.objects.filter(nash_user_id=nash_user.id)
        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)
    
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'categories', 'price',
                  'image', 'trade', 'quantity', 'nash_user', 'date_posted')
        depth = 1
