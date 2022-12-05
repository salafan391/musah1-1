# Generated by Django 4.1.3 on 2022-12-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_remove_taskstatus_reason_taskassighn_reason_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskassighn',
            name='reason',
        ),
        migrations.AddField(
            model_name='taskstatus',
            name='reason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='state',
            field=models.CharField(blank=True, choices=[('منجزة', 'منجزة'), ('غير منجزة', 'غير منجزة')], default='تحت الإجراء', max_length=20, null=True),
        ),
    ]
