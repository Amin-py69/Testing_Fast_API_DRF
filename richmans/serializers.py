from rest_framework import serializers
from .models import RichMans


class RichManSerializer(serializers.Serializer):
    class Meta:
        model = RichMans
        fields = ('name', 'age', 'money', 'country', 'gender', 'image')

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absoluti_uri(image_url)
        return None
