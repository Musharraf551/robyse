# Generated by Django 5.1.6 on 2025-03-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_items_description_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='items',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='more',
            name='Item_name',
        ),
        migrations.DeleteModel(
            name='ItemList',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='More',
        ),
    ]
