# Generated by Django 4.1.4 on 2022-12-12 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_change',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
