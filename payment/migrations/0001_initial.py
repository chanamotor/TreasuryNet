# Generated by Django 2.2.7 on 2020-04-21 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdviceSeq',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('advice_date', models.DateField()),
                ('advice_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BillMaster',
            fields=[
                ('id', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('demand_no', models.CharField(blank=True, max_length=2)),
                ('ddo_code', models.CharField(max_length=7)),
                ('detail_head', models.CharField(max_length=2)),
                ('major_head', models.CharField(blank=True, max_length=4)),
                ('scheme_code', models.CharField(max_length=17)),
                ('dept_bill_no', models.IntegerField()),
                ('bill_type', models.CharField(max_length=2)),
                ('entry_date', models.DateField()),
                ('net_amt', models.BigIntegerField()),
                ('gross_amt', models.BigIntegerField(blank=True)),
                ('payment_type', models.CharField(blank=True, max_length=2)),
                ('flag', models.CharField(max_length=2)),
                ('online_bill_no', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillSeq',
            fields=[
                ('id', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BudgetMaster',
            fields=[
                ('id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('ddo_code', models.CharField(max_length=7)),
                ('detail_head', models.CharField(max_length=2)),
                ('scheme_code', models.CharField(max_length=17)),
                ('issue_date', models.DateField()),
                ('amount', models.BigIntegerField()),
                ('order_no', models.TextField()),
                ('da_no', models.IntegerField()),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('issued_by', models.TextField(blank=True)),
                ('user_code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='FinalBillMaster',
            fields=[
                ('id', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('demand_no', models.CharField(max_length=2)),
                ('ddo_code', models.CharField(max_length=7)),
                ('detail_head', models.CharField(max_length=2)),
                ('major_head', models.CharField(max_length=4)),
                ('scheme_code', models.CharField(max_length=17)),
                ('dept_bill_no', models.IntegerField()),
                ('bill_type', models.CharField(max_length=2)),
                ('entry_date', models.DateField()),
                ('net_amt', models.BigIntegerField()),
                ('gross_amt', models.BigIntegerField()),
                ('payment_type', models.CharField(max_length=2)),
                ('flag', models.CharField(max_length=2)),
                ('online_bill_no', models.IntegerField(blank=True)),
                ('voucher_no', models.IntegerField()),
                ('accounting_date', models.DateField()),
                ('encash_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentVoucherSeq',
            fields=[
                ('id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('month', models.CharField(max_length=2)),
                ('major_head', models.CharField(max_length=4)),
                ('voucher_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GpfTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('sanction_no', models.TextField(blank=True)),
                ('amount', models.BigIntegerField(blank=True)),
                ('grade', models.IntegerField(blank=True)),
                ('bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.BillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no')},
            },
        ),
        migrations.CreateModel(
            name='GpfDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('gpf_no', models.CharField(blank=True, max_length=20)),
                ('subscriber_name', models.CharField(blank=True, max_length=50)),
                ('amount', models.BigIntegerField(blank=True)),
                ('bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.BillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no', 'gpf_no')},
            },
        ),
        migrations.CreateModel(
            name='FinalGpfTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('sanction_no', models.TextField(blank=True)),
                ('amount', models.BigIntegerField(blank=True)),
                ('grade', models.IntegerField(blank=True)),
                ('final_bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.FinalBillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no')},
            },
        ),
        migrations.CreateModel(
            name='FinalGpfDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('gpf_no', models.CharField(blank=True, max_length=20)),
                ('subscriber_name', models.CharField(blank=True, max_length=50)),
                ('amount', models.BigIntegerField(blank=True)),
                ('final_bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.FinalBillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no', 'gpf_no')},
            },
        ),
        migrations.CreateModel(
            name='FinalBillTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('auditor_code', models.CharField(blank=True, max_length=4)),
                ('audit_date', models.DateField()),
                ('accountant_code', models.CharField(blank=True, max_length=4)),
                ('acc_approved_date', models.DateField()),
                ('authorizer_code', models.CharField(blank=True, max_length=4)),
                ('authorized_date', models.DateField()),
                ('flag', models.CharField(max_length=2)),
                ('final_bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.FinalBillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no')},
            },
        ),
        migrations.CreateModel(
            name='FinalBillSubDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('subdetail_head', models.CharField(blank=True, max_length=2)),
                ('amount', models.BigIntegerField(blank=True)),
                ('final_bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.FinalBillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no', 'subdetail_head')},
            },
        ),
        migrations.CreateModel(
            name='FinalBillDeductions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('scheme_code', models.CharField(blank=True, max_length=13)),
                ('major_head', models.CharField(blank=True, max_length=4)),
                ('amount', models.BigIntegerField(blank=True)),
                ('flag', models.CharField(blank=True, max_length=2)),
                ('voucher_no', models.IntegerField(blank=True)),
                ('final_bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.FinalBillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no', 'scheme_code')},
            },
        ),
        migrations.CreateModel(
            name='BillTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('auditor_code', models.CharField(blank=True, max_length=4)),
                ('audit_date', models.DateField()),
                ('accountant_code', models.CharField(blank=True, max_length=4)),
                ('acc_approved_date', models.DateField()),
                ('authorizer_code', models.CharField(blank=True, max_length=4)),
                ('authorized_date', models.DateField()),
                ('flag', models.CharField(max_length=2)),
                ('bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.BillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no')},
            },
        ),
        migrations.CreateModel(
            name='BillSubDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('subdetail_head', models.CharField(blank=True, max_length=2)),
                ('amount', models.BigIntegerField(blank=True)),
                ('bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.BillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no', 'subdetail_head')},
            },
        ),
        migrations.CreateModel(
            name='BillDeductions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('scheme_code', models.CharField(blank=True, max_length=13)),
                ('major_head', models.CharField(blank=True, max_length=4)),
                ('amount', models.BigIntegerField(blank=True)),
                ('flag', models.CharField(blank=True, max_length=2)),
                ('voucher_no', models.IntegerField(blank=True)),
                ('bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.BillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no', 'scheme_code')},
            },
        ),
        migrations.CreateModel(
            name='AdviceRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_year', models.CharField(max_length=9)),
                ('treasury_code', models.CharField(max_length=2)),
                ('bill_no', models.IntegerField()),
                ('advice_no', models.IntegerField()),
                ('bill_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.BillMaster')),
            ],
            options={
                'unique_together': {('fin_year', 'treasury_code', 'bill_no')},
            },
        ),
    ]
