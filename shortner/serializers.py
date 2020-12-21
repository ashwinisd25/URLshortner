from rest_framework import serializers
from . models import shorturl

class ShorturlSerializer(serializers.ModelSerializer):
    class Meta:
        model = shorturl
        fields= ('id','original_url','short_url')
