# Generated by Django 5.1.3 on 2024-12-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestMethod',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(max_length=255, unique=True)),
                ('test_columns', models.JSONField()),
            ],
        ),
    ]
