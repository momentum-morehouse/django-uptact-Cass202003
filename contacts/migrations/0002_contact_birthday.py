# Generated by Django 3.0.8 on 2020-07-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
    ]
