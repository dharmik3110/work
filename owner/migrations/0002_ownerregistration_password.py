# Generated by Django 3.2.5 on 2022-03-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerregistration',
            name='password',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
