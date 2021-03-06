# Generated by Django 3.2 on 2022-05-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_rentinstance_renter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentinstance',
            name='dayprice',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='rentinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'On the road'), ('a', 'Available'), ('r', 'Reserved'), ('m', 'Maintenance')], default='a', help_text='Vehicle availability', max_length=1),
        ),
    ]
