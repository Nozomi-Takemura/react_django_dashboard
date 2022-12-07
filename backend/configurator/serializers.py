from rest_framework import serializers

from .models import Setting, SettingGroup

class SettingSerializer(serializers.HyperlinkedModelSerializer):

    # 'source' controls which attr. is used to populate a field  
    owner = serializers.ReadOnlyField(source='owner.email')
    highlight = serializers.HyperlinkedIdentityField(view_name='group-highlight')

    class Meta:
        model = Setting
        fields = ['url','id', 'settingname', 'settingvalue','owner','highlight'] 

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    # 'source' controls which attr. is used to populate a field  
    owner = serializers.ReadOnlyField(source='owner.email')
    # highlight = serializers.HyperlinkedIdentityField(view_name='group-highlight')

    class Meta:
        model = SettingGroup
        fields = ['url','groupname', 'owner'] 