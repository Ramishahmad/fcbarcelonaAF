from mysite.models import posts
from rest_framework import serializers


class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = posts
        exclude = ['priority','draft','temporary']
        