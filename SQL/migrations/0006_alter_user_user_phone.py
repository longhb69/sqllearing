# Generated by Django 4.2.1 on 2023-07-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SQL', '0005_sqltutorial_qizanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]