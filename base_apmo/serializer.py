from rest_framework import serializers
from .models import Sermon

class SermonSerializer(serializers.ModelSerializer):
    bg_picture_url = serializers.SerializerMethodField()
    audio_file_url = serializers.SerializerMethodField()

    class Meta:
        model = Sermon
        fields = '__all__'

    def get_bg_picture_url(self, obj):
        request = self.context.get('request')
        if obj.bg_picture and request:
            return request.build_absolute_uri(obj.bg_picture.url)
        return None

    def get_audio_file_url(self, obj):
        request = self.context.get('request')
        if obj.audio_file and request:
            return request.build_absolute_uri(obj.audio_file.url)
        return None
