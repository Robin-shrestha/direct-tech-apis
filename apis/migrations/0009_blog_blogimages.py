# Generated by Django 3.1.2 on 2020-11-19 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_auto_20201102_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255)),
                ('blog_body', models.TextField()),
                ('author', models.CharField(max_length=63)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='blog/%Y/%m/%d/')),
                ('blog_post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='apis.blog')),
            ],
        ),
    ]