# Generated by Django 4.1.3 on 2022-12-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_taskstatus_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskassighn',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='taskassighn',
            name='status',
        ),
        migrations.AddField(
            model_name='taskstatus',
            name='reason',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
