# Generated by Django 5.0.6 on 2024-06-17 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_code', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='JewelryType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('master_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('work_experience', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('status_code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('specialization_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('registration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('jewelry_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.jewelrytype')),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.material')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('client_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.client')),
                ('status_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.orderstatus')),
            ],
        ),
        migrations.CreateModel(
            name='OrderComposition',
            fields=[
                ('order_composition_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('jewelry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.jewelry')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.order')),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('production_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('jewelry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.jewelry')),
                ('master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.master')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialUsage',
            fields=[
                ('material_usage_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_used', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.material')),
                ('production_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.production')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
                ('review_date', models.DateField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.order')),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='specialization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UPAccs.specialization'),
        ),
    ]
