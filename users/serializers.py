from rest_framework import serializers
from django.contrib.auth.models import User
from django.http import HttpResponse

class RegisterSerializer( serializers.ModelSerializer ):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already present")
        return value
    
    def validate_password( self, value ):
        if len(value) < 5 :
            raise serializers.ValidationError("Password not strong! lenght should be more than 5")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance