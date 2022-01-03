from rest_framework.serializers import ModelSerializer
from .models import Post
from category.serializers import CategorySerializer


class PostSerializer(ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
