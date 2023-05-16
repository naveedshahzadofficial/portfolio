from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from common.models import BaseModel, SoftDeleteModel
from .model_enums import CategoryNames


class Category(BaseModel, SoftDeleteModel):
    category_name = models.CharField(
        max_length=254,
        choices=CategoryNames.choices,
        default=CategoryNames.GENERAL,
        unique=True)
    category_skill = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    category_status = models.BooleanField(verbose_name='Active', default=True)

    def __str__(self):
        return self.category_name
