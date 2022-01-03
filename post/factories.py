import random

from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import SubFactory, RelatedFactoryList


class CategoryPostFactory(DjangoModelFactory):
    post = SubFactory('post.factories.PostFactory')
    category = SubFactory('category.factories.CategoryFactory')

    class Meta:
        model = 'post.CategoryPost'
        django_get_or_create = ['category', 'post']


class TagPostFactory(DjangoModelFactory):
    post = SubFactory('post.factories.PostFactory')
    tag = SubFactory('tag.factories.TagFactory')

    class Meta:
        model = 'post.TagPost'
        django_get_or_create = ['tag', 'post']


class PostFactory(DjangoModelFactory):
    title = Faker('text', max_nb_chars=60)
    body = Faker('paragraph')
    categories = RelatedFactoryList(
        CategoryPostFactory,
        factory_related_name='post',
        size=lambda: random.randint(1, 6),
    )
    tags = RelatedFactoryList(
        TagPostFactory,
        factory_related_name='post',
        size=lambda: random.randint(1, 6),
    )

    class Meta:
        model = 'post.Post'
