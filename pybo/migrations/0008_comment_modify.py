# Generated by Django 4.0.3 on 2023-05-24 04:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0007_comment_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify',
            field=models.ManyToManyField(related_name='modify_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]