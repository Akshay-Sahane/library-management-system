# Generated by Django 4.0.4 on 2022-04-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTable',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userId', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_Name', models.CharField(max_length=30)),
                ('last_Name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('is_superuser', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
