from django.shortcuts import render
from django.db.models import Prefetch, Count
from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer
from category.models import Category
from category.model_enums import CategoryNames


class QueryingTheDBView(ListAPIView):
    queryset = Post.objects.annotate(categories_count=Count('categories')).filter(
        categories__category_name__in=[CategoryNames.LARAVEL],
        categories_count=1
    ).prefetch_related(
        Prefetch(
            'categories',
            queryset=Category.objects.filter(category_name=CategoryNames.LARAVEL)
        ))
    serializer_class = PostSerializer
    # pagination_class = None
