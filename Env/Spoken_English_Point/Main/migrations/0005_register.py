# Generated by Django 3.0.4 on 2020-09-20 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
            ],
        ),
    ]
