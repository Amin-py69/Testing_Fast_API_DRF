from rest_framework import serializers
from .models import Blogs, Comment
from django.utils.timezone import now


class BlogSerializer(serializers.ModelSerializer):

    comment = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blogs
        fields = ('title', 'description', 'user')
        validators = [

        ]


class CommentSerializer(serializers.ModelSerializer):
    the_pass_date = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_the_pass_date(self, obj):
        return (now() - obj.create).day



class UserSerializer():
    pass






    # def create(self, validated_data):
    #     request = Blogs.objects.get('request')
    #     validated_data['user'] = request.user
    #     return Blogs.objects.create(**validated_data)
