# Generated by Django 3.2.9 on 2021-12-06 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nashville_sell_and_trade_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nash_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nashville_sell_and_trade_api.nashuser')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nashville_sell_and_trade_api.product')),
            ],
        ),
    ]
