# Generated by Django 3.0.3 on 2021-12-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_auto_20211227_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
