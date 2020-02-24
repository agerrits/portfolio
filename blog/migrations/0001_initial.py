# Generated by Django 2.2.10 on 2020-02-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField(auto_now=True)),
                ('body', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
