from rest_framework import serializers
from account.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['id', 'dni', 'username', 'first_name', 'last_name', 'direction', 'telephone', 'bornDate', 'is_client', 'is_active']
        read_only_fields = ['is_client', 'is_active']
        editable = ['is_client', 'is_active']