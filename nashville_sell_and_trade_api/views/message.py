from django.core.exceptions import ValidationError
from rest_framework import status, views
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User

from nashville_sell_and_trade_api.models import Message, NashUser, Product


class MessageView(ViewSet):

    def list(self, request):
        nash_user = NashUser.objects.get(user=request.auth.user)
        message = Message.objects.filter(recipient=nash_user.id)

        serializer = MessageSerializer(
            message, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            message = Message.objects.get(pk=pk)
            serializer = MessageSerializer(message, context={"request"})
            return Response(serializer.data)
        except Message.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            message = Message.objects.get(pk=pk)
            message.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Message.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        nash_user = NashUser.objects.get(user=request.auth.user)
        product = Product.objects.get(pk=request.data['product_Id'])
        recipient = NashUser.objects.get(pk=request.data['recipient'])

        try:
            message = Message.objects.create(
                message=request.data['message'],
                product=product,
                sender=nash_user,
                recipient=recipient


            )
            serializer = MessageSerializer(
                message, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name",'last_name','username')
        
class NashUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = NashUser
        fields = ('user',)
        depth = 1
        


class MessageSerializer(serializers.ModelSerializer):
    sender = NashUserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'message', 'recipient', 'sender', 'date_posted','product')
        depth = 1
