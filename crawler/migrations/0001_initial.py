# Generated by Django 2.1.1 on 2018-12-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=1000, null=True)),
                ('last_name', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'author',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('url', models.CharField(max_length=1000, null=True)),
                ('title', models.CharField(max_length=300)),
                ('date', models.IntegerField(null=True)),
                ('field', models.CharField(max_length=100, null=True)),
                ('publisher', models.CharField(max_length=1000, null=True)),
                ('cited_times', models.IntegerField(null=True)),
                ('abstract', models.CharField(max_length=8000, null=True)),
                ('authors', models.ManyToManyField(to='crawler.Author')),
            ],
            options={
                'db_table': 'paper',
                'managed': True,
            },
        ),
    ]
