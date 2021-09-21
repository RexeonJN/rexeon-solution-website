# Generated by Django 3.1.6 on 2021-09-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rexeonapp', '0002_auto_20210917_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=None, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
