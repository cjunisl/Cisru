# Generated by Django 2.2 on 2019-12-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_auto_20191223_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='feirista',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='folguista',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='extra',
            field=models.CharField(blank=True, choices=[('Folguista', 'Folguista'), ('Feirista', 'Feirista')], max_length=15),
        ),
    ]