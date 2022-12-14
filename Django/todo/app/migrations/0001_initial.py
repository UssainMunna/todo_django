# Generated by Django 4.1.3 on 2022-11-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TITLE', models.CharField(max_length=150)),
                ('STATUS', models.CharField(choices=[('PENDING', 'PENDING'), ('COMEPLETED', 'COMEPLETED'), ('INPROGRESS', 'INPROGRESS')], max_length=10)),
                ('DESCRIPTION', models.CharField(max_length=300)),
                ('DATE', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
