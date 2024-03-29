from rest_framework import serializers
from userAuth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','first_name','last_name','username','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

        def validate(self,attrs):
            password=attrs.get('password')
            password2=attrs.get('password2')
            if password!=password2:
                raise serializers.ValidationError("Passord and confirm Password doesn't match")
            return attrs
        
        def create(self,validate_date):
            return User.objectss.create_user(**validate_date)