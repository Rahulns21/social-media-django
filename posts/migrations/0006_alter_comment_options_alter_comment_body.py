# Generated by Django 5.0.2 on 2024-02-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=500),
        ),
    ]