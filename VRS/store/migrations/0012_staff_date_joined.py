# Generated by Django 4.1.7 on 2023-03-28 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_staff_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
