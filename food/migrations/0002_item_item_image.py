# Generated by Django 3.1.7 on 2021-03-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://zabas.com/wp-content/uploads/2014/09/Placeholder-food.jpg', max_length=500),
        ),
    ]
