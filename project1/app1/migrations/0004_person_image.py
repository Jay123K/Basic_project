# Generated by Django 5.1.3 on 2024-11-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.FileField(null=True, upload_to='person_image'),
        ),
    ]
