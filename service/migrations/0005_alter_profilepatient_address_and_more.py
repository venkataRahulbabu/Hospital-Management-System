# Generated by Django 4.1.4 on 2022-12-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_profilepatient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepatient',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profilepatient',
            name='bloodgroup',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='profilepatient',
            name='dateofbirth',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profilepatient',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
