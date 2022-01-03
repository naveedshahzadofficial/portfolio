from django.db import models


class CategoryNames(models.TextChoices):
    GENERAL = 'GENERAL'
    LARAVEL = 'LARAVEL'
    PYTHON = 'PYTHON'
    VUE = 'VUE'
    ANGULAR = 'ANGULAR'
    PHP = 'PHP'
