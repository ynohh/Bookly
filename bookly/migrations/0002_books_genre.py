# Generated by Django 5.0.3 on 2024-04-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='genre',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
