from django.db import models
from common.models import BaseModel


class Tag(BaseModel):
    tag_name = models.CharField(
        max_length=254,
        unique=True)
    tag_status = models.BooleanField(verbose_name='Active', default=True)

    def __str__(self):
        return self.tag_name

