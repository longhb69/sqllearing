# Generated by Django 4.2.1 on 2023-07-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SQL', '0003_rename_database_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]