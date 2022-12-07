from rest_framework import serializers
from django.contrib.auth import get_user_model

class ApplicationUserSerializer(serializers.HyperlinkedModelSerializer):

    # accounts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # settings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    settings = serializers.StringRelatedField(many=True)

    class Meta:
        model = get_user_model()
        fields = ['id','email','first_name','last_name','creation_date', 'settings']
