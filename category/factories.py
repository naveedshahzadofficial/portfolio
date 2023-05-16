from factory.django import DjangoModelFactory
from factory import fuzzy
from .model_enums import CategoryNames


class CategoryFactory(DjangoModelFactory):
    category_name = fuzzy.FuzzyChoice(CategoryNames)
    category_skill = fuzzy.FuzzyInteger(0, 100)

    class Meta:
        model = 'category.Category'
        django_get_or_create = ['category_name']
