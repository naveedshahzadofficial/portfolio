from django.core.management.base import BaseCommand
from halo import Halo
from experience.factories import ExperienceFactory
from category.model_enums import CategoryNames
from category.factories import CategoryFactory
from post.factories import PostFactory, CategoryPostFactory


def _generate_experiences(amount: int):
    for key, value in CategoryNames.choices:
        CategoryFactory.create(category_name=key)
    # CategoryFactory.create_batch(len(CategoryNames.choices))
    # UserFactory.create_batch(amount)
    # CategoryPostFactory.create_batch(amount)
    PostFactory.create_batch(amount)
    # ExperienceFactory.create_batch(amount)


class Command(BaseCommand):
    help = 'Generate fake data and seed the models with theme, default are 10'

    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='The amount of fake data you want')

    @Halo(text='Generating...', spinner='dots', color='blue', text_color='blue')
    def handle(self, *args, **options):
        amount = options.get('amount') or 10
        _generate_experiences(amount)
