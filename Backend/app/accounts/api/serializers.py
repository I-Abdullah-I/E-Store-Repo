from rest_framework import serializers

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'type', 'balance']
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            full_name=self.validated_data['full_name'],
            type=self.validated_data['type'],
            # balance=self.validated_data['balance'],
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user