from django.db import models
from common.models import BaseModel, SoftDeleteModel


class Experience(BaseModel, SoftDeleteModel):
    is_working = models.BooleanField(default=True)
    title = models.CharField(max_length=253, unique=True)
    organization_name = models.CharField(max_length=253)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True, default=None)
    description = models.TextField()

    def __str__(self):
        return self.title

