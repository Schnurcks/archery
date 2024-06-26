# Generated by Django 5.0.6 on 2024-06-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrows', '0004_arrowshaftmodel_arrowshaftspecific_arrow_shaft'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrow',
            name='shaft_length',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='arrow',
            name='foc',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='arrow',
            name='total_weight',
            field=models.FloatField(null=True),
        ),
    ]
