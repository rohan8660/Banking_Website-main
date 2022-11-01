# Generated by Django 3.1.7 on 2022-11-01 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Data',
            fields=[
                ('Accno', models.IntegerField(primary_key=True, serialize=False)),
                ('Balance', models.FloatField()),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Customer_Data',
            fields=[
                ('Cust_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Phone_no', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=100)),
                ('mothers_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('Trans_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('Type', models.CharField(max_length=30)),
                ('Accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.account_data')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='Money_Transfers',
            fields=[
                ('Trans_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('From_accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From_accno', to='profiles.account_data')),
                ('To_accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To_accno', to='profiles.account_data')),
            ],
            options={
                'db_table': 'transfers',
            },
        ),
        migrations.CreateModel(
            name='ECS_Data',
            fields=[
                ('ECS_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Payer_Name', models.CharField(max_length=300)),
                ('Upper_Limit', models.FloatField()),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.account_data')),
            ],
            options={
                'db_table': 'ecs',
            },
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField()),
                ('Completed', models.BooleanField()),
                ('ECS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.ecs_data')),
            ],
            options={
                'db_table': 'bills',
            },
        ),
        migrations.AddField(
            model_name='account_data',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.customer_data'),
        ),
    ]
