# Generated by Django 2.2.4 on 2019-09-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortnerModule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=120)),
            ],
        ),
    ]
