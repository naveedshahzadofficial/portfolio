# Generated by Django 3.0.3 on 2022-01-03 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
            ],
            options={
                'unique_together': {('post_id', 'tag_id')},
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(through='post.TagPost', to='tag.Tag'),
        ),
    ]