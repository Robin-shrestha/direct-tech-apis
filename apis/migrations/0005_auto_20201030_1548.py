# Generated by Django 3.1.2 on 2020-10-30 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='Last_name',
        ),
        migrations.RemoveField(
            model_name='message',
            name='first_name',
        ),
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default='jon snow', max_length=60),
            preserve_default=False,
        ),
    ]