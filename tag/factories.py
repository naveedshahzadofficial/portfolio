from factory.django import DjangoModelFactory
from factory import fuzzy


class TagFactory(DjangoModelFactory):
    tag_name = fuzzy.FuzzyText()

    class Meta:
        model = 'tag.Tag'
        django_get_or_create = ['tag_name']
