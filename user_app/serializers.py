import re
from user_app.models import *
from rest_framework import serializers

# Serializer: Login
# -------------------------------------------------------------------------------------------------------
class LoginSerializer(serializers.Serializer):
    wallet_address = serializers.CharField(max_length=255)

    def validate_wallet_address(self, value):
        # # Basic validation for OISY wallet address (adjust regex as needed)
        # if not re.match(r'^OISY[0-9A-Za-z]{30,}$', value):
        #     raise serializers.ValidationError("Invalid OISY wallet address format.")
        user = User.objects.filter(address=value).first()
        if user:
            self.context["user"] = user
        return value

    def create(self, validated_data):
        user = User.objects.create(
            address=validated_data["wallet_address"]
        )
        self.context["user"] = user
        return user
    
# Serializer: Profile
# -------------------------------------------------------------------------------------------------------
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["name", "username", "location", "email", "phone_number", "date_of_birth", "photo"]

    def validate_username(self, value):
        if Profile.objects.filter(username=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        if Profile.objects.filter(email=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance