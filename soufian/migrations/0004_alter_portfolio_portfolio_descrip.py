# Generated by Django 4.0.3 on 2022-03-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soufian', '0003_portfolio_portfolio_descrip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_descrip',
            field=models.CharField(max_length=70),
        ),
    ]