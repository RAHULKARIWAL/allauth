# Generated by Django 3.1.3 on 2020-11-14 04:44

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201113_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='content',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
    ]
