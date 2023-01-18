# Generated by Django 4.1.5 on 2023-01-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('url', models.URLField()),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
    ]