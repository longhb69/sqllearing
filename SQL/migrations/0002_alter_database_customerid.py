# Generated by Django 4.2.1 on 2023-06-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SQL', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='customerID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]