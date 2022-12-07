# Generated by Django 4.1.3 on 2022-12-07 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_remove_taskstatus_reason_remove_taskstatus_task_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('job_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='taskassighn',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.employeeadd'),
        ),
    ]