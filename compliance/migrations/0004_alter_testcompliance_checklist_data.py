# Generated by Django 5.1.3 on 2024-12-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0003_testcompliance_checklist_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcompliance',
            name='checklist_data',
            field=models.JSONField(default={}),
        ),
    ]