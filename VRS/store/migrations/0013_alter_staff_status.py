# Generated by Django 4.1.7 on 2023-03-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_staff_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Status',
            field=models.CharField(default='Staff', max_length=200, null=True),
        ),
    ]
