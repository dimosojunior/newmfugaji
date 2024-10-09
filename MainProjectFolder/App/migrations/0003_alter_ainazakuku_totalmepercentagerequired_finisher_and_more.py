# Generated by Django 4.2.6 on 2024-10-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_kumbusholachanjo_kundilakukuwake_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ainazakuku',
            name='TotalMEPercentageRequired_Finisher',
            field=models.CharField(blank=True, default=0, max_length=300, null=True, verbose_name='Kiwango Cha Jumla Cha ME Kwenye Kipindi  Cha Finisher - Kcal/kg'),
        ),
        migrations.AlterField(
            model_name='ainazakuku',
            name='TotalMEPercentageRequired_Grower',
            field=models.CharField(blank=True, default=0, max_length=300, null=True, verbose_name='Kiwango Cha Jumla Cha ME Kwenye Kipindi  Cha Grower - Kcal/kg'),
        ),
        migrations.AlterField(
            model_name='ainazakuku',
            name='TotalMEPercentageRequired_Layer',
            field=models.CharField(blank=True, default=0, max_length=300, null=True, verbose_name='Kiwango Cha Jumla Cha ME Kwenye Kipindi  Cha Layer - Kcal/kg'),
        ),
        migrations.AlterField(
            model_name='ainazakuku',
            name='TotalMEPercentageRequired_Starter',
            field=models.CharField(blank=True, default=0, max_length=300, null=True, verbose_name='Kiwango Cha Jumla Cha ME Kwenye Kipindi  Cha Starter - Kcal/kg'),
        ),
    ]
