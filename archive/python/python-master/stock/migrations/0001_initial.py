# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('deal_id', models.AutoField(serialize=False, primary_key=True)),
                ('deal_date', models.DateField(help_text=b'\xe6\x88\x90\xe4\xba\xa4\xe6\x97\xa5\xe6\x9c\x9f', verbose_name=b'\xe6\x88\x90\xe4\xba\xa4\xe6\x97\xa5\xe6\x9c\x9f')),
                ('stock_code', models.CharField(help_text=b'\xe8\x82\xa1\xe7\xa5\xa8\xe4\xbb\xa3\xe7\xa0\x81', max_length=6)),
                ('stock_name', models.CharField(help_text=b'\xe8\x82\xa1\xe7\xa5\xa8\xe5\x90\x8d\xe7\xa7\xb0', max_length=16)),
                ('operation', models.CharField(help_text=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb1\xbb\xe5\x9e\x8b', max_length=24, choices=[('\u8bc1\u5238\u4e70\u5165', '\u8bc1\u5238\u4e70\u5165'), ('\u8bc1\u5238\u5356\u51fa', '\u8bc1\u5238\u5356\u51fa'), ('\u80a1\u606f\u5165\u5e10', '\u80a1\u606f\u5165\u8d26'), ('\u7ea2\u80a1\u5165\u5e10', '\u7ea2\u80a1\u5165\u8d26'), ('\u7533\u8d2d\u4e2d\u7b7e', '\u7533\u8d2d\u4e2d\u7b7e'), ('\u80a1\u606f\u7ea2\u5229\u7a0e\u8865', '\u80a1\u606f\u7ea2\u5229\u7a0e\u8865')])),
                ('volume', models.SmallIntegerField(help_text=b'\xe6\x88\x90\xe4\xba\xa4\xe6\x95\xb0\xe9\x87\x8f')),
                ('balance', models.IntegerField(help_text=b'\xe5\x8f\x98\xe5\x8a\xa8\xe5\x90\x8e\xe6\x8c\x81\xe8\x82\xa1\xe6\x95\xb0\xe9\x87\x8f')),
                ('avg_price', models.DecimalField(help_text=b'\xe6\x88\x90\xe4\xba\xa4\xe5\x9d\x87\xe4\xbb\xb7', max_digits=5, decimal_places=2)),
                ('turnover', models.DecimalField(help_text=b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x91\xe9\xa2\x9d', max_digits=8, decimal_places=2)),
                ('amount', models.DecimalField(help_text=b'\xe5\x8f\x91\xe7\x94\x9f\xe9\x87\x91\xe9\xa2\x9d', max_digits=8, decimal_places=2)),
                ('brokerage', models.DecimalField(help_text=b'\xe4\xbd\xa3\xe9\x87\x91', max_digits=5, decimal_places=2)),
                ('stamp_tax', models.DecimalField(help_text=b'\xe5\x8d\xb0\xe8\x8a\xb1\xe7\xa8\x8e', max_digits=5, decimal_places=2)),
                ('transfer_fee', models.DecimalField(default=0.0, help_text=b'\xe8\xbf\x87\xe6\x88\xb7\xe8\xb4\xb9', max_digits=4, decimal_places=2)),
            ],
            options={
                'ordering': ['-deal_date'],
                'db_table': 'stock',
            },
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set([('deal_date', 'stock_code', 'operation', 'avg_price')]),
        ),
    ]
