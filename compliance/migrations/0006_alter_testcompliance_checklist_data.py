# Generated by Django 5.1.3 on 2024-12-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0005_alter_testcompliance_checklist_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcompliance',
            name='checklist_data',
            field=models.JSONField(null=True),
        ),
    ]