# Generated by Django 4.0.3 on 2022-03-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soufian', '0002_alter_about_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_descrip',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
    ]
