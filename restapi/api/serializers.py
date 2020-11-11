from rest_framework import serializers
from api.models import User, UserProfile, MyFile



class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('name','twitter','facebook','linkedin', 'photo') 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email',  'password', 'profile') 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.name = profile_data.get('name', profile.name)
        
        profile.twitter = profile_data.get('twitter', profile.twitter)
        profile.facebook = profile_data.get('facebook', profile.facebook)
        profile.linkedin = profile_data.get('linkedin', profile.linkedin)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance

    def delete(self, instance):
        profile = instance.delete()
        return " User deleted"


class MyFileSerializer(serializers.ModelSerializer):
    class Meta():
        model = MyFile
        fields = ('file', 'description', 'uploaded_at')
