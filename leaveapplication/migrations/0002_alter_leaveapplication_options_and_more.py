# Generated by Django 5.1.3 on 2024-12-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaveapplication',
            options={'ordering': ['-creation_date'], 'verbose_name': 'Leave Application', 'verbose_name_plural': 'Leave Applications'},
        ),
        migrations.RemoveField(
            model_name='leaveapplication',
            name='isApproved',
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='end_date',
            field=models.DateField(default=None, verbose_name='End Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='is_approved',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10, verbose_name='Approval Status'),
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='start_date',
            field=models.DateField(default=None, verbose_name='Start Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='reason',
            field=models.TextField(verbose_name='Reason'),
        ),
    ]
