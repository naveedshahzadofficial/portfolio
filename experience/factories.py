from factory.django import DjangoModelFactory
from factory.faker import Faker


# from factory import Sequence, PostGenerationMethodCall, sequence


class ExperienceFactory(DjangoModelFactory):
    is_working = Faker('boolean')
    title = Faker('sentence', nb_words=4)
    organization_name = Faker('company')
    from_date = Faker('past_date')
    to_date = Faker('past_date')
    description = Faker('text', max_nb_chars=153)

    class Meta:
        model = 'experience.Experience'
