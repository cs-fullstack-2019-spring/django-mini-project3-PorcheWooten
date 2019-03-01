# Generated by Django 2.0.6 on 2019-03-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('school', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('hours', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dateOfWork', models.DateField()),
                ('dateOfEntry', models.DateTimeField()),
            ],
        ),
    ]