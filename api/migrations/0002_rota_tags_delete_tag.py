# Generated by Django 4.2.7 on 2023-11-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rota',
            name='tags',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]