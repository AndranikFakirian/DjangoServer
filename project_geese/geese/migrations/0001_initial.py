# Generated by Django 4.2.7 on 2023-12-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=5000)),
                ('password', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=30)),
            ],
        ),
    ]