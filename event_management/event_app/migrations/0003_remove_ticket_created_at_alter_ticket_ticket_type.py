# Generated by Django 4.2.8 on 2024-09-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0002_ticket_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(max_length=100),
        ),
    ]
