# Generated by Django 5.0.1 on 2024-02-12 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0003_alter_pizza_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
