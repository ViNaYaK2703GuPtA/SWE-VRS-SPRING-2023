# Generated by Django 4.1.7 on 2023-03-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_staff_date_joined_staff_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Status',
            field=models.CharField(default='Staff', max_length=200, null=True, verbose_name='Staff'),
        ),
    ]