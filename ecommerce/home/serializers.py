
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import productcollectioninfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']



class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = productcollectioninfo
        fields = ['id','item_name','item_price','item_type','item_description','additional_info_weight','additional_info_dimensions','additional_info_material','additional_info_available_color','additional_info_size','item_image','item_Back_view','item_alone_view']