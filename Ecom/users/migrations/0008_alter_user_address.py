# Generated by Django 4.1.7 on 2023-07-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='Syrai / Latakia', max_length=250),
        ),
    ]
