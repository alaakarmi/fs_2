# Generated by Django 4.2.5 on 2024-01-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]