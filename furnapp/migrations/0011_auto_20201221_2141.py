# Generated by Django 3.1.2 on 2020-12-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0010_auto_20201221_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('sofa', 'sofa'), ('bed', 'bed'), ('chair', 'chair'), ('tables', 'tables'), ('wardrobe', 'wardrobe'), ('lightning', 'lightning')], max_length=20, null=True),
        ),
    ]
