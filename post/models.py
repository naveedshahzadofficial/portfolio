from django.db import models
from common.models import BaseModel, SoftDeleteModel
from category.models import Category


class Post(BaseModel, SoftDeleteModel):
    title = models.CharField(max_length=254, null=False)
    body = models.TextField(null=False)
    categories = models.ManyToManyField(Category, through='CategoryPost')


# https://docs.djangoproject.com/en/3.2/ref/models/fields/
class CategoryPost(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['post_id', 'category_id']]
