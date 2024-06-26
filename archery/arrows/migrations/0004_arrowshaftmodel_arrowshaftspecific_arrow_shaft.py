# Generated by Django 5.0.6 on 2024-06-05 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrows', '0003_arrowcomponent_manufacturer_arrowcomponent_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrowShaftModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('inner_diameter', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ArrowShaftSpecific',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spine', models.IntegerField()),
                ('outer_diameter', models.FloatField()),
                ('weight_per_inch', models.FloatField()),
                ('max_mength', models.FloatField()),
                ('arrow_shaft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrows.arrowshaftmodel')),
            ],
        ),
        migrations.AddField(
            model_name='arrow',
            name='shaft',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='arrows.arrowshaftspecific'),
        ),
    ]
