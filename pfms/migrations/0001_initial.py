# Generated by Django 2.2.7 on 2020-04-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PfmsFileSeq',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('fin_year', models.CharField(max_length=9)),
                ('file_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PfmsSchemeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goi_code', models.CharField(max_length=5)),
                ('budget_code', models.CharField(max_length=18)),
                ('demand_no', models.CharField(max_length=2)),
                ('detail_head', models.CharField(max_length=2)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'unique_together': {('goi_code', 'budget_code')},
            },
        ),
        migrations.CreateModel(
            name='PfmsExpenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('budget_code', models.CharField(max_length=18)),
                ('gross_amt', models.BigIntegerField()),
                ('net_amt', models.BigIntegerField()),
                ('accounting_date', models.DateField()),
                ('filename', models.CharField(max_length=30)),
                ('dated', models.DateField()),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no')},
            },
        ),
    ]
