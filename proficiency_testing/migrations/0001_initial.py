# Generated by Django 5.1.3 on 2024-12-06 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test_methods', '0002_testmethod_test_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProficiencyTesting',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_start', models.DateField()),
                ('category', models.CharField(choices=[('GPT', 'Global PT Provider'), ('DM', 'Deep Metallurgy PT Provider')], default='GPT', max_length=50)),
                ('test_status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed')], default='pending', max_length=50)),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_methods.testmethod')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('test_id', 'test_start'), name='unique_test_per_date')],
            },
        ),
    ]