# Generated by Django 3.0.3 on 2021-12-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_status',
            field=models.IntegerField(choices=[(1, 'active'), (0, 'inactive')], default=1),
        ),
    ]
