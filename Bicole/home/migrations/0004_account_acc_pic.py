# Generated by Django 3.1.4 on 2021-02-28 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210227_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Acc_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
