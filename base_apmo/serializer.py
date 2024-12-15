from rest_framework import serializers
from .models import Sermon

class SermonSerializer(serializers.ModelSerializer):
    bg_picture_url = serializers.SerializerMethodField()  # Include full URL for the image

    class Meta:
        model = Sermon
        fields = '__all__'

    def get_bg_picture_url(self, obj):
        request = self.context.get('request')
        if obj.bg_picture:
            return request.build_absolute_uri(obj.bg_picture.url)
        return None
