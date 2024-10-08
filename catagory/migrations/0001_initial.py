# Generated by Django 5.1.1 on 2024-10-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('catagory_image', models.ImageField(blank=True, upload_to='photos/catagories')),
            ],
            options={
                'verbose_name': 'catagory',
                'verbose_name_plural': 'catagories',
            },
        ),
    ]
