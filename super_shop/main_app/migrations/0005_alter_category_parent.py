# Generated by Django 3.2 on 2021-04-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.CharField(max_length=20, null=True),
        ),
    ]