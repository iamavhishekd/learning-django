from rest_framework import serializers
from userAuth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','first_name','last_name','username','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

        # def validate(self,attrs):
        #     password=attrs.get('password')
        #     password2=attrs.get('password2')
        #     if password!=password2:
        #         raise serializers.ValidationError("Passord and confirm Password doesn't match")
        #     return attrs
        
        def create(self,validated_data):
            print("-----")
            print(validated_data)
            print("-----")
            return User.object.create_user(**validated_data)